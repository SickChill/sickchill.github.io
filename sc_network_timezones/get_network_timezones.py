"""get_network_timezones.py

An over-engineered script for scraping networks (now called companies) from theTVDB and TVmaze and formatting them into something we can use.
"""

import argparse
import base64
import logging
import mimetypes
import os
import random
import re
import sys
import time
import traceback
import unicodedata
from pathlib import Path
from typing import Iterable, Optional, Set, Type
from urllib.parse import parse_qs, urlparse

import coloredlogs
import country_converter
import pytz
import verboselogs
from bs4 import BeautifulSoup
from pytz import country_timezones
from requests_cache import CachedSession

logger = logging.getLogger("")
country_converter_logger = logging.getLogger("country_converter")
country_converter_logger.setLevel(logging.ERROR)

TVMAZE_API_ROOT = "https://api.tvmaze.com"
TVMAZE_SITE_ROOT = "https://www.tvmaze.com"
TVMAZE_USER_AGENT = "SickChill-network-timezones (+https://github.com/SickChill/sickchill.github.io)"
SICKCHILL_NETWORK_IMAGES_REF = "develop"
# TVmaze allows at least 20 calls every 10 seconds; back off a little to stay under that.
TVMAZE_MIN_INTERVAL = 0.5
TVMAZE_ID_GAP_LIMIT = 100
TVDB_API_ROOT = "https://api4.thetvdb.com/v4"
# Same built-in project key as SickChill develop (settings.TVDB_V4_APIKEY_BUILTIN).
TVDB_V4_APIKEY_BUILTIN = base64.b64decode(b"YjMwNDExM2MtM2QxZi00NzdlLWFiNmQtZmRlYTNlMzYzZDUw").decode("ascii")


class Scraper:
    def __init__(self):
        self.session = CachedSession(cache_name="requests_cache.sqlite")
        self.session.headers.update({"User-Agent": TVMAZE_USER_AGENT})

        self.location = Path(__file__).parent

        self.verbose = False
        self.debug = False
        self.quiet = False

        self.purge_old = False
        self.start_page = 1
        self.number_of_pages = -1
        self._include_types = ["Network"]
        self.throttle = True
        self.throttle_seconds = None
        self._pages_processed = 0
        self.tvdb_apikey = os.environ.get("TVDB_V4_APIKEY") or TVDB_V4_APIKEY_BUILTIN
        self.tvdb_pin = os.environ.get("TVDB_V4_PIN") or ""

        self.output_file = self.location.joinpath("network_timezones.txt")
        self.discarded_file_path = self.output_file.parent.joinpath(f"DISCARDED_{self.output_file.name}")
        self.images_dir = None

        self.parser = argparse.ArgumentParser(
            epilog=f"""
                Network and timezones will be stored in: {self.output_file}
                All purged networks will be stored in: {self.discarded_file_path}
            """,
            description=__doc__,
            formatter_class=argparse.RawTextHelpFormatter,
        )

        self.parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="store_true",
            help="enable verbose logging",
        )
        self.parser.add_argument(
            "-d",
            "--debug",
            dest="debug",
            action="store_true",
            help="enable debug output",
        )
        self.parser.add_argument(
            "-q",
            "--quiet",
            dest="quiet",
            action="store_true",
            help="shush log output to only warnings and errors",
        )
        self.parser.add_argument(
            "-p",
            "--purge-old",
            dest="purge_old",
            action="store_true",
            help="purge items not found on theTVDB",
        )
        self.parser.add_argument(
            "-s",
            "--start-page",
            type=int,
            dest="start_page",
            default=self.start_page,
            help="page to start from",
        )
        self.parser.add_argument(
            "-n",
            "--numer-of-pages",
            type=int,
            dest="number_of_pages",
            default=self.number_of_pages,
            help="number of pages to parse",
        )
        self.parser.add_argument(
            "-o",
            "--output-file",
            dest="output_file",
            default=self.output_file,
            help="output filename",
        )
        self.parser.add_argument(
            "-i",
            "--include-types",
            dest="include_types",
            default=",".join(self.include_types),
            help="company types to include",
        )
        self.parser.add_argument(
            "--no-throttle",
            dest="throttle",
            action="store_false",
            help="do not sleep between pages",
        )
        self.parser.add_argument(
            "-t",
            "--throttle-seconds",
            type=int,
            dest="throttle_seconds",
            default=self.throttle_seconds,
            help="do not sleep between pages",
        )
        self.parser.add_argument(
            "--tvdb-apikey",
            dest="tvdb_apikey",
            default=self.tvdb_apikey,
            help="TheTVDB v4 API key (default: SickChill develop built-in, or TVDB_V4_APIKEY)",
        )
        self.parser.add_argument(
            "--tvdb-pin",
            dest="tvdb_pin",
            default=self.tvdb_pin,
            help="optional TheTVDB subscriber PIN (or TVDB_V4_PIN)",
        )
        self.parser.add_argument(
            "--images-dir",
            dest="images_dir",
            default=None,
            help="local SickChill images/network directory (default: sibling clone, else GitHub develop)",
        )

        self.parser.parse_args(namespace=self)
        if not isinstance(self._include_types, set):
            raw = self._include_types
            if isinstance(raw, (list, tuple, set)):
                raw = ",".join(str(item) for item in raw)
            self.include_types = raw

        if self.verbose:
            self.set_log_level(logging.VERBOSE)
        elif self.debug:
            self.set_log_level(logging.DEBUG)
        elif self.quiet:
            self.set_log_level(logging.WARNING)
        else:
            self.set_log_level(logging.INFO)

        # TVDB v4 /companies pages are 0-based; -s 1 still means "start of list".
        self._next_page = 0 if self.start_page <= 1 else self.start_page
        self._new_list = {}
        self._extra_companies = {}
        self._extra_company_types = []
        self._extra_dump_files = []
        self._tvdb_token = None
        self._tvdb_type_names = {}
        self._tvdb_name_index = {}

        self.country_converter = country_converter.CountryConverter(include_obsolete=True)

    def set_log_level(self, level: Type[int]):
        verboselogs.install()
        global logger
        logger = verboselogs.VerboseLogger("")
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(level)

        coloredlogs.install(level=level, logger=logger)
        for handler in logger.handlers:
            handler.setLevel(level)

    @property
    def include_types(self):
        return self._include_types

    @include_types.setter
    def include_types(self, value):
        self._include_types = {name.strip().lower() for name in value.split(",")}

    def _tvdb_login(self) -> str:
        if self._tvdb_token:
            return self._tvdb_token
        payload = {"apikey": self.tvdb_apikey}
        if self.tvdb_pin:
            payload["pin"] = self.tvdb_pin
        with self.session.cache_disabled():
            response = self.session.post(f"{TVDB_API_ROOT}/login", json=payload, timeout=30)
        response.raise_for_status()
        token = ((response.json() or {}).get("data") or {}).get("token")
        if not token:
            raise RuntimeError("TheTVDB v4 login did not return a token")
        self._tvdb_token = token
        return token

    def _tvdb_get(self, path: str, params: Optional[dict] = None) -> dict:
        url = f"{TVDB_API_ROOT}{path}"
        retries = 6
        backoff = 5
        response = None
        for attempt in range(1, retries + 1):
            headers = {
                "User-Agent": TVMAZE_USER_AGENT,
                "Accept": "application/json",
                "Authorization": f"Bearer {self._tvdb_login()}",
            }
            response = self.session.get(url, params=params, headers=headers, timeout=30)
            if response.status_code == 401:
                self._tvdb_token = None
                continue
            if response.status_code == 429 or response.status_code >= 500:
                logger.warning(f"TVDB {response.status_code} for {response.url}, retry {attempt}/{retries} in {backoff}s")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
                continue
            response.raise_for_status()
            payload = response.json()
            if not isinstance(payload, dict):
                raise RuntimeError(f"Unexpected TVDB response for {path}")
            return payload
        raise RuntimeError(f"TVDB request failed for {url}")

    def _tvdb_company_type_name(self, item: dict) -> str:
        company_type = item.get("companyType") or {}
        if isinstance(company_type, dict) and company_type.get("companyTypeName"):
            return company_type.get("companyTypeName")
        if not self._tvdb_type_names:
            payload = self._tvdb_get("/companies/types")
            for entry in payload.get("data") or []:
                type_id = entry.get("companyTypeId")
                type_name = entry.get("companyTypeName")
                if type_id is not None and type_name:
                    self._tvdb_type_names[int(type_id)] = type_name
        type_id = item.get("primaryCompanyType")
        try:
            return self._tvdb_type_names.get(int(type_id), "")
        except (TypeError, ValueError):
            return ""

    def scrape_tvdb(self):
        logger.info(f"Fetching TVDB v4 companies page: {self._next_page}")

        page = self._next_page
        if isinstance(page, (list, tuple)):
            page = page[0]
        page = int(page)

        payload = self._tvdb_get("/companies", params={"page": page})
        records = payload.get("data") or []
        included = {item.lower() for item in self.include_types}
        found = 0

        for item in records:
            company_name = (item.get("name") or "").strip()
            if not company_name:
                continue
            company_type = self._tvdb_company_type_name(item) or "Unknown"
            company_country = item.get("country") or ""
            found += 1
            if company_type.lower() in included:
                logger.verbose(f"Found result: {company_name}:{company_country} with type {company_type}")
                self._new_list[company_name] = company_country
            else:
                if company_type not in self._extra_companies:
                    self._extra_companies[company_type] = {}
                self._extra_companies[company_type][company_name] = company_country

        self._next_page = None
        self._pages_processed += 1

        if found == 0:
            logger.info(f"Reached the end of the TVDB v4 company list after {self._pages_processed - 1} page(s)")
            return

        logger.info(f"TVDB page {page}: {found} companies, {len(self._new_list)} included so far")

        if self.number_of_pages > 0 and self._pages_processed >= self.number_of_pages:
            logger.info(f"Reached our maximum number of pages to scrape: {self._pages_processed}")
            return

        next_url = (payload.get("links") or {}).get("next")
        if next_url:
            page_vals = parse_qs(urlparse(next_url).query).get("page") or []
            if page_vals:
                self._next_page = int(page_vals[0])

    def __process_tvmaze_result(self, item: dict, kind: str):
        if not item:
            return

        name = (item.get("name") or "").strip()
        if not name:
            return

        country = item.get("country") or {}
        timezone = country.get("timezone") or ""
        if not timezone:
            return

        canonical = self._tvdb_name_index.get(name.lower())
        if not canonical:
            logger.debug(f"Skipping TVmaze-only {kind}: {name}")
            return

        logger.verbose(f"TVmaze timezone for {canonical}: {timezone}")
        self._new_list[canonical] = timezone

    def _tvmaze_request(self, url: str, params: Optional[dict] = None, accept: Optional[str] = None):
        headers = {"User-Agent": TVMAZE_USER_AGENT}
        if accept:
            headers["Accept"] = accept

        retries = 6
        backoff = 5
        response = None
        for attempt in range(1, retries + 1):
            response = self.session.get(url, params=params, headers=headers, timeout=30)
            if response.status_code == 429 or response.status_code >= 500:
                logger.warning(f"TVmaze {response.status_code} for {response.url}, retry {attempt}/{retries} in {backoff}s")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
                continue
            return response

        return response

    def _tvmaze_get_resource(self, resource: str, resource_id: int) -> Optional[dict]:
        url = f"{TVMAZE_API_ROOT}/{resource}/{resource_id}"
        response = self._tvmaze_request(url, accept="application/json")
        if response is None:
            raise RuntimeError(f"No response from {url}")
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    def _tvmaze_ids_from_locs(self, locs: Iterable[str], resource: str) -> Set[int]:
        pattern = re.compile(rf"/{re.escape(resource)}/(\d+)(?:/|$)")
        ids = set()
        for loc in locs:
            match = pattern.search(loc)
            if match:
                ids.add(int(match.group(1)))
        return ids

    def _tvmaze_ids_from_sitemap(self, resource: str) -> Set[int]:
        ids = set()
        index_url = f"{TVMAZE_SITE_ROOT}/sitemaps/{resource}.xml"
        response = self._tvmaze_request(index_url)
        if response is None or response.status_code == 404:
            logger.debug(f"TVmaze sitemap not available for {resource}")
            return ids
        response.raise_for_status()

        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", response.text)
        child_maps = [loc for loc in locs if "/sitemaps/" in loc]
        page_urls = [loc for loc in locs if f"/{resource}/" in loc]

        for child in child_maps:
            child_response = self._tvmaze_request(child)
            if child_response is None or child_response.status_code >= 400:
                logger.warning(f"Failed to fetch TVmaze sitemap {child}")
                continue
            page_urls.extend(re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", child_response.text))
            self.sleep()

        ids = self._tvmaze_ids_from_locs(page_urls, resource)
        logger.debug(f"Found {len(ids)} TVmaze {resource} ids from sitemap")
        return ids

    def _tvmaze_ids_from_listing(self, resource: str) -> Set[int]:
        ids = set()
        page = 1
        id_pattern = re.compile(rf"/{re.escape(resource)}/(\d+)/")

        while True:
            response = self._tvmaze_request(f"{TVMAZE_SITE_ROOT}/{resource}", params={"page": page})
            if response is None or response.status_code == 404:
                break
            response.raise_for_status()

            page_ids = {int(match) for match in id_pattern.findall(response.text)}
            if not page_ids - ids and page > 1:
                break
            ids.update(page_ids)

            soup = BeautifulSoup(response.content, "html.parser")
            next_link = soup.select_one("li.next:not(.disabled) > a[href]")
            if not next_link:
                break

            href = next_link.get("href") or ""
            page_vals = parse_qs(urlparse(href).query).get("page") or []
            if not page_vals:
                break
            next_page = int(page_vals[0])
            if next_page <= page:
                break
            page = next_page
            self.sleep()

        logger.debug(f"Found {len(ids)} TVmaze {resource} ids from HTML listing")
        return ids

    def _tvmaze_ids_from_walk(self, resource: str) -> Set[int]:
        """Fall back to probing /{resource}/:id until a long run of 404s."""
        ids = set()
        resource_id = max(self.start_page, 1)
        consecutive_404 = 0
        logger.warning(f"Walking TVmaze {resource} ids starting at {resource_id}")

        while consecutive_404 < TVMAZE_ID_GAP_LIMIT:
            data = self._tvmaze_get_resource(resource, resource_id)
            if data:
                consecutive_404 = 0
                ids.add(resource_id)
            else:
                consecutive_404 += 1
            resource_id += 1
            self.sleep()

        logger.debug(f"Found {len(ids)} TVmaze {resource} ids by walking")
        return ids

    def _discover_tvmaze_ids(self, resource: str) -> list:
        ids = set()
        try:
            ids.update(self._tvmaze_ids_from_sitemap(resource))
        except Exception as error:
            logger.warning(f"Failed to read TVmaze {resource} sitemap: {error}")

        if not ids:
            try:
                ids.update(self._tvmaze_ids_from_listing(resource))
            except Exception as error:
                logger.warning(f"Failed to read TVmaze {resource} listing: {error}")

        if not ids:
            try:
                ids.update(self._tvmaze_ids_from_walk(resource))
            except Exception as error:
                logger.error(f"Failed to walk TVmaze {resource} ids: {error}")

        return sorted(resource_id for resource_id in ids if resource_id >= max(self.start_page, 1))

    def scrape_tvmaze(self):
        original_throttle = self.throttle_seconds
        if self.throttle and (self.throttle_seconds is None or self.throttle_seconds <= 0):
            self.throttle_seconds = TVMAZE_MIN_INTERVAL

        self._tvdb_name_index = {name.lower(): name for name in self._new_list}
        logger.info(f"Overlaying TVmaze timezones onto {len(self._tvdb_name_index)} TVDB network names")

        for resource, kind in (("networks", "Network"), ("webchannels", "WebChannel")):
            ids = self._discover_tvmaze_ids(resource)
            logger.info(f"Discovered {len(ids)} TVmaze {kind} ids")
            processed = 0
            for resource_id in ids:
                try:
                    data = self._tvmaze_get_resource(resource, resource_id)
                except Exception as error:
                    logger.warning(f"Error fetching TVmaze {kind} {resource_id}: {error}")
                    self.sleep()
                    continue
                if data:
                    self.__process_tvmaze_result(data, kind)
                    processed += 1
                self.sleep()
            logger.info(f"Finished processing {processed} {kind}s from tvmaze")

        self.throttle_seconds = original_throttle

    def scrape_tmdb(self):
        pass

    def sleep(self):
        if not self.throttle:
            return

        seconds = self.throttle_seconds
        if seconds is None or seconds <= 0:
            seconds = random.randint(1, 3)

        logger.debug(f"Sleeping for {seconds}")
        time.sleep(seconds)

    def dump_extra_company_types(self):
        logger.info("Dumping excluded types to corresponding txt files, in format {company}:{country} (not timezone!)")
        for company_type, companies in self._extra_companies.items():
            location = self.location.joinpath(f"{company_type.lower().replace(' ', '_')}_timezones.txt")
            self._extra_dump_files.append(location)

            logger.info(f"Dumping company type {company_type} to {location}")

            with open(location, mode="w", encoding="utf-8") as dump_file:
                for company, country in sorted(companies.items()):
                    new_value = self.country_name_to_timezone(company, country)
                    dump_file.write(f"{company}:{new_value}\n")

        self._extra_company_types = sorted(self._extra_companies)
        self._extra_companies.clear()

    @staticmethod
    def _as_iso2_code(code) -> Optional[str]:
        values = code if isinstance(code, (list, tuple, set)) else [code]
        for item in values:
            if not item or item == "not found" or not isinstance(item, str):
                continue
            item = item.strip().upper()
            if len(item) == 2 and item.isalpha():
                return item
        return None

    def country_name_to_timezone(self, network: str, value: str = None) -> str:
        if value is None:
            return ""
        if not isinstance(value, str):
            value = str(value)
        value = value.strip()
        if not value or value == "Unknown Country" or re.fullmatch(r"\d[\d,]*", value):
            return ""

        try:
            pytz.timezone(value)
            return value
        except pytz.exceptions.UnknownTimeZoneError:
            code = None
            for src in ("name_official", "name_short", "regex", "ISO2", "ISO3"):
                code = self._as_iso2_code(self.country_converter.convert(value, to="ISO2", src=src))
                if code:
                    break
            if not code:
                logger.debug(f"Did not find timezone for {network} from value {value}, returning empty")
                return ""

            zones = country_timezones.get(code) or []
            if not zones:
                logger.debug(f"No timezone map for {network} from country {code} ({value})")
                return ""
            return zones[0]

    def process_line(self, network, value):
        return network, self.country_name_to_timezone(network, value)

    def run(self):
        # Load data from TVDB network select box
        while self._next_page is not None:
            self.scrape_tvdb()
            self.sleep()

        self.scrape_tvmaze()

        logger.info(f"Processed {self._pages_processed} pages from theTVDB")

        self.dump_extra_company_types()

        old_list = []
        if self.output_file.is_file():
            with open(self.output_file, encoding="utf-8") as tz_file:
                for current in tz_file.readlines():
                    network, timezone = current.strip("\n").rsplit(":", 1)
                    old_list.append({"network": network, "time_zone": timezone})

        new_incomplete = new_complete = duplicate_count = 0
        new_data = []
        invalid_data = []

        def is_name_in_list(name, lst):
            for item in lst:
                if item.startswith(name + ":"):
                    return True
            return False

        logger.verbose("Listing valid old networks + time zones")
        logger.verbose("Action - Network Name - Time Zone")

        data_to_append = []
        while old_list:
            current = old_list.pop(0)

            line_format = f"{current['network']}:{current['time_zone']}\n"

            if is_name_in_list(current["network"], new_data + invalid_data):
                duplicate_count += 1
                logger.verbose(f"Duplicate - {current['network']} - {current['time_zone']}")
                continue

            if current["network"] not in self._new_list:
                if current["time_zone"]:
                    valid_timezone = self.country_name_to_timezone(current["network"], current["time_zone"])
                    if valid_timezone:
                        invalid_data.append(line_format)
                logger.verbose(f"Invalid: {current['network']} - {current['time_zone']}")
                continue
            else:
                if current["time_zone"]:
                    valid_timezone = self.country_name_to_timezone(current["network"], current["time_zone"])
                    if valid_timezone:
                        del self._new_list[current["network"]]
                        new_data.append(line_format)

                    logger.verbose(f"Re-adding: {current['network']} - {current['time_zone']}")

        logger.verbose("--- Adding new networks ---")
        logger.verbose("Action - Network Name - Country - Guessed Time Zone")

        for network, country in self._new_list.items():
            # try to determine time zone by country name in display name
            network, timezone_guess = self.process_line(network, country)
            if timezone_guess:
                new_complete += 1
                logger.debug(f"New network: {network} - {country} - {timezone_guess}")
                new_data.append(f"{network}:{timezone_guess}\n")
            else:
                new_incomplete += 1
                fixed_value = re.sub(re.escape(network) + r"(?:.* \((.*)\))?$", r"\1", country)
                logger.debug(f"New network: {network} - {fixed_value} - Unknown")
                data_to_append.append(f"{network}:{timezone_guess}\n")

        with open(self.output_file, mode="w", encoding="utf-8") as tz_file:
            if self.purge_old:
                if new_data:
                    new_data.sort()
                    tz_file.writelines(new_data)
            else:
                if new_data or invalid_data:
                    joined_data = new_data + invalid_data
                    joined_data.sort()
                    tz_file.writelines(joined_data)
            if data_to_append:
                data_to_append.sort()
                tz_file.writelines(data_to_append)

        if self.purge_old and invalid_data:
            with open(self.discarded_file_path, mode="w", encoding="utf-8") as tz_file:
                tz_file.writelines(invalid_data)

        logger.info("--- Done ---")
        logger.info(f"Processed {self._pages_processed} pages")
        logger.info(f"Skipped all {self._extra_company_types}")
        logger.info(f"New file created [{self.output_file.name}]")
        for extra_file in self._extra_dump_files:
            logging.info(f"New file created: {extra_file}")

        logger.info(f"Total {len(new_data)}")
        logger.info(f"New with time zone {new_complete}")
        logger.info(f"New without time zone {new_incomplete}")
        logger.info(f"Duplicates: {duplicate_count}")
        if invalid_data:
            if not self.purge_old:
                logger.info(f"Invalid networks added {len(invalid_data)}")
            else:
                logger.info(f"New file created [{self.discarded_file_path.name}]")
                logger.info(f"Total discarded {len(invalid_data)}")

        written = list(new_data)
        if not self.purge_old:
            written.extend(invalid_data)
        written.extend(data_to_append)
        self.missing_images(written)

    @staticmethod
    def _fold_network_name(name: str) -> str:
        # SickChill uses text_unidecode, then lower, then /\: -> spaces so the
        # filename is valid on disk.
        folded = None
        for module_name in ("text_unidecode", "unidecode"):
            try:
                unidecode = __import__(module_name, fromlist=["unidecode"]).unidecode
                folded = unidecode(name or "").lower().strip()
                break
            except ImportError:
                continue
        if folded is None:
            text = (name or "").replace("×", "x").replace("✕", "x").replace("–", "-").replace("—", "-")
            folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
            folded = folded.lower().strip()
        folded = re.sub(r"[/\\:]+", " ", folded)
        return re.sub(r"\s+", " ", folded).strip()

    @classmethod
    def _network_image_filename(cls, name: str) -> str:
        stem = cls._fold_network_name(name)
        return f"{stem}.png" if stem else ""

    @staticmethod
    def _is_image_filename(name: str) -> bool:
        guessed = mimetypes.guess_type(name)[0]
        if guessed and guessed.startswith("image/"):
            return True
        return name.lower().rsplit(".", 1)[-1] in {"png", "gif", "jpg", "jpeg", "svg", "webp"}

    def _default_images_dir(self) -> Optional[Path]:
        candidate = Path(__file__).resolve().parents[2] / "sickchill" / "sickchill" / "gui" / "slick" / "images" / "network"
        return candidate if candidate.is_dir() else None

    def _local_network_image_filenames(self, directory: Path) -> Set[str]:
        images = {
            path.name
            for path in directory.iterdir()
            if path.is_file() and self._is_image_filename(path.name)
        }
        if not images:
            raise RuntimeError(f"No network images found in {directory}")
        return images

    def _github_network_image_filenames(self) -> Set[str]:
        """Return filenames from SickChill's network logo directory on GitHub.

        The Contents API caps directory listings at 1000 entries; use the git tree instead.
        Compare against develop, which is the current image set before it lands on master.
        """
        headers = {"User-Agent": TVMAZE_USER_AGENT, "Accept": "application/vnd.github+json"}
        tree_url = f"https://api.github.com/repos/SickChill/SickChill/git/trees/{SICKCHILL_NETWORK_IMAGES_REF}?recursive=1"
        prefix = "sickchill/gui/slick/images/network/"
        response = self.session.get(tree_url, headers=headers, timeout=60)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict) or "tree" not in payload:
            raise RuntimeError(f"Unexpected GitHub tree response: {payload}")

        images = set()
        for entry in payload.get("tree") or []:
            path = entry.get("path") or ""
            if entry.get("type") != "blob" or not path.startswith(prefix):
                continue
            filename = path.rsplit("/", 1)[-1]
            if self._is_image_filename(filename):
                images.add(filename)

        if payload.get("truncated"):
            logger.warning("GitHub tree listing was truncated; some network images may be omitted")
        if not images:
            raise RuntimeError("GitHub network image tree was empty")
        return images

    def _load_network_image_filenames(self) -> Set[str]:
        images_dir = getattr(self, "images_dir", None)
        if images_dir:
            directory = Path(images_dir)
            logger.info(f"Using network images from {directory}")
            return self._local_network_image_filenames(directory)

        default = self._default_images_dir()
        if default:
            logger.info(f"Using local SickChill network images: {default}")
            return self._local_network_image_filenames(default)

        logger.info("Using GitHub develop network images")
        return self._github_network_image_filenames()

    def missing_images(self, network_list):
        try:
            existing_filenames = self._load_network_image_filenames()
        except Exception as error:
            logger.warning(f"Could not refresh missing/extra network images: {error}")
            return

        network_names = []
        seen = set()
        for line in network_list:
            name = line.rsplit(":", 1)[0].strip()
            if not name or name in seen:
                continue
            seen.add(name)
            network_names.append(name)

        network_stems = {self._fold_network_name(name) for name in network_names if self._fold_network_name(name)}
        extra_images = sorted(
            filename
            for filename in existing_filenames
            if self._fold_network_name(filename.rsplit(".", 1)[0]) not in network_stems
            and self._fold_network_name(filename.rsplit(".", 1)[0]) != "nonetwork"
        )
        missing = [
            name
            for name in network_names
            if not self._network_image_filename(name) or self._network_image_filename(name) not in existing_filenames
        ]

        missing_location = self.location.joinpath("missing_images.txt")
        with open(missing_location, "w", encoding="utf-8") as missing_file:
            missing_file.write("\n".join(missing))

        extra_location = self.location.joinpath("extra_images.txt")
        with open(extra_location, "w", encoding="utf-8") as extra_file:
            extra_file.write("\n".join(extra_images))

        logger.info(f"Network images: {len(existing_filenames)}")
        logger.info(f"Missing images count: {len(missing)}, Extra images count: {len(extra_images)}")


if __name__ == "__main__":
    scraper = Scraper()
    if sys.getdefaultencoding() != "utf-8" or sys.getfilesystemencoding() != "utf-8":
        logger.error("Default encoding and file system encoding must me utf-8 for use this script")
        logger.info(f"File system encoding is: {sys.getfilesystemencoding()}")
        logger.info(f"Default system encoding is: {sys.getdefaultencoding()}")
        sys.exit(1)
    scraper.run()

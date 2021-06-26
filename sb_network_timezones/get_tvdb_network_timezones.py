"""get_tvdb_network_timezones.py

An over-engineered script for scraping networks (now called companies) from theTVDB and formatting them into something we can use.
"""

import argparse
import json
import logging
import random
import re
import sys
import time
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import coloredlogs
import verboselogs
from bs4 import BeautifulSoup
from pytz import country_timezones
from requests_cache import CacheMixin
from requests_html import HTMLSession

from typing import Type

logger = logging.getLogger("")


class CachedHTMLSession(CacheMixin, HTMLSession):
    """Session with features from both CachedSession and HTMLSession"""


class Scraper:
    def __init__(self):
        self.session = CachedHTMLSession(cache_name="requests_cache.sqlite")

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

        self.output_file = self.location.joinpath("network_timezones.txt")
        self.discarded_file_path = self.output_file.parent.joinpath(f"DISCARDED_{self.output_file.name}")

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

        self.parser.parse_args(namespace=self)

        if self.verbose:
            self.set_log_level(logging.VERBOSE)
        elif self.debug:
            self.set_log_level(logging.DEBUG)
        elif self.quiet:
            self.set_log_level(logging.WARNING)
        else:
            self.set_log_level(logging.INFO)

        self.country_codes = CountryCode(self.location)

        self._next_page = self.start_page
        self._new_list = {}
        self._extra_companies = {}
        self._extra_company_types = []


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

    def scrape_tvdb(self):

        logger.info(f"Scraping page: {self._next_page}")

        companies_url = "https://thetvdb.com/companies/"

        data = self.session.get(companies_url, params={"page": self._next_page})

        soup = BeautifulSoup(data.content, "html.parser")

        company_rows = soup.find_all(class_="row mb-3")
        for _current in company_rows:
            company_name = _current.find(class_="mt-0 mb-0").get_text(strip=True)
            company_country = _current.find(class_="ml-0").get_text(strip=True)
            company_type = _current.find(class_="ml-1").get_text(strip=True)

            if company_type.lower() in [item.lower() for item in self.include_types]:
                logger.verbose(f"Found result: {company_name}:{company_country} with type {company_type}")
                self._new_list[company_name] = company_country
            else:
                if company_type not in self._extra_companies:
                    self._extra_companies[company_type] = {}
                self._extra_companies[company_type][company_name] = company_country

                logger.verbose(f"Skipping result: {company_name}:{company_country} with type {company_type}")

        # This must be before any return due to checks such as number of pages processed,
        # so that the loop is broken unless this is reset below to a value.
        self._next_page = None

        self._pages_processed += 1
        if self.number_of_pages > 0 and self._pages_processed >= self.number_of_pages:
            logger.info(f"Reached our maximum number of pages to scrape: {self._pages_processed}")
            return

        next_page = soup.find("a", attrs={"rel": "next"})
        if next_page and next_page.get("href"):
            parsed_url = urlparse(next_page["href"])
            query = parse_qs(parsed_url.query)
            self._next_page = query.get("page")

    def sleep(self):
        if self.throttle:
            seconds = self.throttle_seconds
            if seconds is None or seconds <= 0:
                seconds = random.randint(1, 3)

            logger.debug(f"Sleeping for {(seconds)}")
            time.sleep(seconds)

    def dump_extra_company_types(self):
        logger.info("Dumping excluded types to corresponding txt files, in format {company}:{country} (not timezone!)")
        for company_type, companies in self._extra_companies.items():
            location = self.location.joinpath(f"{company_type.lower()}_countries.txt")
            logger.info(f"Dumping company type {company_type} to {location}")
            with open(location, "w", "utf-8") as dump_file:
                for company, country in sorted(companies.items()):
                    dump_file.write(f"{company}:{country}\n")

        self._extra_company_types = sorted(self._extra_companies)
        self._extra_companies.clear()

    def run(self):
        # Load data from TVDB network select box
        while self._next_page is not None:
            self.scrape_tvdb()
            self.sleep()

        logger.info(f"Processed {self._pages_processed} pages from theTVDB")

        self.dump_extra_company_types()

        dump_list = {}
        file_path = self.location.joinpath("json_data", "tvseries-table-networks.json")
        with open(file_path, encoding="utf-8") as dump_file:
            for item in json.load(dump_file):
                item = item["Network"]
                if item not in dump_list and item not in self._new_list:
                    dump_list[item] = item

        # Load data from current list
        old_list = []
        if self.output_file.is_file():
            with open(self.output_file, encoding="utf-8") as tz_file:
                for current in tz_file.readlines():
                    name, time_zone = current.strip("\n").rsplit(":", 1)
                    old_list.append({"name": name, "time_zone": time_zone})

        new_count = auto_new_count = duplicate_count = 0
        new_data = []
        invalid_data = []

        def is_name_in_list(name, lst):
            for item in lst:
                if item.startswith(name + ":"):
                    return True
            return False

        logger.verbose("Listing valid old networks + time zones")
        logger.verbose("Action - Network Name - Time Zone")

        while old_list:
            current = old_list.pop(0)

            line_format = f"{current['name']}:{current['time_zone']}\n"

            is_duplicate = is_name_in_list(current["name"], new_data + invalid_data)
            if is_duplicate:
                duplicate_count += 1
                logger.verbose(f"Duplicate - {current['name']} - {current['time_zone']}")
                continue

            found_in_new = current["name"] in self._new_list
            found_in_dump = current["name"] in dump_list
            if not (found_in_new or found_in_dump):
                invalid_data.append(line_format)
                logger.verbose(f"Invalid: {current['name']} - {current['time_zone']}")
                continue

            if not current["time_zone"]:  # treat as new network
                continue

            # ensure that no duplicates are added
            if found_in_new:
                del self._new_list[current["name"]]
            if found_in_dump:
                del dump_list[current["name"]]

            new_data.append(line_format)
            logger.verbose(f"Re-adding: {current['name']} - {current['time_zone']}")

        data_to_append = []
        logger.verbose("--- Adding new networks ---")
        logger.verbose("Action - Network Name - Country - Guessed Time Zone")

        for key, value in self._new_list.items():
            # try to determine time zone by country name in display name
            tz_guess = ""
            code = self.country_codes[value]
            if code and len(code) <= 2:
                tz_guess = country_timezones(code)[0]

            if tz_guess:
                auto_new_count += 1
                logger.debug(f"New network: {key} - {value} - {tz_guess}")
                new_data.append(f"{key}:{tz_guess}\n")
            else:
                new_count += 1
                fixed_value = re.sub(re.escape(key) + r"(?:.* \((.*)\))?$", r"\1", value)
                logger.debug(f"New network: {key} - {fixed_value} - Unknown")
                data_to_append.append(f"{key}:{tz_guess}\n")

        match_country = re.compile(r"\(([a-z\s]+)\)$", re.I)
        for key, value_ in dump_list.items():
            # try to determine time zone by country name in display name
            tz_guess = ""
            country = re.findall(match_country, key)
            if country:
                code = self.country_codes[country[0]]
                if code and len(code) <= 2:
                    tz_guess = country_timezones(code)[0]

            if tz_guess:
                auto_new_count += 1
                logger.debug(f"New network: {key} - {country[0]} - {tz_guess}")
                new_data.append(f"{key}:{tz_guess}\n")
            elif country:
                new_count += 1
                logger.debug(f"New network: {key} - {country[0]} - Unknown")
                data_to_append.append(f"{key}:{tz_guess}\n")
            else:
                new_count += 1
                logger.debug(f"New network: {key} - Unknown - Unknown")
                data_to_append.append(f"{key}:{tz_guess}\n")

        with open(self.output_file, "w", "utf-8") as tz_file:
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
            with open(self.discarded_file_path, "w", "utf-8") as tz_file:
                tz_file.writelines(invalid_data)

        logger.info("--- Done ---")
        logger.info(f"Processed {self._pages_processed} pages")
        logger.info(f"Skipped all {self._extra_company_types}")
        logger.info(f"New file created [{self.output_file.name}]")
        for company_type in self._extra_company_types:
            location = self.location.joinpath(f"{company_type.lower()}_countries.txt")
            logging.info(f"New file created: {location}")

        logger.info(f"Total {len(new_data)}")
        logger.info(f"New with time zone {auto_new_count}")
        logger.info(f"New without time zone {new_count}")
        logger.info(f"Duplicates: {duplicate_count}")
        if invalid_data:
            if not self.purge_old:
                logger.info(f"Invalid networks added {len(invalid_data)}")
            else:
                logger.info("")
                logger.info(f"New file created [{self.discarded_file_path.name}]")
                logger.info(f"Total discarded {len(invalid_data)}")


class CountryCode:
    def __init__(self, location: "Path"):
        """Load countries data from json file"""
        self.countries = None
        self.location = location.joinpath("json_data", "countries.json")
        with open(self.location, encoding="utf-8") as countries_file:
            self.countries = json.load(countries_file)

        self.exceptions = {"UK": "GB"}

    def __getitem__(self, country):
        """Get country two-letter code from name"""
        return self.countries.get(country, self.exceptions.get(country, country))

if __name__ == "__main__":

    scraper = Scraper()
    if sys.getdefaultencoding() != "utf-8" or sys.getfilesystemencoding() != "utf-8":
        logger.error("Default encoding and file system encoding must me utf-8 for use this script")
        logger.info(f"File system encoding is: {sys.getfilesystemencoding()}")
        logger.info(f"Default system encoding is: {sys.getdefaultencoding()}")
        sys.exit(1)
    scraper.run()
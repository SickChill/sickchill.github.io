"""collect_missing_images.py

Download missing SickChill network logos into new_images/ as 8-bit RGBA PNG
(ImgBot-style strip + lossless PNG compression).

TVDB company icons are typically 512x512. The historic SickChill set is 64x32,
which is only 32px tall after letterboxing a square icon and looks muddy when
enlarged. The default here is 1024x512 (same 2:1 canvas) so a 512x512 source
is not downscaled.

Icons are taken from public thetvdb.com company HTML pages, not the TVDB API.
"""

import argparse
import logging
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

from requests_cache import CachedSession

from get_network_timezones import TVMAZE_USER_AGENT, Scraper

logger = logging.getLogger("collect_missing_images")

# 0 = no size cap. A 1024x512 RGBA logo is typically 10–80KiB; a few dense
# artwork files are 200–300KiB. Capping here is what made those look muddy.
MAX_BYTES = 0
TARGET_GEOM = "1024x512"
CONVERT = shutil.which("convert")
IDENTIFY = shutil.which("identify")
OPTIPNG = shutil.which("optipng")
GEOM_RE = re.compile(r"^(\d+)x(\d+)$")
TVDB_SITE = "https://thetvdb.com"
ICON_URL_RE = re.compile(
    r"https://artworks\.thetvdb\.com/banners/v4/company/\d+/icons/[A-Za-z0-9]+\.png"
)


def load_missing_names(path: Path) -> list:
    names = []
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if not name or name.startswith("#") or name in seen:
            continue
        seen.add(name)
        names.append(name)
    return names


def fold_filename(name: str) -> str:
    return Scraper._network_image_filename(name)


def company_slugs(name: str) -> list:
    folded = Scraper._fold_network_name(name)
    slug = re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")
    slugs = [slug]
    if "+" in name:
        slugs.append(re.sub(r"[^a-z0-9]+", "-", folded.lower().replace("+", "plus")).strip("-"))
        slugs.append(re.sub(r"[^a-z0-9]+", "-", folded.lower().replace("+", "")).strip("-"))
    no_paren = re.sub(r"\([^)]*\)", "", folded)
    alt = re.sub(r"[^a-z0-9]+", "-", no_paren.lower()).strip("-")
    if alt:
        slugs.append(alt)
    seen = set()
    unique = []
    for item in slugs:
        if item and item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def parse_geom(value: str) -> str:
    if not GEOM_RE.match(value or ""):
        raise argparse.ArgumentTypeError("size must be WxH, e.g. 1024x512")
    return value


def geom_wh(geom: str) -> tuple:
    width, height = geom.lower().split("x", 1)
    return int(width), int(height)


def image_wh(path: Path) -> tuple:
    if IDENTIFY:
        output = subprocess.check_output([IDENTIFY, "-format", "%w %h", str(path)], text=True)
    else:
        output = subprocess.check_output([CONVERT, str(path), "-format", "%w %h", "info:"], text=True)
    width, height = output.strip().split()
    return int(width), int(height)


def first_icon_url(html: str) -> Optional[str]:
    for url in ICON_URL_RE.findall(html or ""):
        if not url.endswith("_t.png"):
            return url
    return None


class Collector:
    def __init__(self, args):
        self.args = args
        self.session = CachedSession(cache_name="requests_cache.sqlite")
        self.session.headers.update({"User-Agent": TVMAZE_USER_AGENT})
        self.output_dir = Path(args.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.listing_icons = {}

    def fetch_html(self, url: str, params=None):
        response = self.session.get(url, params=params, timeout=30, headers={"User-Agent": TVMAZE_USER_AGENT})
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.text

    def scan_listings(self, wanted: set):
        """Map company name -> icon URL from public /companies listing pages."""
        if not wanted:
            return
        logger.info("Scanning thetvdb.com/companies HTML listings for icons")
        page = 1
        empty = 0
        while wanted:
            html = self.fetch_html(f"{TVDB_SITE}/companies/", params={"page": page})
            if not html:
                break
            names = re.findall(
                r'<h4 class="mt-1 mb-0"[^>]*>\s*<a href="/companies/([^"]+)">([^<]+)</a>',
                html,
            )
            thumbs = dict(re.findall(r'href="/companies/([^"]+)"[^>]*>\s*<img[^>]+src="([^"]+)"', html))
            for slug, listed_name in names:
                listed_name = listed_name.strip()
                icon = first_icon_url(thumbs.get(slug) or "")
                if not icon:
                    continue
                for key in (listed_name.lower(), Scraper._fold_network_name(listed_name)):
                    self.listing_icons[key] = icon
                    wanted.discard(key)
            if not names:
                empty += 1
                if empty >= 2:
                    break
            else:
                empty = 0
            if not re.search(r'rel="next"', html):
                break
            page += 1
            self.sleep()
        logger.info(f"Listing scan finished at page {page}, mapped {len(self.listing_icons)} company icons")

    def find_icon_url(self, name: str) -> Optional[str]:
        for key in (name.lower(), Scraper._fold_network_name(name)):
            if key in self.listing_icons:
                return self.listing_icons[key]

        for slug in company_slugs(name):
            html = self.fetch_html(urljoin(TVDB_SITE, f"/companies/{slug}"))
            if not html:
                continue
            icon = first_icon_url(html)
            if icon:
                return icon
        return None

    def download(self, url: str) -> Optional[bytes]:
        response = self.session.get(url, timeout=30, headers={"User-Agent": TVMAZE_USER_AGENT})
        if response.status_code != 200 or not response.content:
            return None
        return response.content

    def optimize(self, source: Path, dest: Path) -> bool:
        if not CONVERT:
            logger.error("ImageMagick 'convert' is required")
            return False

        geom = self.args.size
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp) / "work.png"
            # Lanczos on downscale; square 512x512 sources fit in 1024x512 without
            # shrinking the logo, then transparent letterbox to 2:1.
            cmd = [
                CONVERT,
                str(source),
                "-filter",
                "Lanczos",
                "-resize",
                geom,
                "-background",
                "none",
                "-gravity",
                "center",
                "-extent",
                geom,
                "+repage",
                "-alpha",
                "on",
                "-type",
                "TrueColorAlpha",
                "-depth",
                "8",
                "-strip",
                "-define",
                "png:color-type=6",
                "-define",
                "png:bit-depth=8",
                "-define",
                "png:compression-level=9",
                "-define",
                "png:compression-filter=5",
                "PNG32:" + str(work),
            ]
            subprocess.run(cmd, check=True, capture_output=True)

            if OPTIPNG:
                # -nc keeps TrueColor+alpha; default optipng may convert to a colormap.
                subprocess.run([OPTIPNG, "-o7", "-nc", "-quiet", str(work)], capture_output=True)

            size = work.stat().st_size
            if self.args.max_bytes and size > self.args.max_bytes:
                logger.warning(f"{dest.name} is {size} bytes after optimize (limit {self.args.max_bytes})")
                return False
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(work, dest)
            return True

    def sleep(self):
        if self.args.throttle > 0:
            time.sleep(self.args.throttle)

    def reencode_existing(self):
        pngs = sorted(self.output_dir.glob("*.png"))
        target_min = min(geom_wh(self.args.size))
        logger.info(f"Re-encoding {len(pngs)} existing logos to {self.args.size} 8-bit RGBA")
        logger.warning(
            "Re-encode cannot invent pixels. Already-shrunk 64x32 files stay muddy; "
            "re-download with --force (or delete new_images/*.png and collect again)."
        )
        ok = fail = skipped = 0
        for path in pngs:
            try:
                width, height = image_wh(path)
                if max(width, height) < target_min:
                    logger.warning(
                        f"Skip {path.name}: {width}x{height} is too small for {self.args.size}; use --force"
                    )
                    skipped += 1
                    continue
                if self.optimize(path, path):
                    ok += 1
                else:
                    fail += 1
            except subprocess.CalledProcessError as error:
                logger.warning(f"Re-encode failed for {path.name}: {error}")
                fail += 1
        logger.info(f"Re-encode done. ok={ok} skipped_too_small={skipped} failed={fail}")

    def run(self):
        if self.args.reencode:
            self.reencode_existing()
            return

        names = load_missing_names(Path(self.args.input_file))
        if self.args.limit > 0:
            names = names[: self.args.limit]
        logger.info(f"Collecting up to {len(names)} missing logos into {self.output_dir}")
        if self.args.scan_listings:
            wanted = {name.lower() for name in names}
            wanted.update(Scraper._fold_network_name(name) for name in names)
            self.scan_listings(wanted)

        saved = skipped = failed = existed = 0
        skipped_names = []

        for name in names:
            filename = fold_filename(name)
            if not filename:
                logger.info(f"No filesystem-safe logo name for {name}")
                skipped += 1
                skipped_names.append(name)
                continue
            dest = self.output_dir / filename
            if dest.exists() and not self.args.force:
                existed += 1
                continue

            try:
                icon_url = self.find_icon_url(name)
            except Exception as error:
                logger.warning(f"Lookup failed for {name}: {error}")
                failed += 1
                self.sleep()
                continue

            if not icon_url:
                logger.info(f"No public icon for {name}")
                skipped += 1
                skipped_names.append(name)
                self.sleep()
                continue

            raw = self.download(icon_url)
            if not raw:
                logger.warning(f"Download failed for {name}: {icon_url}")
                failed += 1
                self.sleep()
                continue

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                tmp.write(raw)
                src = Path(tmp.name)
            try:
                if self.optimize(src, dest):
                    logger.info(f"Saved {dest.name} ({dest.stat().st_size} bytes) for {name}")
                    saved += 1
                else:
                    failed += 1
            except subprocess.CalledProcessError as error:
                logger.warning(f"Optimize failed for {name}: {error.stderr.decode(errors='ignore')[:200]}")
                failed += 1
            finally:
                src.unlink(missing_ok=True)
            self.sleep()

        skip_file = self.output_dir / "skipped.txt"
        skip_file.write_text("\n".join(skipped_names) + ("\n" if skipped_names else ""), encoding="utf-8")
        logger.info(f"Done. saved={saved} skipped_no_icon={skipped} failed={failed} already_existed={existed}")
        limit = self.args.max_bytes or "unlimited"
        logger.info(
            f"Images are {self.args.size} 8-bit RGBA PNG, stripped, lossless-compressed, max {limit} bytes"
        )


def main():
    location = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input-file", default=str(location / "missing_images.txt"))
    parser.add_argument("-o", "--output-dir", default=str(location / "new_images"))
    parser.add_argument(
        "--size",
        type=parse_geom,
        default=TARGET_GEOM,
        help=f"output canvas WxH (2:1 RGBA). Default {TARGET_GEOM} so typical 512x512 TVDB icons are not downscaled",
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=MAX_BYTES,
        help="skip files larger than this after optimize; 0 (default) disables the cap",
    )
    parser.add_argument("--limit", type=int, default=0, help="process only the first N names")
    parser.add_argument("--throttle", type=float, default=0.5)
    parser.add_argument("--force", action="store_true", help="overwrite logos already in the output folder")
    parser.add_argument(
        "--reencode",
        action="store_true",
        help="re-optimize existing output files that already have enough pixels; does not re-download",
    )
    parser.add_argument(
        "--scan-listings",
        action="store_true",
        help="also scrape public /companies listing pages for thumbnail URLs",
    )
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.WARNING if args.quiet else logging.INFO,
        format="%(levelname)s %(message)s",
    )
    if not CONVERT:
        logger.error("ImageMagick convert not found on PATH")
        sys.exit(1)
    Collector(args).run()


if __name__ == "__main__":
    main()

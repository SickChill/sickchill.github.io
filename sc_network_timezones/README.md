Network Timezones for SickChill
====================

This holds all the timezone autoupdade info for SickChill. SickChill uses this data to display the Coming Episodes in the local timezone.

----------

**Part 1:**

File: *network_timezones.txt*

Content:

network name:timezone


----------


**Part 2:**
```bash
File: *get_network_timezones.py [-q] [-p]*

usage: get_network_timezones.py [-h] [-v] [-d] [-q] [-p] [-s START_PAGE] [-n NUMBER_OF_PAGES] [-o OUTPUT_FILE] [--no-throttle] [-t THROTTLE_SECONDS]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose logging
  -d, --debug           Enable debug output
  -q, --quiet           Shush log output to only warnings and errors
  -p, --purge-old       Purge items not found on theTVDB
  -s START_PAGE, --start-page START_PAGE
                        Page to start from
  -n NUMBER_OF_PAGES, --numer-of-pages NUMBER_OF_PAGES
                        Number of pages to parse
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output filename
  --no-throttle         Do not sleep between pages
  -t THROTTLE_SECONDS, --throttle-seconds THROTTLE_SECONDS
                        Do not sleep between pages

```
Arguments:
  - **-q** : Quiet - disable listing the preformed actions
  - **-p** : Purge - purge old/invalid networks (right now causes many missing networks for users.)<br>
  All purged networks are stored in *DISCARDED_network_timezones.txt*


Description: A Python script that fetches the latest network list from TheTVDB.com,
compares it to the current list to check for removed or new networks,
then rebuilds the list, sorted alphabetically.

* The script can guess most, if not all of the time zones.
The networks that it can't guess will be appended to the end of the list,
with an empty time zone.

* The script **will re-add** old/invalid networks by default.
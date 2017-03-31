Network Timezones for Sickbeard
====================

This holds all the timezone autoupdade info for Sickbeard. Sickbeard uses this data to display the Coming Episodes in the local timezone.

----------

**Part 1:**

File: *network_timezones.txt*

Content:

network name:timezone


----------


**Part 2:**

File: *update_networks_list.py [-q] [-p]*

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


----------


**Part 3:**

dateutil zoneinfo update

Version-Info-File: *zoneinfo.txt*

Content:

Zoneinfo-Filename md5hash


Data-File: *zoneinfo-.....tar.gz*

**BEFORE YOU OPEN AN ISSUE**
===============

Search for the error in the search box. Re-use the existing issue if it already exists, even if it is closed.
If you don't find it please follow the guidelines below, otherwise the issue will be closed.

**Update problems? Try this first:**

Stop SickChill, SSH(Linux)/CMD(Windows) and enter SickChill folder
```
git remote set-url origin https://github.com/SickChill/SickChill.git
git fetch origin
git checkout master
git branch -u origin/master
git reset --hard origin/master
git pull
```

## SickChill Bug/Issue Tracker
===============

This repo is dedicated to tracking bugs and issue reports only.

## SUBMITTING A BUG/ISSUE TICKET
(DO NOT POST ANYTHING THAT CONTAINS YOUR LOGIN INFORMATION OR API KEY)<br />
Please include the following when opening a new ticket:
 - Branch
 - Commit hash
 - Your operating system and python version
 - What you did
 - What happened
 - What you expected
 - Link to a copy/paste of your logfile with clear debug info of the error on [GIST](http://gist.github.com)

## ENABLING DETAILED DEBUGGING FOR LOGS
1. Open SR interface
2. Menu General Settings > Advanced Settings
3. Enable 'Enable debug'

Note: Synology users can use WinSCP to gain access/browse to the root where the SickChill log is located. /volume1/@appstore/sickbeard-custom/var/Logs/sickchill.log

## FAQ

https://github.com/SickChill/SickChill/wiki/FAQ's-and-Fixes

## Wiki

https://github.com/SickChill/SickChill/wiki

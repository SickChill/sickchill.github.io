### 2016.03.28-2

[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.28-2...master)

* Update french fansub.
* Added Subtile Provider Cache.
* Fixed Seeders and Leechers on TtN.
* Fixed brassetv and add others.
* Fixed web_root prepend for redirects.
* Fixed multiple timezone issues.
* Improved TorrentDay provider
* Improved unicode handling.
* Improved disk usage logic.
* Various fixes and code optimization

### 2016.03.28-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.28-1...master)

* Fixed transmission test connection
* Fixed binsearch provider, Remove alt.binaries.teevee (no longer exists) 
* Fixed btn provider.
* Fixed omgwtfnzbs provider.
* Fixed Shazbat passkey warning.
* Fixed web_root issue.
* Improved Use cookie auth for Synology DSM, and Show error messages for error codes. 
* Improved unicode handling
* Various fixes and code optimization

### 2016.03.23-1
[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.23-1...master)

* Fixed Some small bugs. 
* Improved unicode handling

### 2016.03.22-1
[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.22-1...master)

* Fixed SABNzbd cert. issues.
* Fixed Disable SSL verify in t411 since their cert does not match.
* Improved itasa provvider for better scores.
* Improved unicode handling.
* Fixed multiple small bugs. 
* Various fixes and code optimization

### 2016.03.20-1
[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.20-1...master)

* Improved Change wiki/issues links to main repo.
* Improved some providers.
* Fixed warning for the show 11.22.63 
* Only show commit hash for ERROR log lines
* Update nzbtomedia to V10.14
* Updated many libs.
* Generate API key more randomly and securely
* Check api limits and errors with hd4free
* Change NMA URL
* Show commit hash and branch even if we dont know the tag number (source installs especially)
* Fix download link on transmithenet
* Improved database process.
* Improved unicode handling.
* Added ItaSA subtitle provider
* Various fixes and code optimization

### 2016.03.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.10-1...master)

* Hotfix dateutil error for timezone names on Windows
* Fixed commit hash update notifications when using source install. 
* Fixed WEB-DL and WEB-Rip detections * Optimize regex * Add WEB detection * Add DLMux detection
* Fixed Make show filter on poster view case insensitive match.
* Fixed NoneType for CUR_COMMIT_HASH error when github is not available
* Fixed Don't error when show was already removed from trakt or never was on trakt.
* Fixed Nzbget issue
* Fixed network timezone reporting
* Fixed Searching tvdb to add shows when result contains a result that has no firstaired set.
* Improved Newznab provider handles show id internally now, and rid is no longer used.
* Improved Refresh show from dir even when it hasnt been updated on tvdb, but do not rebuild metadata.
* Improved pre-sort qualities for quality list
* Improved logging.
* Improved Boxcar2 notifier.
* Improved pushbullet notifier.
* Improved  pushalot notifier.
* Improved Updated "Sync File Extension" list for qBittorrent
* Improved URL handling.
* Added custom notification email subject
* Added anime category for bluetiger provider
* Various fixes and code optimization

### 2016.03.05-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.03.05-1...master)

* Improved Cache handling.
* Improved Create gists uploads as secret instead of public
* Improved Set default log size to 10MB to reduce rolling over.
* Improved logging.
* Improved airdate modify timestamp handling.
* Improved Refactored scene_quality 
* Improved Many providers
* Improved URL logging 
* Improved URL retreving.
* Improved Filter scene exceptions a bit different.
* Improved Add explanation about subliminal score math
* Improved Reduce subtitle score to match only Series, Season, Episode and Year
* Improved Subtitle options. 
* Fixed Gingadaddy, nzb.su and other providers who don't support the tvdbid search
* Fixed Don't limit allowed extensions to 3 chars
* Fixed Newznab cats that are disabled, shouldn't be shown in configure options tab.
* Fixed Continue PP when setting file timestamp to airdate chokes process.
* Fixed Changing categories for default newznab providers.
* Fixed Multiple unicode issues.
* Fixed Multiple Plex media server issues.
* Fixed Multiple subtitle issues.
* Fixed Didn't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Fixed Mede8er issue.
* Fixed Multiple small bugs
* Various fixes and code optimization
* Feature Added some new Network logo(s)
* Feature Add "ignore subs" setting in manual PP 
* Feature Allow file globs in "Sync File Extensions" setting to postpone postprocessing
* Feature Add option to keep only wanted subs

### 2016.02.22-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.16-1...2016.02.22-1)

* Fixed https://github.com/SickRage/sickrage-issues/issues/1028
* Fixed https://github.com/SickRage/sickrage-issues/issues/1042
* Fixed https://github.com/SickRage/sickrage-issues/issues/235#issuecomment-185068695
* Fixes url encoded censored items in logs not being censored.
* Force "Subtitles Multi-Language" if more than one wanted subtitle language
* Add option to keep only wanted subs
* Other Various subtitle ralted fixes
* Add PR/Issue templates
* Fix TPB when using an invalid proxy
* Improved show updater job logic
* Add "(musicbolt.com)" to removewordslist
* Minor cleanup and improvement to numerous search providers
* Various fixes and code optimization

### 2016.02.16-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.11-1...2016.02.16-1)

* Fix SickRage/sickrage-issues/issues/892
* Fix SickRage/sickrage-issues/issues/914
* Fix SickRage/sickrage-issues/issues/902
* Fix SickRage/sickrage-issues/issues/269
* Potentially fixed SickRage/sickrage-issues/issues/862
* Fix anime bluray detection
* Add option to ini to allow PMS update without token or user/pass when you dont require authentication - config.ini only option for now
* Dont run FINDSUBTITLES thread right on SR start
* Allow passing arguments future= and past= for range of weeks from today to add to the webcal http://localhost:8081/calendar?past=2&future=3 - both default to 52
* Allow file globs in "Sync File Extensions" setting to postpone postprocessing
* Reduce subtitle score to match only Series, Season, Episode and Year
* Allow changing categories for default newznab providers. Caveat: They are on the "Custom Newznab Providers" tab where you change the categories, until the js can be fixed
* Use generic exceptions for all seasons, not just season 1
* Various fixes for several search providers including: BinSearch, TPB, Alpharation, AbNormal Updates, KAT, TorrentLeech, Bitcannon, TorrentBytes, BTDigg, RARBG.
* Various bug fixes and code optimizations

### 2016.02.11-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.10-1...2016.02.11-1)

* Fix SickRage/sickrage-issues#818
* Fix SickRage/sickrage-issues#824
* Fix SickRage/sickrage-issues#852
* Partial fix of SickRage/sickrage-issues#12
* Fix anime bluray qualities
* Added network logos for RMC decouverte and UP TV
* Use .eu for podnapisi
* Don't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Updated subliminal and legendastv provider
* Plex notifier improvements
* Various code fixes and improvements

### 2016.02.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.09-1...2016.02.10-1)

* Use json scene exceptions
* Set "Authentication Failed" as a warning
* Fix issue where MTV doesn't download
* Various bug fixes


### 2016.02.09-2

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.08-1...2016.02.09-1)

* Use xem absolute numbers for tvdb mapping if tvdb doesnt provide them, fixes american dad if you disable scene numbering
* Dont pass q on rss update, use sickbeard.USENET_RETENTION directly regardless of mode
* Set search string for subsequent scene exceptions after tvdbid has been popped
* Fix provider log message by decoding to utf-8 instead
* Fix daily search issues with ABNormal

### 2016.02.08-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.02.07-1...2016.02.08-1)

* Make sickbeard.gh work even when github login settings are incorrect
* Display exception text from NameParser in validateDir
* Fix for nzb indexers who dont support tvdbid or happen to have missed a tvdbid mapping for some shows/episodes
* Fix "No processable items found in folder" by building name cache on startup... /slap miigotu and his miibugs
* Swap settings order "Alternate search mode as fallback is fine" and "Season search mode"
* Update nzbToMedia to V10.13 thanks to @clinton-hall
* Standardize providers
* Add log message to warn user and/or help debug possible issues
* Dont unpack again if files were previously unpacked when
* Fix issue when release is RARred
* Revert "Fetch only current branch. Not all branches"
* Fix schedule so it doesnt bork when db upgrade
* Fix bug that caused plex server/client password to be set to all * when saving notifications if you did not type them in after loading the page
* Fix small mistake in name_parser, use better variable names in quality pills
* Various code and mako updates and optimizations

### 2016.02.07-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.01.31-1...2016.02.07-1)

* Encode io.open in helper with ek() 
* Updated subliminal develop (f245383)
* Updated guessit (28b6789)
* Updated rebulk (68a4588)
* Re-enable cachecontrol
* Fix testing providers search types manually
* Fix log showing errors incorrectly
* Change speed.cd url to use https
* Use node 5.0.0 instead of 0.12 for build tests, make npm quiet during ci, updated npm deps
* Replaced all menu icons and logos with colored versions
* Fix bug in PP where rar'd files would say there were no processable items found in folder after extraction
* Fix typeError breaking backlog/manual/failed searches
* Add editorconfig
* Dont show traceback if error sending torrent
* Dont clear old snatch history in failed.db, see if that fixes some issues with fdh
* Revert "Added add from popular anime list"
* Revert "Added anidb http client"
* Clean up recommended.py
* Fix issues with various strings, changes to the help and info page
* Various group and provider updates (incl. bitcannon, legendastv)
* Various codefixes and optimizations

### 2016.01.31-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.01.23-1...2016.01.31-1)

* Fix restart not reloading page
* Added UHD quality support (4k, 8k, etc)
* Updated subliminal to latest version
* Updated guessit to v2
* Fix some missing imports and undefined variables
* Fix boxcar2/freemobile sms
* Fix null season numbers being added to db
* Fix adding anime shows causing mako errors
* New icons on the status page
* Fix several providers
* Many small random fixes
* Add an "Add from anidb popular list" page

### 2016.01.23-1

[full changelog](https://github.com/SickRage/SickRage/compare/2016.01.20-1...2016.01.23-1)

* Remove duplicate FDH setting
* Add seeds/leechers to some log messages during searches 
* Refactor the way we initialize provider caches 
* Standardize providers more 
* Add ABNormal and PhxBit providers 
* Fix newznab issues with pre-aired episodes and maxage, and bad q params 
* Fix several UI bugs 
* Add SSL Version to help & info page, and make it pretty 
* Fix error when PP finds file of same size exists 
* Prepare to add ability to add shows from anidb lists (if they are on tvdb) 
* Fix confirmed downloads setting for TPB which was only allowing unconfirmed results 
* Fix discrepancy between home and display show for show file size when show has multi-eps 
* Fix t411 
* Fix several NoneType exceptions

### 2016.01.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/v5.1.1...2016.01.20-1)

* Change TPB domain back to .se, use a custom url if it doesnt work
* Fix restart on gentoo 
* Randomize default show updater hour between 2-4 am 
* Randomize show updater minute during that hour (helps spread load for indexers) 
* Adjust some errors to warnings, especially in telegram 
* Fix email notifier when using TLS 
* Update torrentbytes icon, add some missing network logos 
* Fix omgwtfnzbs and newznab improvements 
* Fix RARBG 
* Update GFTracker provider code to new format 
* Switch to nosetests and abandon custom unit test loader 
* Fix NZBGet HTTPS setting and sabNZBd Forced Priority setting 
* General refactoring and code cleanup

### 5.1.2 (2016-01-14)

[full changelog](https://github.com/SickRage/SickRage/compare/v5.1.1...v5.1.2)

* Rework newznab.py to use new search strings and fix categories and torznab
* Add some custom provider logos 
* Add some unit tests for convert_size method 
* Fix an errant comma in the kodi notifier 
* Fix some misplaced bold fonts for the font type sticklers (oh, my eyes!!!11!) 
* Add support for minor db versions 
* Fix trendingShows reload on change 
* Remove TitansOfTV 
* Re-Enable CPasbien

### 5.1.1 (2016-01-13)

[full changelog](https://github.com/SickRage/SickRage/compare/v5.1...v5.1.1)

* Remove titansoftv and animenzb (down)
* Fixed about 10 broken providers
* Rewrote many providers, more to come
 * thepiratebay, speed.cd, morethantv, torrentleech, danishbits, freshontv, btdigg, bitsnoop
 * rarbg, xthor, hd-torrents, alpharatio, iptorrents, extratorrent, scenetime, hd4free, tokyotoshokan (more)
* Add size parsing to many providers
* Updated subliminal to 17cce96
* Added Custom error page and 404 page
* Removed some unused code, cleanup code, and start moving toward python3
* Various bug fixes along the way

### 5.1 (2016-01-03)

[full changelog](https://github.com/SickRage/SickRage/compare/v5.0.3...v5.1)

* Refactor Plex Media Server and Plex Home Theater Notifiers
* Fix PHT (PMC) Notifier, Uses Kodi notifier for PHT/PMC notifications
* Add HTTPS option for Plex Media Server
* Fix sorting of home page on initial load, and partial layout issues
* Reword a lot of config/notifications for clarity
* Remove git-autoissues code
* Update subliminal to latest git dev version
* Make sure status is a long integer before comparing to int
* Fix DB upgrade from vanilla Sick-Beard DB
* Fix potential issue with DB row_type being incorrect for a DB connection action and make it thread safe
* Fix identity vs equality issue in logger when checking for SSL exceptions
* Fix some typos in log lines in metadata generator
* Lint tv.py and fix a few small issues
* Restore original SB behavior is the 'paused' parameter in webapi

--------

[Changelog 2016](https://github.com/SickRage/sickrage.github.io/raw/master/sickrage-news/CHANGES.md)
[Changelog 2015](https://github.com/SickRage/sickrage.github.io/raw/master/sickrage-news/CHANGES-2015.md)
[Changelog 2014](https://github.com/SickRage/sickrage.github.io/raw/master/sickrage-news/CHANGES-2014.md)

### v2017.01.01-1

[full changelog](https://github.com/SickRage/SickRage/compare/1db7ce5220bac059246d1967ee145bd71203ea89...v2017.01.01-1)

* Make sure the show location exists or at least the root dir exists and is set for the show dir. Fixes #2521
* Update "Bot" name (#2819)
* Update add torrent paused for rtorrent (#2820)
* Fix #2690 - Show location encoding error with latin-1 when changing root dir in mass edit or location in editShow Set utf-8 for accept-encoding and encoding of some js files Fix problem where users got confused that the filebrowser didnt keep the location they typed in the location filebrowser but didnt hit enter, now it uses the location in the text box always, which is also updated when you click dirs

### v2016.12.30-1

[full changelog](https://github.com/SickRage/SickRage/compare/2c4eddbdbf40c2ec56a3897225d5c29dbaa28ffb...v2016.12.30-1)

* Fix #2815 - Anime regex matching wrong
* Fix up linux desktop notifications, add some missing notifications
* Catch some unnecessary gi.repository warnings, remove some unnecessary error logs
* Support for adding torrents as paused to rTorrent
* AuthException is when they provide wrong user/pass, its not an error

### v2016.12.27-1

[full changelog](https://github.com/SickRage/SickRage/compare/a88b77a2b76b32b2db4644a8481ada60df71fb46...v2016.12.27-1)

* Fix #2079
* bobbysteel - Remove dead provders: bluetigers btdigg ilovetorrents, replaces #2720 (#2801)
* Fix score detection (#2800)
* Fix missed js in trendingShows and other issues, Fixes #2725
* Use proxy everywhere when proxy is set: imdb, tvdb. Remove proxy_indexers setting Fixes #2685

### v2016.12.20-2

[full changelog](https://github.com/SickRage/SickRage/compare/1983507caa0a1759a059c9179d4fcd89de9e08e7...v2016.12.20-2)

* Update subliminal to 2.1.0.dev

### v2016.12.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/a097e440a4b3cfe075dcb426e8cd7c24b4606d49...v2016.12.20-1)

* Remove network_timezones lib and make network_timezones.py use lowercase network keys (#2721)

### v2016.12.18-1

[full changelog](https://github.com/SickRage/SickRage/compare/17e9b81c71fd4ae12ab2371998c8fa04bee4fd7a...v2016.12.18-1)

* Reduce noise from the episode parser. (#2709)
* Fix regex for RARBG.mp4, Fixes #2705 Fix tests and add RARBG.mp4 to test strings.
* Popup auth for putio when you click test, user needs to make sure a popup blocker doesnt block it
* (2706) If file name has more than 4 episode numbers, make sure it doesnt match since it isnt a real episode its a compilation. Fixes #2706
* Include twilio notification service (#2693)
* Added Pushover priority (#2707)
* Include 2160p TV shows in search categories (#2704)

### v2016.12.15-1

[full changelog](https://github.com/SickRage/SickRage/compare/a1bf3b30a9a0d6319c09fb0cf48d2d468dbf4e61...v2016.12.15-1)

* Try and set upstream on branch before checking latest commit hash from remote, Fixes #2657 (#2700)
* issuee with refresh paused s show (#2694)
* Add torrent9.biz provider (#2681)
* added option to disable autorefresh for shows paused and ended (#2683)

### v2016.10.28-1

[full changelog](https://github.com/SickRage/SickRage/compare/17ee2872052786b7824c78acbb50e1ea6b0b90f7...v2016.10.28-1)

* Add cookie auth to ipt, Fixes #2511
* Newpct hdtv by url (#2524)
* IRIB TV1 (Tehran Iran) (#2520)

### v2016.10.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/9b2f19888d6c12e8b2d1693f6161ed123a779be4...v2016.10.20-1)

* Add custom_url option for IPT, Fixes #2511 Fix custom_url for TPB
* Tagger resolution improvements (#2431)
* Images - networks: adjusted Rai logos ratios and added new Italian networks (#2513)
* Typo in apibuilder causes double parameter (#2509)

### v2016.10.18-1

[full changelog](https://github.com/SickRage/SickRage/compare/f67267f210a487d209f88cf3384a0e59facb3f97...v2016.10.18-1)

* Fixes #2508 - It's only a visual issue since PP can only run once at a time anyways
* Fix size parsing for TPB Use categories and check only tv-shows and hd shows for rss in TPB Convert URL for TPB before requesting to avoid a 302 (The 301 is expected due to the .se redirector to best mirror) Fix an issue with title parsing, sometimes had js in the title
* Rai network logos (#2491)
* Elitetorrent seeders (#2469)
* Optimize imports
* Clean up logger a bit, fix no-member warning for log

### v2016.10.11-1

[full changelog](https://github.com/SickRage/SickRage/compare/0583eb4bbbdb227fe0b850e43e0ecf83061bf3c2...v2016.10.11-1)

* Mostly bug fixes
* Replaces #2436 (elitetorrents throttling)
* Try to fix #2292 (slack notification exception)
* Update GenericProvider.py (#2461)
* Ability to select which root dir to show shows from on home page (#2458)
* Fix #2308 - Plex request will never go through proxy
* Update guessit and rebulk
* Compare lowercase for showlist sort (#2454)
* Remove header updates who are incorrectly overwriting UA.
* Fix #2445, #2415, #2177, #2444, #2428

### v2016.10.07-1

[full changelog](https://github.com/SickRage/SickRage/compare/433fd54986ca7d855c022a0fdc0a64a7ed0f7e1a...v2016.10.07-1)

* Fix adding shows with ' in the name (#2441)
* Add cloudflare-scrape
* Remove shutil_custom.copyfile_custom hack. Official one should work fine, and uses a smaller buffer (No reason to use 128MB of mem to copy a file) (#2435)

### v2016.10.05-1

[full changelog](https://github.com/SickRage/SickRage/compare/b8e13a4837fd64efb83b1f7134c49fa2c621fb08...v2016.10.05-1)

* Attempt to fix #2429, and also show proper parser result in the log (#2434)
* Added FileList.ro torrent provider (#1145)
* Fix #1874 (#2420)

### v2016.09.28-1

[full changelog](https://github.com/SickRage/SickRage/compare/4127db91f7ae3d9638fcad1fb67113be0a1bf931...v2016.09.28-1)

* Update subliminal to 2.1.0.dev
* Fix wrong season for season banners and posters #2011

### v2016.09.18-1

[full changelog](https://github.com/SickRage/SickRage/compare/38757cd9a849eb3ecfef4d22610c81f8549f0e52...v2016.09.18-1)

* b6041e9 Add openSans to grunt's mainFiles to suppress warning and include css
* 38757cd Added NZBFinder.ws as default provider (#2179)
* 951532d Issue 1907 (#2344)
* 34df1e2 providers/scenetime: Fix broken search after site changes (#2335)
* 7f68d18 Fixed Dave network logo (#2326)
* a30221a Added HorribleSubs as provider (#2246)
* 74c66d8 Outline poster with table (#2320)

### v2016.09.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/8564c29aa3b2d95bf41e03eed7e5a6938f1a6b3a...v2016.09.10-1)

* 043fb0d (origin/develop, develop) Update pullapprove.yaml
* b7d3e5e Fixes #2311 (#2317)
* c7800a0 Use Torrentz2 (#2312)
* 82e88de replaced banner.png (#2309)
* 070e000 Fix dupe import in itasa
* cec3bcb Parser exception (#2302)
* b0fe360 Various UI tweaks (#2298)

### v2016.09.03-1

[full changelog](https://github.com/SickRage/SickRage/compare/4219585709dc1d9ed23ec7ea773a51e92c97b7b5...v2016.09.03-1)

* Fix slack error breaking post processing when NOTIFY_SUBTITLE settings are used.
* Fix icon wrapping in cubmenu on error viewer
* -----END PGP SIGNATURE-----

### v2016.09.01-1

[full changelog](https://github.com/SickRage/SickRage/compare/75042d8c406bb4356d88b6b67a73c847a56ce3f3...v2016.09.01-1)

* Add NTV (JP) logo (#2283)
* Fix notification responsiveness #2274 (#2277)
* Adding Slack notification for snatches and downloads (#2276)
* Add x265 categories to Torrentday provider (#2263)
* Fix add show from imdb popular
* Fix imdb popular page parsing due to change in imdb site (#2257)
* -----END PGP SIGNATURE-----

### v2016.08.25-1

[full changelog](https://github.com/SickRage/SickRage/compare/ae848a6c2915815167b69d9662a785cb9f889781...v2016.08.25-1)

* cfc6d09 (origin/develop, develop) Fixes #1907 (#2256)
* 820c59a Fix #1621 (#2254)
* 554affc Fix Debian/Ubuntu install script (#2242)
* 68f4617 Fix form submit for firefox (#2238)
* 9ae99f7 Fix reverse symlink menu item in settings (#2235)
* 2265336 Fix 'Error: [Errno 1] Operation not permitted:' when using SymLink (#2231)
* -----END PGP SIGNATURE-----

### v2016.08.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/cee2058963fb4be42443d65bdff2976bb3bb4b93...v2016.08.20-1)

* Fix iptorrents
* Remove torrentz
* Fix some page formatting/label
* Fix massEdit for users with srHome prefix
* -----END PGP SIGNATURE-----

### v2016.07.31-1

[full changelog](https://github.com/SickRage/SickRage/compare/a97af68389d2348b1b1740eb918b401e26c571ba...v2016.07.31-1)

* Support reverse symlinking
* Fix `stupid` regex and tests
* Add support for retrying subtitle downloads
* Disable KAT
* More responsive ui changes
* -----END PGP SIGNATURE-----

### v2016.07.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/33c3008471c15742c7264e14ff4a9e243bc1c119...v2016.07.10-1)

* Change "No Show Object found for show with indexerID" log message to warning (#2059)
* fix upstart to use default folder when using installer script (#2053)
* For installer script: if folder not exist, clone repo (#2054)
* ItaSa: fix manage season number (#2038)
* Fixed typo which loaded the cookies setting into api_key variable. (#2048)
* Enable cookies field for all TorrentProviders, if they have the provider.enable_cookies attribute set. (#2034)
* remove trailing comma from list of columns to select when checking for duplicate shows (#2029)
* Use unique seasons when searching (#2027)
* Updates qbittorrent api calls to reflect changes made in qbittorrent with version 3.3.5. Ensure backward compatibility with older versions of qbt. (#1996)
* Fixes #1976 - encoding userid/password before logging in to SMTP server (#1977)
* Fix for torrentday
* -----END PGP SIGNATURE-----

### v2016.06.14-1

[full changelog](https://github.com/SickRage/SickRage/compare/946f6be31a26c661a5e0903c5d66e4ce348ce19d...v2016.06.14-1)

* Feature to metadata for subtitles, add retry for itasa using 'rip suffix'
* Small fixes
* -----END PGP SIGNATURE-----

### v2016.05.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/88637a4da7da930272adeb8c2daee5ba7404b2f4...v2016.05.20-1)

* 0b7e099 Fixes #1802
* dee4d9f Update author typo
* 0ef6d1e Rewrite xthor to use api (#1818)
* 18851b7 Added some lines for translation (#1803)
* 4038fac Fixes #1775
* eaec0c4 Subtitle improvement (#1784)
* 0742462 Fix offset checkboxes in config pages (#1780)
* 02acf84 Responsive ui - round 2 (#1767)
* 9db0392 Small tweakes to the icons/css (#1766)
* e120a76 newpct rss ayer (#1745)
* -----END PGP SIGNATURE-----

### v2016.05.12-1

[full changelog](https://github.com/SickRage/SickRage/compare/61b8a1965bcee524b557a667fa11ffdece31ba72...v2016.05.12-1)

* Fixes jquery for adding scene exceptions, black/whitelist Fixes #1746 Fixes #1747 Fixes #1759
* Fix season pack search in tvchuk and "fix" titles (#1752)
* Fix regexes (#1750)
* Fix show info width (#1755)
* Fix label in deluge, needs to be lower case (#1749)
* Change log to info, no need to be warning (#1742)
* Fixes search in windows systems for danishbits (#1741)
* -----END PGP SIGNATURE-----

### v2016.05.09-2

[full changelog](https://github.com/SickRage/SickRage/compare/14f70d96464ff48adfa35e9df6d8c4d8e6211d3d...v2016.05.09-2)

* Fix put.io client
* Fix icons on the schedule page
* Fix IndexError in home.mako
* Fix incorrect log when a result is not found on KAT

### v2016.05.09-1

[full changelog](https://github.com/SickRage/SickRage/compare/b6fbce6af0236a182241a1048d8991a5c3f88f2e...v2016.05.09-1)

* Fix unable to set label for torrent in qbittorrent
* Update subliminal to 14707b6
* Initial changes moving towards a responsive ui (may be issues to iron out)
* Add some more translations
* Remove postpone if no subs feature, in preparation for a better solution

### v2016.04.28-1

[full changelog](https://github.com/SickRage/SickRage/compare/0771ed9c40318b58b88a5a823488f64defe71fb9...v2016.04.28-1)

* Remove Strike and Bitsoup providers, strike is taken down, bitsoup is pay only
* Add german scene release tag 'netflix', matches web-dl
* Update translations

### v2016.04.27-1

[full changelog](https://github.com/SickRage/SickRage/compare/88883c1ddd4aab833bbf28b3f35e36ffae54be93...v2016.04.27-1)

* Refactor FilterBadReleases to filter_bad_releases, and adjust the logic:
*     **Show specific required/ignored words now totally override global settings if they are set**
* 
*     If show ignored words are not set, global ignored words will be used
*     If show required words are not set, global required will be used
* 
*     If the show has required words, they will be removed from the overall calculated ignored list when evaluating
*     If the show has ignored words, they will be removed from the overall calculated rquired words list when evaluating
* 
*     If a show has required words which are also in the global ignored words they will override the global ignored and the release will be accepted
*     If a show has ignored words which are also in the global required words they will overrid the global required and the release will be discared
* 
*     Release must not contain ANY of the final ignored words list, and at least ONE of the final calculated required words.
* 
*     Added a unit test to make sure this behavior is as expected and remains that way
* 
*     Fixes #1541
*     Fixes #1619
*     Fixes #1623
*     Fixes #1629
* 
* Updated torrentproject to use api magnet (#1632)
* Fix Legendas.tv subtitle provider not showing for some people (stevedore...) Fixes #1626
* Fixed #1623
* Fixed https://github.com/SickRage/sickrage-issues/issues/778
* Fixed #1578
* Fixed #1585
* Removed phxbit, no longer exists (#1605)
* Added put.io & Join logos to the GUI (#1595)
* Added putio client and update search providers templates (#1550)
* Added Join notifier (#1588)
* Updated icon sprite sheet

### v2016.04.17-2

[full changelog](https://github.com/SickRage/SickRage/compare/3d8fffd084b63e5a3cfb538f2619b6ed91e65c90...v2016.04.17-2)

* Update translations
* Move github setup out of sickbeard init to sickrage.common.helper, so a restart isnt required after entering github credentials (#1533)
* Fanart background in displayShow (#1531)
* Change level of all loggers when enabling debug, so a restart isnt required! (#1529)

### v2016.04.17-1

[full changelog](https://github.com/SickRage/SickRage/compare/8e2ceeef340bef7c9e268b218d62b4f12ee6af4e...v2016.04.17-1)

* Fix database upgrade to 43.1
* Update translations
* Add Bulgarian translations

### v2016.04.16-1

[full changelog](https://github.com/SickRage/SickRage/compare/b80c18dbb712a91c38d3617576a2aff67ed17bb0...v2016.04.16-1)

* Update translations
* Added more text for translation (#1504) (#1503) (#1499)
* Update TtN , remove unnecessary fall back and change size to bytes to… (#1508)
* Display banner on DisplayShow page. (#1518)
* Add MBC 1 logo (#1515)
* Clickable icon to open shows page on http://www.fanart.tv (#1512)
* Added some missing buttons for translation (#1506) (#1507) (#1509)

### v2016.04.14-1

[full changelog](https://github.com/SickRage/SickRage/compare/5709abdbe82611c8c941ddc0cda9784e8ef65bcd...v2016.04.14-1)

* Update languages, add a few translation strings

### v2016.04.13-1

[full changelog](https://github.com/SickRage/SickRage/compare/707f8dc8dd5000bc08af66db2b91697e4bbcb69b...v2016.04.13-1)

* Bump DB version to 43 to avoid issues updating when DB was previously used with SRTV
* Specify encoding for config file
* Update pushbullet info string in webui
* Fix typo in rename-selected url
* Improve handling of windows file operations, fix issue with getting free space
* Temporarily Disabled pymediainfo due to segfaults

### v2016.04.12-1

[full changelog](https://github.com/SickRage/SickRage/compare/31b5be571b3cc4d7e11dc543ea5b3c071bf55b41...v2016.04.12-1)

* Merge pull request #1469 from SickRage/neoatomic-develop
* Update translations, add en_GB translation
* Fix a few syntax errors in mako embedded python Fix manageSearches page syntax error for translatable string and clean it up some
* Some additions for the translations.
* Fixes #1463
* Update subliminal to 2.0.rc1 (b48c0c9) VANILLA! (#1459)
* Remove itasa subtitle provider and add shooter.cn subtitle provider
* Try to fix #1446 #1445 (#1458)

### v2016.04.11-2

[full changelog](https://github.com/SickRage/SickRage/compare/3472b28fe1509a95479cec52d138be1e08dc3307...v2016.04.11-2)

* Add ability to select your language for the web ui in config/general on the interface tab

### v2016.04.11-1

[full changelog](https://github.com/SickRage/SickRage/compare/f36e21bb5a96d946aa773a4cba875ed86572cd7c...v2016.04.11-1)

* Fix issue tracker link in readme
* Combine show req/ign words with global ign/req words when checking release names so it doesnt require a word from BOTH ign lists or BOTH req lists
* Fix issue with manual pp and nzbtomedia
* Fix a few str formatting errors and add a few localizable strings

### v2016.04.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/8e2b26857c85a4bada2b6cc068279c081c7c8311...v2016.04.10-1)

* Update translation strings
* Fix typos related to translations
* Fix selecting subtitle languages
* -----END PGP SIGNATURE-----

### v2016.04.09-1

[full changelog](https://github.com/SickRage/SickRage/compare/5120ba8d8fc3ee1c7a3fbfb1efddb3c63f2e1274...v2016.04.09-1)

* Fix issue matching subtitles from the wrong show to downloads in the PP folder
* Add mediainfo integration for getting video screen size, to help guessing quality from unknown quality files. Can be used for more things in the future
* Translate the rest of the ui, still small tweaks here and there to-do
* Update with latest translations, you guys are on fire
* -----END PGP SIGNATURE-----

### v2016.04.08-1

[full changelog](https://github.com/SickRage/SickRage/compare/6e3ebea4d634d3e5894ae9b85eabffe4284be0ca...v2016.04.08-1)

* Add ability to fully translate the web interface
*   Use crowdin.com for managing translations
* 
* Fix issue listing files associated with an episode or video file.
*   This fixes subtitles and nfo not being moved during post processing,
*   and not being renamed when renaming episodes
* 
*   Also fixes PP trying to double process a video, because the video itself
*   was also returned as an "associated file"
* 
* Fix issue where show refresh used an insane amount of memory/cpu
*   and would hang on broken videos and avi files when quality was
*   not detected from the name.
* 
* Fix wrong show/episode air times
* Fix issue sending app image to boxcar2
* 
* Small tweak to make web interface look just a little better on mobile, more to come.
* 
* Fixed #1373 (#1378)
* Add some weight to episode_numbers, to prefer matching them over absolute numbers in cases where the title has numbers or the word "Episode \d"
* Fall back to SDDVD when it matches SD DVD regex in filename for default named eps coming from sickbeard.
* Backport glob.escape from python 3.4
* Ditch hachoir for purpose of parsing screen height of files when guessing quality, rolled my own avi WxH implementation and use enzyme for mkv
* Add test to make sure providers return results in the proper format and valid values
* Fix TorrentProject requesting trackers with no hash and cure ddos by only requesting when less than 3 seeds, almost dead torrents
* Partial Dutch Translation for Sickrage
* Make sure show specific req/ignored words exist before trying to split them
* Cassettes and tests for public providers' search parsing.
* Must explicitly cast basestrings to int before using int based format specifiers
* Fix AM/PM of show air times
* Add Ilovetorrents provider
* Fix WEB detection
* Disable verify for plex media server, since it is signed with the plex direct wildcard cert (even locally)
* Adjust metadata file log messages
* Fix up tvshow.nfo parsing a bit so it doesnt give warnings when id/tvdbid is an empty string
* -----END PGP SIGNATURE-----

### v2016.04.01-1

[full changelog](https://github.com/SickRage/SickRage/compare/f59e46744829adf67a73a7dc9442eda26c40301d...v2016.04.01-1)

* Fixes #1309, #1304, #1285
* Fix "Unable to determine free space"
* Fix issue where importing existing files that parsed to unknown quality would not change episode status to downloaded
* Fix issue causing incorrect airdates
* Fix issue with timezones causing Synology DSM6 to fail to start
* Fix bug where qualityFromFileMeta was getting double and triple called

### v2016.03.31-1

[full changelog](https://github.com/SickRage/SickRage/compare/9a4b1fd2cf04451e74cd8ed51c6210545a7d7fd3...v2016.03.31-1)

* Highlights:
*     Allow sending NZB's to DSM on Synology
*     Ignored/Required words for specific shows override global defaults now
*     Add channels support for pushbullet
*     Hella fixes? xD
* 
* Fix port number in settings gui url note
* Use a set().difference for handling ignored/required words If a word is in the global ignored words and in the show's required words, it is required If a word is in the global required but in the show's ignored, it is ignored
* DSM: Make sure to use nzb client settings when sending nzb, and torrent settings when sending torrents
* Add docstrings
* Add ability to use Synology DSM for nzb also
* Allow trakt checker to continue when imdbid is not known for one show Fixes #1287
* release group sort is now case insensitive
* Fix tuple index out of range
* Make "Available Groups" sort by alphabetical order
* Fix typo from unicode_literals regexing...
* Disable OneRun wrapper for PP, we need a better solution Fixes #1282 https://github.com/SickRage/sickrage-issues/issues/1389
* ...
* Handle when hash or size are missing
* Fix error with multiple search results per provider Thanks @p0psicles
* https://github.com/SickRage/sickrage-issues/issues/1390
* Add debian/ubuntu install script contributed by @DirtyCajunRice
* Make sure df returns 1k blocks without the K suffix
* These arent coding errors, whoever made them logger.ERROR should be swatted Fixes #1263
* Make disk_usage return int, and convert it from K to B Assure df returns in KB (default on most systems, but lets be sure) Fixes #1269
* Remove helpers._getTempDir as it is unused Use platform.system instead of os.name in helpers
* Add functions to check for Pushbullet channels

### v2016.03.28-2

[full changelog](https://github.com/SickRage/SickRage/compare/1847f03608e96cf80b9999233811ff58021ddb3e...v2016.03.28-2)

* Unicode literals for TorrentDay Try and parse size from a dict by default in GenericTorrentProvider
* Split out disk_usage logic so that verify_freespace and getDiskSpaceUsage use the same logic Replaces #1262 Fixes #1259
* Update french fansub
* Added Subtile Provider Cache
* Call df in a subprocess, since OSX has a bug with volumes > 4TB when using statvfs. This will work in all unix-like environments Fixes #1259
* Remove nzbToMedia from source control. It auto updates and breaks git pull
* Use cookie auth for DSM Show error messages for error codes returned from DSM according to DSM docs Check DSM version, and fix the download location if it is absolute on DSM6
* Fix transmission test connection Replaces #1247
* Remove alt.binaries.teevee from binsearch provider (no longer exists) Fixes #1238
* Change code back to use original bencode Fix some logs Fixes wrong torrent hash calculation (labels sometimes not working in utorrent) Fixes #1235 #1203 https://github.com/SickRage/sickrage-issues/issues/1375
* Comment lines that cause most errors with bdecode
* Switch back to official libtorrent bencoder
* Update snyk Use .on('click'... instead of .click(... syntax in js Set a default value for downCurQuality in retryEpisode Use the callback in $.post in js to make sure the reload is after the post finishes, otherwise the reload is before eg. the episode status has changed
* Fix indice error when no results in an omgwtfnzbs search Fixes https://github.com/SickRage/sickrage-issues/issues/1380 Fixes #1225
* Dont warn saying incorrect passkey for shazbat when it has no results Fixes https://github.com/SickRage/sickrage-issues/issues/283
* showDir is utf-8 when addExisting shows Fixes #1229
* Fix Seeders and Leechers on TtN
* Add a few more non release groups
* Fix brassetv and add others
* Fix web_root prepend for redirects.
* Use tzlocal and pytz for everything except parsing date strings from the name parser
* Add tzlocal and pytz libs

### v2016.03.28-1

[full changelog](https://github.com/SickRage/SickRage/compare/c34cbbdbca3d999372b34f5b1c61f858ce7cb8d6...v2016.03.28-1)

* Use cookie auth for DSM Show error messages for error codes returned from DSM according to DSM docs Check DSM version, and fix the download location if it is absolute on DSM6
* Fix transmission test connection Replaces #1247
* Remove alt.binaries.teevee from binsearch provider (no longer exists) Fixes #1238
* Change code back to use original bencode Fix some logs Fixes wrong torrent hash calculation (labels sometimes not working in utorrent) Fixes #1235 #1203 https://github.com/SickRage/sickrage-issues/issues/1375
* Comment lines that cause most errors with bdecode
* Switch back to official libtorrent bencoder
* Update snyk Use .on('click'... instead of .click(... syntax in js Set a default value for downCurQuality in retryEpisode Use the callback in $.post in js to make sure the reload is after the post finishes, otherwise the reload is before eg. the episode status has changed
* Fix indice error when no results in an omgwtfnzbs search Fixes https://github.com/SickRage/sickrage-issues/issues/1380 Fixes #1225
* Dont warn saying incorrect passkey for shazbat when it has no results Fixes https://github.com/SickRage/sickrage-issues/issues/283
* showDir is utf-8 when addExisting shows Fixes #1229
* Update btn.py
* Fix web_root prepend for redirects.

### v2016.03.23-1

[full changelog](https://github.com/SickRage/SickRage/compare/5b4d865cb5b5a908cd474c3cb5752b848592943d...v2016.03.23-1)

* Quantified code, please dont force format tokens to strings, lol Fixes https://github.com/SickRage/sickrage-issues/issues/1370
* Show how many characters the url has exceeded the limit in the alert when operating on too many shows https://github.com/SickRage/sickrage-issues/issues/1203#issuecomment-200097373
* Pass true to loaction.reload, to ensure it doesnt reload from cache Fixes #1202
* Clean up generic client and utorrent client use unicode_literals and str.format()

### v2016.03.22-1

[full changelog](https://github.com/SickRage/SickRage/compare/e7ec19c820a246e9a07701cbfcad7b64c323d40b...v2016.03.22-1)

* Use unicode_literals in show_queue Use str.format() Lint, and fix some funkyness Normalize text between ui notifications and logger
* Send verify=False for sab requests Fixes https://github.com/SickRage/sickrage-issues/issues/1201
* add number index to string format replacements, normalize the search string log line
* match bs4 search results by direct parameter rather than attrs=
* Use bs4 objects as a method instead of explicitly calling findAll/find_all for shorter code
* Remove unnecessary cookielib
* Unify requests exception handling
* Unicode literals for common, helpers, naming, and tv Fixes https://github.com/SickRage/sickrage-issues/issues/1340
* Disable SSL verify in t411 since their cert does not match Fixes https://github.com/SickRage/sickrage-issues/issues/1341
* Only encode potential extra script params if there is actually a script to run Add some try/except. Might need one to catch the execv error Fixes https://github.com/SickRage/sickrage-issues/issues/1237
* Modified itasa provvider for better scores

### v2016.03.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/bc5e61a8f96a8abae80ae78fbf261ff3023a664d...v2016.03.20-1)

* Change wiki/issues links to main repo
* Clean up gui imports, and some other finagery
* Updating subliminal to f40e79a78b7c8c92b83399d4d8778ec54ee8b7d2 plus legendastv and itasa providers
* Avoid `None` as a redundant second argument to `dict.get()` Avoid using `not ... is` instead of `is not`
* Use set comprehension
* Avoid mutable defaults for method parameters
* Avoid using `len(x)` to check if x is empty
* Remove funkyness with torrentday, untested
* Hacky fix for 11.22.63, the warning was never really an error anyways, just a warning on one of the regex iterations that it didnt match to Fixes https://github.com/SickRage/sickrage-issues/issues/1221
* Only show commit hash for ERROR log lines
* Update nzbtomedia reference to V10.14
* Update requests to 2.9.1
* Update certifi to 38502797954603558ebf5f2c93f3645279e18158
* Generate API key more randomly and securely
* Remove unused md5_for_file code and tests Fix mutable parameter default values Remove has_key tests since we no longer override has_key in qualities
* update node dev dependancies change to node 5.6.0 for travis
* Migrated `%` string formating
* Explicitely numbered replacement fields
* Fix string format in sickbeard.helpers
* Allow sep=None for convert_size
* Add .checkignore
* Check api limits and errors with hd4free
* Change NMA URL
* Show commit hash and branch even if we dont know the tag number (source installs especially)
* Fix download link on transmithenet
* Try again for 1086 Fixes SickRage/sickrage-issues#1086
* Cleanup sickbeard.__init__ to remove some global keywords and write out the config nicer
* If adding existing shows, and you have a show in your list with a missing show dir, re-use the existing show object in the db and update it's info rather than skipping it
* Add limit for massupdate url generated by js
* Limit url length generated by addExisting with an ugly js alert =P Temporary solution
* Fixes https://github.com/SickRage/sickrage-issues/issues/1198
* Switch bencode implementation, using https://pypi.python.org/pypi/python-bencode
* update dateutil to d05b837
* Remove some spamminous logging from name_cache, db upgrade checks, and setter sets location (tv.py) Cleanup db.py
* Add missing ITASA globals in sickbeard.__init__
* Some changes to nw timezones, hopefully will make it more reliable.
* Encode file path and episode location to SYS_ENCODING (usually utf-8) before calling popen Fixes https://github.com/SickRage/sickrage-issues/issues/1086
* Add .pullapprove.yml
* Added ItaSA subtitle provider

### v2016.03.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/99a6af8382a36339a55431308fad5ca991ad5d1a...v2016.03.10-1)

* Don't save filter_Rows state through page refreshes Fixes https://github.com/SickRage/sickrage-issues/issues/1177
* No need to specify timezone in datetime.now() in the footer
* Newznab provider handles show id internally now, and rid is no longer used, so this is stray code that does nothing
* Use a better module property name for hachoir's log
* log ERROR=>DEBUG when show is already being updated and attempted to be done again Fixes https://github.com/SickRage/sickrage-issues/issues/1165
* Fix commit hash update notifications when using source install. Fixes https://github.com/SickRage/sickrage-issues/issues/1118
* Fix auth header for pushbullet https://github.com/SickRage/sickrage-issues/issues/1118
* Add custom notification email subject
* Fix WEB-DL and WEB-Rip detections * Optimize regex * Add WEB detection * Add DLMux detection
* Use sickrage.github.io for url to the icon, instead of rawgit
* Add icon and app name to boxcar notification
* Boxcar2, use requests, unicode literals, str.format
* Oops, need to send the session to getURL
* Rework pushbullet, might need some message improvements
* Rework pushalot notifier Fixes https://github.com/SickRage/sickrage-issues/issues/1034
* update dateutil to c2c9700
* Fix NoneType for CUR_COMMIT_HASH error when github is not available
* Updated "Sync File Extension" list for qBittorrent
* Fix typo in TTN Fixes https://github.com/SickRage/sickrage-issues/issues/1112
* Use request hook for download_file in providers, until we can be sure sessions are working correctly
* Don't require TLD with validators for providers that may be local (bitcannon, torznab, newznab) Fixes https://github.com/SickRage/sickrage-issues/issues/1117
* Rework how session and request parameters are handled Prevents residual params in the session Prevents session getting stuck in stream mode Allows ssl_verify to be disabled without a restart Allows passing verify as a kwarg to disable it on a per request basis Allows passing headers without contaminating the session Removes old code from glype that was poisoning the session/headers/proxies
* Add setup.py and tox
* Add better test coverage to GenericProvider
* Fixes SickRage/sickrage-issues#1115
* Clean up scheduler thread formatting in `sickbeard.__init__` Set show updater to cycle time 1hr again, see if that fixes it not running Delay start of most threads at least a minute or two after startup Fix bug adding cycle time to last_run
* Make show filter on poster view case insensitive match.
* Add anime category for bluetiger provider
* Add code to send email on remote login and sickrage updates Use unicode literals Use str.format
* Fix network timezone reporting
* Refresh show from dir even when it hasnt been updated on tvdb, but do not rebuild metadata (force=False) Fixes https://github.com/SickRage/sickrage-issues/issues/1089
* Don't error when show was already removed from trakt or never was on trakt. Fixes https://github.com/SickRage/sickrage-issues/issues/1038
* Fix errant nzbget string after converting strings
* Fix searching tvdb to add shows when result contains a result that has no firstaired set. Clean up sickbeard.classes
* pre-sort qualities for quality list Fixes https://github.com/SickRage/sickrage-issues/issues/1087
* Hotfix dateutil error for timezone names on Windows
* Fix error where sometimes client did not log into the provider before downloading a torrent or nzb Fix error where sab was calling an undefined method Switch sab code over to completelt requests Pass returns= in all calls to get_url Remove json= and need_bytes= params from getURL and get_url Cleaner __str__ for search result class Remove some dupe logging

### v2016.03.05-1

[full changelog](https://github.com/SickRage/SickRage/compare/ace5e56d632654b03f00d533c2489440e792cba9...v2016.03.05-1)

* Use content when downloading nzbs
* Updated the provider icons & added viceland network logo.
* Fix "'NoneType' object has no attribute 'indexerid'" when deleting a show when new shows are being added.
* https://github.com/SickRage/SickRage/commit/bbd16184ae6f47d5d260cb08e4dde18cd7c1cd4d#commitcomment-16505285
* Fix gingadaddy Fix nzb.su and other providers who don't support tvdbid Use dict for result lists in all torrent providers No need to override get_ratio Fix more get_url calls to use the request hook Fix issue with blank download url when using transmission 2.90+ Fix dupe quality from numDict Sort quality lists Much more
* Force mimetypes for commonly misconfigured types, ie: when a user has dreamweaver installed Fixes https://github.com/SickRage/sickrage-issues/issues/1078
* Fix login issue with tvchaosUK, fixes need to double login Fixes https://github.com/SickRage/sickrage-issues/issues/1077
* Update dateutil to 2.5.0 with updated zoneinfo
* Fix tvchaosuk, there is one persistent cookie for CF, then totals 4 cookies when authed Fix tntvillage login, has 3 cookies when logged in. RSS search still disabled in this provider Fixes https://github.com/SickRage/sickrage-issues/issues/1072
* Update T411 domain name
* Change UA for statistical reasons
* Every request in SR was re-initializing the cache, so no request was honoring cachecontrol (like, ever) This is probably why caching to disk was causing breakage, and also why we are spamming xem.
* rewrite, got rid of unnecessary methods and based the provider on abnormal.py
* Made the webbrowser dependency optional
* use str.format instead of %s for search string
* Fix docstrings, quotes and some other coding style issues
* Norbits provider
* Use _ for french adn icon name.
* Move logging commit hash
* Prevent logging "No results found" message
* Fix subtitles indent
* Update subliminal to latest version (c3c0c45)
* Add mako indenting
* 50 Threads? Really? This fix halves VIRT alloc, to halve it again add export MALLOC_ARENA_MAX=2 (or 1) to your runscript on linux)
* Missed a few replace-map typos
* Disable show update on start until it can be improved
* Gui had wrong replacement chars for scene numbers in renamer
* fix: Danishbits provider now works again
* Fixes https://github.com/SickRage/sickrage-issues/issues/1046
* Use a decorator to prevent processing a dir more than once at a time, regardless of caller Fixes https://github.com/SickRage/sickrage-issues/issues/1028
* Fixes https://github.com/SickRage/sickrage-issues/issues/1042 Fixes touchFile to use ek and check file exists
* Disable auto pp when postpone if no subs
* Fixes url encoded censored items in logs not being censored.
* Plex: Always return True when getting auth token if username/password aren't configured
* Fix issue where last_update_indexer was using date instead of datetime, use time based updates xml from tvdb instead of day.xml. Even though it is deprecated it works BETTER
* even more fixes
* more fixes
* Quck subtitles improvements
* Check SUBTITLES_MULTI and make subs exceptions as dict
* Delete unwanted subtitles
* Check if sub is enabled before postpone
* update bower_concat
* Revert "Fix SickRage/sickrage-issues/issues/813"
* Show refresh/update should have high priority
* Force "Subtitles Multi-Language" if more than one wanted subtitle language
* Subtitle language exceptions as Dict
* Add PR/Issue templates, move contributing.md to .github
* Add OCS network logo
* Add option to keep only wanted subs
* Delete unwanted subtitles if we don't want them
* Check if show has subtitle enable before postpone PP
* Add "ignore subs" setting in manual PP
* This seems ok
* Remove subliminal patch, grunt like what
* Revert "Updated npm deps"
* Updated npm deps Remove patches (subliminal is not locally patched anymore) Did best Tim Allen impersonation
* Fix TPB when using an invalid proxy
* NewPCT:   * Unicode literals   * Fix string quotes   * Fix get_url override   * Conformity and cleanup
* Warn about database owner/permissions
* NewPCT:   * Unicode literals   * Fix string quotes   * Fix get_url override   * Conformity and cleanup
* Make the show updater run on startup Fix it so that it doesnt keep updating the same shows over and over Fix cycleTime for show updater for status page Clean up logging in tv.py when setting the next episode and updating show
* Disable subtitles code db check
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Catch shutil errors and proper display as error/warning
* Create gists as secret instead of public
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix https://github.com/SickRage/sickrage-issues/issues/235#issuecomment-185068695
* Add "(musicbolt.com)" to removewordslist
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix https://github.com/SickRage/sickrage-issues/issues/235#issuecomment-185068695
* Pass params through getRSSFeeds to get_url instead of urlencode Update string quotes, u prefix removal and unicode literals for bunsearch, nyaa, omg, rsstorrents, shazbat, womble Clean up and improve those providers
* Add option to ini to allow PMS update without token or user/pass when you dont require authentication config.ini only option for now
* Use provider's get_url for getting rss feeds instead of urllib/httplib2 Fixes bozo, and removes old code Normalizes logging
* Update contributing.md
* Dont run FINDSUBTITLES thread right on SR start
* Allow passing arguments future= and past= for range of weeks from today to add to the webcal http://localhost:8081/calendar?past=2&future=3 both default to 52
* Handle float log sizes Increase default log size to 10MB to reduce rolling over Fix SickRage/sickrage-issues/issues/892 Replaces #1027
* Fix typo preventing confirm modal not showing before submitting errors
* RARBG:   * Show api error messages   * Show log when no torrents differentiated from when no data returned   * Move sleep to prevent hitting request limit and use CPU_PRESETS
* Fix btdigg api url
* It is returns= not response= now
* RARBG:   * Use unicode literals, remove u prefixes, use " over ' for strings   * Use .format over token string formatting   * Pass returns="json"   * Remove excess logging, pop elements as they are used from the json
* BTDigg:   * Use unicode_literals, remove u prefixes, use " instead of ' for strings   * Use .format instead of token string formatting throughout   * Pass params to get_url, and specify json response type   * Remove duplicitous logging   * General BTDigg cleanup   * Add ! to config_providers since btdigg api is currently not working.
* Revert "fixed, Newznab cats that are disabled, shouldn't be shown in configure options tab."
* Adjust requests hook just a bit
* Use a requests hook for get_url in providers, show post data for post requests
* KAT:   * Use unicode_literals, remove u prefix, use " for strings   * Use validators for custom_url   * Use urljoin throughout   * BS4Parser for better cleanup   * Fix issue with magnets
* Fix seeders/leechers log lines
* Providers:   * Only include freeleech in provider __init__ if provider supports it (same for minseed, minleech, etc)   * No need to encode search_string, it is encoded in _get_*_search_strings
* TorrentBytes:   * Use unicode_literals, remote u prefixes, use " over ' for strings   * Use urljoin throughout   * Pass search params to requests instead of building the url   * Pass response="text" to get_url   * Parse table headers and use for cell indexing
* TPB doesnt have freeleech
* ABNormal code doesnt support freeleech param
* Bitcannon:   * Use unicode_literals and remove u prefixes   * Use " over ' for strings   * Use validators for custom_url
* Add missed dependancy for validator: decorator.py
* No need to check if torrent_table is None, it is handled in the next line to allow the log
* Update torrentleech   * Use unicode_literals and remove u prefixes   * Use " over ' for strings   * Use .format over token formatting   * Use urljoin over string concat for urls   * Pass params to get_url instead of urlencoding
* Update search string log line for all providers
* Update BinSearch   * Use unicode_literals and remove u prefix   * Use " over ' for strings   * Use .format over % token string formatting   * Use urljoin instead of concat for urls   * Import urljoin, urlencode from requests.compat
* AbNormal Updates   * Pass response="text" for login and search   * No need to use named format replacements unless you are using the same replacement more than once   * Switch back to " over ' for strings
* update "Search Mode:" log line in all providers to use .format
* TPB Updated * Use unicode_literals and remove u prefix * Use " over ' for strings * Use .format over string tokens * Remove extra search url log and pass response='text' to get_url * use validators to validate custom_url
* Add lib/validators to be used with custom_urls and email and ip validation of user input and other places
* Alpharatio strings updates * Remove u prefix from strings * Normalize strings to use " throughout
* Alpharatio updates * Use urljoin over string concat * Use unicode_literals * Remove search url log and pass response param to get_url
* Removed unused urlencode import
* Use params instead of encoding the params and joining them Remove duplicate logging
* Use urljoin instead of concat
* Use unicode literals
* Standardize string formatting
* Standardize strings to use single-quotes
* Import urlencode from requests.compat instead
* Clean up airdate modify timestamp handling and make sure exceptions are caught. Fixes https://github.com/SickRage/sickrage-issues/issues/914
* Make sure etree always adds xml declaration for mede8er and specify encoding explicitly Trying to fix https://github.com/SickRage/sickrage-issues/issues/862
* Import urlencode from requests.compat instead of urllib
* Allow file globs in "Sync File Extensions" setting to postpone postprocessing
* Remove old_scene_quality Remove quality assertion Refactor sceneQuality => scene_quality Fix anime bluray detection
* Fix getURL calls to use `returns` argument
* Append show name to show search strings regardless of searched season
* Append show name to show search strings regardless of searched season
* Fix logging when result is None fixes SickRage/sickrage-issues/issues/902
* Fix getURL log entry should be debug
* Fix apikey shown in log when = is urlencoded as %3D
* Add URL logging to GenericProvider.get_url
* Add raw response object as a getURL return type Add pending deprecation warnings for getURL arguments json, need_bytes Add pending deprecation warning for getURL returning text
* Don't limit allowed extensions to 3 chars
* Reduce subtitle score to match only Series, Season, Episode and Year
* fixed, Newznab cats that are disabled, shouldn't be shown in configure options tab.
* Fail gracefully and continue PP when setting file timestamp to airdate chokes Fixes https://github.com/SickRage/sickrage-issues/issues/269
* Allow changing categories for defautl newznab providers. Caveat: They are on the "Custom Newznab Providers" tab where you change the categories, until the js can be fixed
* Need to use generic exceptions for all seasons, not just season 1
* Need to use generic exceptions for all seasons, not just season 1
* Filter scene exceptions a bit different
* Fromstring is already the tree root -.-
* Explicitly encode in the exception raises for name parser Partial issue of https://github.com/SickRage/sickrage-issues/issues/12
* Must use etree.fromstring instead of etree.parse since its a string instead of a stream now in PMS
* Must check if generic exceptions are in the exceptionList already before appending them. Fixes https://github.com/SickRage/sickrage-issues/issues/852
* Add explanation about subliminal score math
* Don't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Fix SickRage/sickrage-issues/issues/824

### v2016.02.22-1

[full changelog](https://github.com/SickRage/SickRage/compare/26ddbf4b882c293c187fe3ec88dd6e826eeed7a7...v2016.02.22-1)

* Use a decorator to prevent processing a dir more than once at a time, regardless of caller Fixes https://github.com/SickRage/sickrage-issues/issues/1028
* Fixes https://github.com/SickRage/sickrage-issues/issues/1042 Fixes touchFile to use ek and check file exists
* Disable auto pp when postpone if no subs
* Fixes url encoded censored items in logs not being censored.
* Plex: Always return True when getting auth token if username/password aren't configured
* Fix issue where last_update_indexer was using date instead of datetime, use time based updates xml from tvdb instead of day.xml. Even though it is deprecated it works BETTER
* even more fixes
* more fixes
* Quck subtitles improvements
* Check SUBTITLES_MULTI and make subs exceptions as dict
* Delete unwanted subtitles
* Check if sub is enabled before postpone
* Show refresh/update should have high priority
* Force "Subtitles Multi-Language" if more than one wanted subtitle language
* Subtitle language exceptions as Dict
* Add PR/Issue templates, move contributing.md to .github
* Add option to keep only wanted subs
* Delete unwanted subtitles if we don't want them
* Check if show has subtitle enable before postpone PP
* Add "ignore subs" setting in manual PP
* Remove subliminal patch, grunt like what
* Updated npm deps Remove patches (subliminal is not locally patched anymore)
* Fix TPB when using an invalid proxy
* Warn about database owner/permissions
* NewPCT:   * Unicode literals   * Fix string quotes   * Fix get_url override   * Conformity and cleanup
* Make the show updater run on startup Fix it so that it doesnt keep updating the same shows over and over Fix cycleTime for show updater for status page Clean up logging in tv.py when setting the next episode and updating show
* Disable subtitles code db check
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Catch shutil errors and proper display as error/warning
* Create gists as secret instead of public
* Add "(musicbolt.com)" to removewordslist
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix https://github.com/SickRage/sickrage-issues/issues/235#issuecomment-185068695
* Pass params through getRSSFeeds to get_url instead of urlencode Update string quotes, u prefix removal and unicode literals for bunsearch, nyaa, omg, rsstorrents, shazbat, womble Clean up and improve those providers

### v2016.02.16-1

[full changelog](https://github.com/SickRage/SickRage/compare/820b900a6dc72ed4958a90ac027d8f92d785810b...v2016.02.16-1)

* Add option to ini to allow PMS update without token or user/pass when you dont require authentication config.ini only option for now
* Use provider's get_url for getting rss feeds instead of urllib/httplib2 Fixes bozo, and removes old code Normalizes logging
* Update contributing.md
* Dont run FINDSUBTITLES thread right on SR start
* Allow passing arguments future= and past= for range of weeks from today to add to the webcal http://localhost:8081/calendar?past=2&future=3 both default to 52
* Handle float log sizes Increase default log size to 10MB to reduce rolling over Fix SickRage/sickrage-issues/issues/892 Replaces #1027
* Fix typo preventing confirm modal not showing before submitting errors
* RARBG:   * Show api error messages   * Show log when no torrents differentiated from when no data returned   * Move sleep to prevent hitting request limit and use CPU_PRESETS
* RARBG:   * Use unicode literals, remove u prefixes, use " over ' for strings   * Use .format over token string formatting   * Pass returns="json"   * Remove excess logging, pop elements as they are used from the json
* BTDigg:   * Use unicode_literals, remove u prefixes, use " instead of ' for strings   * Use .format instead of token string formatting throughout   * Pass params to get_url, and specify json response type   * Remove duplicitous logging   * General BTDigg cleanup   * Add ! to config_providers since btdigg api is currently not working.
* TorrentBytes:   * Use unicode_literals, remote u prefixes, use " over ' for strings   * Use urljoin throughout   * Pass search params to requests instead of building the url   * Pass response="text" to get_url   * Parse table headers and use for cell indexing
* Bitcannon:   * Use unicode_literals and remove u prefixes   * Use " over ' for strings   * Use validators for custom_url
* TorrentLeech   * Use unicode_literals and remove u prefixes   * Use " over ' for strings   * Use .format over token formatting   * Use urljoin over string concat for urls   * Pass params to get_url instead of urlencoding
* KAT:   * Use unicode_literals, remove u prefix, use " for strings   * Use validators for custom_url   * Use urljoin throughout   * BS4Parser for better cleanup   * Fix issue with magnets
* AbNormal Updates   * Pass response="text" for login and search   * No need to use named format replacements unless you are using the same replacement more than once   * Switch back to " over ' for strings
* Alpharatio updates * Use urljoin over string concat * Use unicode_literals * Remove search url log and pass response param to get_url
* TPB: * Use unicode_literals and remove u prefix * Use " over ' for strings * Use .format over string tokens * Remove extra search url log and pass response='text' to get_url * use validators to validate custom_url
* BinSearch:   * Use unicode_literals and remove u prefix   * Use " over ' for strings   * Use .format over % token string formatting   * Use urljoin instead of concat for urls   * Import urljoin, urlencode from requests.compat
* Use a requests hook for get_url in providers, show post data for post requests
* Fix seeders/leechers log lines
* Providers:   * Only include freeleech in provider __init__ if provider supports it (same for minseed, minleech, etc)   * No need to encode search_string, it is encoded in _get_*_search_strings
* Add URL logging to GenericProvider.get_url
* Add raw response object as a getURL return type Add pending deprecation warnings for getURL arguments json, need_bytes Add pending deprecation warning for getURL returning text
* Update search string and mode log line for all providers
* Add lib/validators to be used with custom_urls and email and ip validation of user input and other places
* Import urlencode from requests.compat instead
* Clean up airdate modify timestamp handling and make sure exceptions are caught. Fixes https://github.com/SickRage/sickrage-issues/issues/914
* Make sure etree always adds xml declaration for mede8er and specify encoding explicitly Trying to fix https://github.com/SickRage/sickrage-issues/issues/862
* Allow file globs in "Sync File Extensions" setting to postpone postprocessing
* Remove old_scene_quality Remove quality assertion Refactor sceneQuality => scene_quality Fix anime bluray detection
* Append show name to show search strings regardless of searched season
* Fix logging when result is None fixes SickRage/sickrage-issues/issues/902
* Fix apikey shown in log when = is urlencoded as %3D
* Don't limit allowed extensions to 3 chars in post processor
* Reduce subtitle score to match only Series, Season, Episode and Year
* Fail gracefully and continue PP when setting file timestamp to airdate chokes Fixes https://github.com/SickRage/sickrage-issues/issues/269
* Allow changing categories for default newznab providers. Caveat: They are on the "Custom Newznab Providers" tab where you change the categories, until the js can be fixed
* Use generic exceptions for all seasons, not just season 1

### v2016.02.11-1

[full changelog](https://github.com/SickRage/SickRage/compare/4f3207fa6ab2db95f11a86bc7305ccef45523ecb...v2016.02.11-1)

* Explicitly encode in the exception raises for name parser Partial issue of https://github.com/SickRage/sickrage-issues/issues/12
* Must check if generic exceptions are in the exceptionList already before appending them. Fixes https://github.com/SickRage/sickrage-issues/issues/852
* Add explanation about subliminal score math
* Don't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Fix SickRage/sickrage-issues/issues/824
* Added network logo's  for RMC decouverte and UP TV.
* Use .eu for podnapisi
* Fix cyclic dependancy in notifiers so we can use helpers, clean up some crazy
* Updated subliminal develop (864ecf4) and legendastv provider, adjusted scores for subtitles
* Rewrite a good bit of plex notifier to use requests and maintain headers
* Fix download url generation in alpharatio, danishbits, gft, speed.cd Fixes https://github.com/SickRage/sickrage-issues/issues/818
* Fix anime bluray qualities

### v2016.02.10-1

[full changelog](https://github.com/SickRage/SickRage/compare/7a94dd094c2861d54f500c39af5fb2cdb856dfdc...v2016.02.10-1)

* Use json scene exceptions
* Only get scene exceptions matching season we are searching for
* Set "Authentication Failed" as warning
* Fixes issue of MTV not downloading
* Add an API method to clear the logs
* Remove need for ek() in subtitles
* Fixe size on transmithenet

### v2016.02.09-2

[full changelog](https://github.com/SickRage/SickRage/compare/c285305affd7385dbd228f95ac1dd5f0f50bf1d1...v2016.02.09-2)

* Use xem absolute numbers for tvdb mapping if tvdb doesnt provide them, fixes american dad if you disable scene numbering
* Dont pass q on rss update, use sickbeard.USENET_RETENTION directly regardless of mode
* Set search string for subsequent scene exceptions after tvdbid has been popped
* Fix provider log message by decoding to utf-8 instead
* Fix daily search in ABNormal.ws Fixes https://github.com/SickRage/sickrage-issues/issues/768

### v2016.02.08-1

[full changelog](https://github.com/SickRage/SickRage/compare/cdf22bfe1cf70b90c32932a6b9326b6d3b8f7e63...v2016.02.08-1)

* Fix decode by using utf-8 instead Fix unnecessary decode on urlencoded string
* Make sickbeard.gh work even when github login settings are incorrect so that the updater still works Lint sickbeard.__init__
* Revert "Add 5020 (foreign) to default newznab providers (and some missing nzb…"
* Add 5020 (foreign) to default newznab providers (and some missing nzbs.org cats)
* Fix Unicode decoding errors in newznab logging and ex
* Display exception text from NameParser in validateDir
* Fix for nzb indexers who dont support tvdbid or happen to have missed a tvdbid mapping for some shows/episodes. Fixes https://github.com/SickRage/sickrage-issues/issues/667 Fixes https://github.com/SickRage/sickrage-issues/issues/782
* Fix "No processable items found in folder" by building name cache on startup... /slap miigotu and his miibugs
* Change config mako for nzb also
* Swap settings order "Alternate search mode as fallback is fine" and "Season search mode"
* Update nzbToMedia to V10.13 thanks to @clinton-hall
* Standardize providers
* Add log message to warn user and/or help debug possible issues
* Dont unpack again if files were previously unpacked when
* Show log message when not able to search provider
* Fix issue when release is RARred
* Use div or span when using css to apply an image, not an img tag
* Change width of infoTable to 100% in config.mako
* Revert "Fetch only current branch. Not all branches"
* Make sure - is at the end of character groups in regex to avoid future mistakes, even if they arent preceeded by another char Add , as a seperator between episode and extra_info for normal regex Fixes https://github.com/SickRage/sickrage-issues/issues/771
* Fix schedule so it doesnt bork when db upgrade
* Remove the rest of the unnecessary len() in if's Rework the find_search_results a bit to use scene numbers depending if the show is scene or not to determine if the result matches or should be skipped, it was quite iffy, and still is.
* Fix bug that caused plex server/client password to be set to all * when saving notifications if you did not type them in after loading the page
* Use a better exception text for InvalidShow and InvalidName.
* Normalize more name_parser.parse calls and exception handling
* Use the string passed when raising InvalidNameException or InvalidShowException to avoid maintaining log text in too many places.
* Fix small mistake in name_parser, use better variable names in quality pills
* No need to use len to check if a list is not empty (name_parser.parser) No need to cast to list before iterating a set (name_cache) Lint name_parser.parser, fix small bug preventing S00 from being able to be parsed
* Rename initial to preferred in quality pill text

### v2016.02.07-1

[full changelog](https://github.com/SickRage/SickRage/compare/5d51b1687edf252958317c8cbb110069d7b207b3...v2016.02.07-1)

* encode io.open in helper with ek()
* Updated subliminal develop (f245383)
* Updated guessit (28b6789)
* Updated rebulk (68a4588)
* Updated legendastv provider. Fixed a few things in subtitles.py
* Improve bitcannon provider Fixes https://github.com/SickRage/sickrage-issues/issues/763
* Re-enable cachecontrol, except use it in memory
* Fix testing providers search types manually
* Rework tvchaosuk and fix daily search
* Fix log showing errors incorrectly by iterating over a string in PP when unrar fails
* Change speed.cd url to use https to make it work for when ppl use the force secure connections on their site
* Switches nzb and torrent method icons on dropdown switch
* Some fixes concerning the icons.
* Added icons to the buttons & clients.
* Use node 5.0.0 instead of 0.12 for build tests, make npm quiet during ci, updated npm deps
* Replaced all menu icons and logos with colored versions.
* Removed duplicate/unused css code.
* Fix bug in PP where rar'd files would say there were no processable items found in folder after extraction
* Fix typeError breaking backlog/manual/failed searches
* Fixes https://github.com/SickRage/sickrage-issues/issues/736
* Add editorconfig
* Dont show traceback if error sending torrent
* Dont clear old snatch history in failed.db, see if that fixes some issues with fdh
* Various flaking/code cleanup Change log from debug to info for http status code returned from clients Change log from error to warning when sending to client failed (the request failed, client down or network error maybe)
* Fix Attribute Error object has no attribute 'errno'
* Revert "Added add from popular anime list."
* Revert "Added anidb http client."
* Clean up recommended.py
* Optimize order of usage of parameters in __init__, optimize imports
* Fix spacing, tabs, spelling errors, non-unicode strings, docstrings, license information, encoding declarations, EOF, unused variables
* Group french team fansub, new encompassing anime regex
* Some changes to the help & info page.

### v2016.01.31-1

[full changelog](https://github.com/SickRage/SickRage/compare/f568d1515557f854042511d7bfee3ae070c864bd...v2016.01.31-1)

* Fix restart not reloading page
* Add an "Add from anidb popular list" page
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

### v2016.01.23-1

[full changelog](https://github.com/SickRage/SickRage/compare/32c0fcf8b6a238047d028d121f1699fa1207e090...v2016.01.23-1)

* Remove duplicate FDH setting
* Add seeds/leechers to some log messages during searches
* Refactor the way we initialize provider caches
* Standardize providers more
* Add ABNormal and PhxBit providers
* Fix newznab issues with pre-aired episodes and maxage, and bad q params
* Fix several UI bugs
* Add SSL Version to help&info page, and make it pretty
* Fix error when PP finds file of same size exists
* Prepare to add ability to add shows from anidb lists (if they are on tvdb)
* Fix confirmed downloads setting for TPB which was only allowing unconfirmed results
* Fix discrepancy between home and display show for show file size when show has multi-eps
* Fix t411
* Fix several NoneType exceptions

### v2016.01.20-1

[full changelog](https://github.com/SickRage/SickRage/compare/c58107f10fa5fcd1331a2a6a34c1d077839c8af7...v2016.01.20-1)

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

### show

[full changelog](https://github.com/SickRage/SickRage/compare/89efb07b1e482a6c8b21b0ac4e18e069d25c856e...show)

* * Changed: Major change to mako templates from cheetah
* * Added: Mako added to libraries
* * Added: New torrent client deluge daemon (deluged direct)
* * Added: View popular shows on IMDB (Still has issue with images)
* * Added: Free disk space info on status page
* * Added: Send tweets via direct message
* * Added: Ability to use sounds with pushover notifications
* * Added: More missing network logos
* * Removed: Animezb provider (domain up for sale)
* * Updated: Hachoir library updated
* * Updated: Pynma to version 1.0
* * Updated: Wiki URL in post processing
* * Updated: Version checker urls, to use cdn.rawgit
* * Fixed: Stop starting backlog search on show updates
* * Fixed: Rarbg SSL error, switched to http from https
* * Fixed: NyaaTorrents bugs
* * Fixed: Prevent robots from indexing SR pages
* * Fixed: Subtitles flags on history
* * Fixed: Sending torrents to Download Station and others
* * Fixed: NyaaTorrents bug


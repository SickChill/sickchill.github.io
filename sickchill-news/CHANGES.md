### v2021.07.14-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.14-2...v2021.07.14-3)

* update pythonpackage.yml
* Fix label in pythonpackage.yml

### v2021.07.14-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.14-1...v2021.07.14-2)

* poe format

### v2021.07.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-6...v2021.07.14-1)

* Fix source based updater
* Some work on docker builder workflow and dockerfile

### v2021.07.13-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-5...v2021.07.13-6)

* Do not list links to the incorrect wheels, dont install requirements in docker build, let SC do it.
* Release 2021.7.13-4

### v2021.07.13-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-4...v2021.07.13-5)

* Less log spam, update depends

### v2021.07.13-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-3...v2021.07.13-4)

* Handle issue when getsitepackages does not exist
* Publish 2021.7.13-2

### v2021.07.13-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-2...v2021.07.13-3)

* Missed a file, release v2021.7.13-1

### v2021.07.13-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.13-1...v2021.07.13-2)

* Daemonize before poetry/pip code is called, so services do not time out before they fork

### v2021.07.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.12-4...v2021.07.13-1)

* Merge branch 'master' into develop
* isort
* Fix deletion of tempfile created for virtualenv.pyz and get-pip.py (you can manually delete the temp files that were left behind) Better venv python executable detection for systems that use an unconventional method. Signed-off-by: miigotu <miigotu@gmail.com>
* isort
* Use pathlib in update_manager
* Update dockerfile to work with new changes
* Merge branch 'master' into develop
* sc_update
* SC comment cleanup
* Poe format

### v2021.07.12-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.12-3...v2021.07.12-4)

* Release 2021.7.12-6
* Fix auto detection of git path when installer was used on windows
* More path fixes to use nupkg python for windows
* Set proper interpreter for windows
* Add missing url type
* Add ability to use a portable virtualenv module when it does not exist in the environment, also download and run get-pip.py when pip is not available

### v2021.07.12-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.12-2...v2021.07.12-3)

* HOTFIX: Make sure we excplicitly specify python3 as the interpreter of new virtualenvs
* Merge branch 'develop'

### v2021.07.12-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.07.12-1...v2021.07.12-2)

* Merge branch 'develop'

### v2021.07.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.06.16-1...v2021.07.12-1)

* Merge branch 'develop'
* HOTFIX: Logging errors calls to logging.exception were not being handled, which caused many users head scratching and confusion as to why thing were not working when they were not working.
* Hotfix undefined TVShow type hint

### v2021.06.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.04.10-1...v2021.06.16-1)

* Update gruntfile
* Update dependencies Remove thegft tracker (domain jacked) Allow 265 in more regexes
* Update anime regexes to accept 4 digits ep num
* Yarn upgrade
* Merge branch 'master' into develop
* New translations messages.pot (Dutch)
* New translations messages.pot (Dutch)
* New translations messages.pot (Dutch)
* New translations messages.pot (Dutch)
* New translations messages.pot (Dutch)
* New translations messages.pot (Dutch)
* Bump feedparser from 6.0.5 to 6.0.6
* Bump feedparser from 6.0.4 to 6.0.5
* Bump sqlalchemy from 1.4.17 to 1.4.18
* Bump feedparser from 6.0.2 to 6.0.4
* Fix logger format
* Bump pytest-cov from 2.12.0 to 2.12.1
* Bump twilio from 6.59.0 to 6.59.1
* Bump sqlalchemy from 1.4.15 to 1.4.17
* Bump coveralls from 3.0.1 to 3.1.0
* Bump flake8-pytest-style from 1.4.1 to 1.4.2
* New translations messages.pot (French)
* Log Url destination in " " to be consistent with file destination
* Adjusting logging.info result data
* simplify posted logger info
* Revert "Update download_station.py"
* Update download_station.py
* Update download_station.py
* Not a fan of string concatenation
* Call it destination rather than path, because it is a remote destination not a local path
* Make sure we are using the correct path in DSM, and this keeps working for nzb users.
* Update download_station.py
* Bump qbittorrent-api from 2021.5.21 to 2021.5.22
* Bump sqlalchemy from 1.4.14 to 1.4.15
* Bump pytest-cov from 2.11.1 to 2.12.0
* Update torrentday.py
* Isort
* add space after comma for params & add reponse.content in debug log
* use tvdbId for emby show update instead of fs path
* Bump twilio from 6.58.0 to 6.59.0
* Bump pytest-isort from 1.3.0 to 2.0.0
* Release 2021.5.10-1
* Bump python-slugify from 4.0.1 to 5.0.2
* Merge branch 'master' into develop
* Drop twilio until their dependancies are updated for pyjwt
* Create SECURITY.md
* Release 2021.5.6-1
* Upgrade to GitHub-native Dependabot
* Fix ncore torrent provider url
* Add StartYear to detailed show info for api
* Make sure branch names are valid docker tag values
* Update dependancies
* Use user space for pip install in testing
* Bump qbittorrent-api from 2021.4.19 to 2021.4.20
* Bump pymediainfo from 5.0.3 to 5.0.4

### v2021.04.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.04.06-3...v2021.04.10-1)

* Release 2021.4.10
* Do not log info in postprocessor for "@eaDir". Fixes [#7072](https://github.com/SickChill/SickChill/issues/7072)
* Update depends
* Add some type checking in transmission andm qbittorrent project
* Bump twilio from 6.55.0 to 6.56.0
* Bump sqlalchemy from 1.4.5 to 1.4.6
* Bump cloudscraper from 1.2.56 to 1.2.58

### v2021.04.06-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.04.06-2...v2021.04.06-3)

* Skip python req from toml

### v2021.04.06-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.04.06-1...v2021.04.06-2)

* Remove errant line

### v2021.04.06-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.04.05-1...v2021.04.06-1)

* Allow building with setup.py for now, until [#40](https://github.com/python-poetry/poetry-core/pull/40) is merged
* Remove unused lines from poetry
* Release 2021.4.6
* Publish 2021.04.05-1

### v2021.04.05-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.28-3...v2021.04.05-1)

* Bump js2py from 0.70 to 0.71
* poetry update
* Bump flake8-pytest-style from 1.4.0 to 1.4.1
* Bump sqlalchemy from 1.4.3 to 1.4.5
* Fix sending torrent files to synology downloadstation 3.8.16-3566+
* more silly wonkiness for dsm api
* Silly quotes included in json
* Fix coverage
* isort and move isort config to pyproject.toml
* Fix some errors and api issue for downloadstation. I hope it does not break for older DSM.
* yarn upgrade and try to fix a few xo errors
* isort
* Fix errors
* Add poetry.lock
* Add pyproject.toml
* Move to pytest, run black, do some flake8
* Bump y18n from 3.2.1 to 3.2.2
* Add Wow Presents Plus logo
 kodi.py: Add missing unquote_plus
* Release 2021.3.28.post3

### v2021.03.28-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.28-2...v2021.03.28-3)

* Merge branch 'develop'

### v2021.03.28-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.28-1...v2021.03.28-2)

* Merge branch 'develop'

### v2021.03.28-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.27-1...v2021.03.28-1)

* Merge branch 'develop'

### v2021.03.27-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.18-1...v2021.03.27-1)

* Merge branch 'develop'
* Actions ([#7053](https://github.com/SickChill/SickChill/issues/7053))

### v2021.03.18-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.10-1...v2021.03.18-1)

* Remove log spam when saving providers, remove js errors when loading provider options
* Discord name, avatar, and tts were not saved to config. Fixes [#7047](https://github.com/SickChill/SickChill/issues/7047)
* Manually set cloudscraper delay, avoid one more potential parse error
* Update cloudscraper
* New Crowdin updates ([#7048](https://github.com/SickChill/SickChill/issues/7048))
* Network logo - Add Fox Kids ([#7042](https://github.com/SickChill/SickChill/issues/7042))
* isort
* Release 2021.3.10.post1

### v2021.03.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.07-2...v2021.03.10-1)

* Bump elliptic from 6.5.3 to 6.5.4 ([#7040](https://github.com/SickChill/SickChill/issues/7040))
* Fixes [#7039](https://github.com/SickChill/SickChill/issues/7039)
* Add gitignores for readynas, so the updater does not delete the service or config.xml
* Release sickchill-2021.3.7.post2

### v2021.03.07-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.03.07-1...v2021.03.07-2)

* Fix jslint errors again
* Fix jslint errors
* No longer need to save discord settings before testing webhook. Fixes [#6941](https://github.com/SickChill/SickChill/issues/6941)
* Fix string for detection of nebulance login failure Possibly fixes [#7033](https://github.com/SickChill/SickChill/issues/7033)
* Release 2021.3.7.post1

### v2021.03.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.17-1...v2021.03.07-1)

* Suppress error when users cant get their locale and timezone right. Fixes [#6869](https://github.com/SickChill/SickChill/issues/6869)
* New Crowdin updates ([#7035](https://github.com/SickChill/SickChill/issues/7035))
* New Crowdin updates ([#7024](https://github.com/SickChill/SickChill/issues/7024))
* New Crowdin updates ([#7023](https://github.com/SickChill/SickChill/issues/7023))
* Some more cleanup in post_processor Add torrent-paradise icon Remove unused imports More translated post_processing strings
* isort
* Look up release name from the cache if a urlk is passed for failed download from nzbtomedia Translate some logs in post processor and failed processor Refactor some screwy variable names that made confusion
* Fix only allowed branches or branches-ignore (terrible docs)
* Fix syntax error
* Ignore build for commits and pull requests from crowdin
* Add cancel-workflow-action
* New translations messages.pot (English, United Kingdom)
* New translations messages.pot (Spanish)
* New translations messages.pot (Afrikaans)
* New translations messages.pot (Arabic)
* New translations messages.pot (Bulgarian)
* New translations messages.pot (Catalan)
* New translations messages.pot (Czech)
* New translations messages.pot (Danish)
* New translations messages.pot (German)
* New translations messages.pot (Greek)
* New translations messages.pot (Finnish)
* New translations messages.pot (Hebrew)
* New translations messages.pot (Hungarian)
* New translations messages.pot (Italian)
* New translations messages.pot (French)
* New translations messages.pot (Dutch)
* New translations messages.pot (Polish)
* New translations messages.pot (Portuguese)
* New translations messages.pot (Russian)
* New translations messages.pot (Slovak)
* New translations messages.pot (Slovenian)
* New translations messages.pot (Swedish)
* New translations messages.pot (Turkish)
* New translations messages.pot (Chinese Simplified)
* New translations messages.pot (Chinese Traditional)
* New translations messages.pot (English)
* New translations messages.pot (Portuguese, Brazilian)
* New translations messages.pot (Estonian)
* New translations messages.pot (Norwegian)
* New translations messages.pot (Romanian)
* New translations messages.pot (English, United Kingdom)
* New translations messages.pot (Spanish)
* New translations messages.pot (Afrikaans)
* New translations messages.pot (Arabic)
* New translations messages.pot (Bulgarian)
* New translations messages.pot (Catalan)
* New translations messages.pot (Czech)
* New translations messages.pot (Danish)
* New translations messages.pot (German)
* New translations messages.pot (Greek)
* New translations messages.pot (Finnish)
* New translations messages.pot (Hebrew)
* New translations messages.pot (Hungarian)
* New translations messages.pot (Italian)
* New translations messages.pot (French)
* New translations messages.pot (Dutch)
* New translations messages.pot (Polish)
* New translations messages.pot (Portuguese)
* New translations messages.pot (Russian)
* New translations messages.pot (Slovak)
* New translations messages.pot (Slovenian)
* New translations messages.pot (Swedish)
* New translations messages.pot (Turkish)
* New translations messages.pot (Chinese Simplified)
* New translations messages.pot (Chinese Traditional)
* New translations messages.pot (English)
* New translations messages.pot (Portuguese, Brazilian)
* New translations messages.pot (Estonian)
* New translations messages.pot (Norwegian)
* New translations messages.pot (Romanian)
* Update messages.pot
* Show warning on login page when incorrect username or pass is used.
* Fixes [#7015](https://github.com/SickChill/SickChill/issues/7015)
* Release 2021.2.17.post1

### v2021.02.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.15-3...v2021.02.17-1)

* Add deprecated parameters back to post processing api, to fix proper release processing from nzbtomedia
* Add torrent-paradise provider for backlog searching.
* Release 2021.2.15.post3

### v2021.02.15-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.15-2...v2021.02.15-3)

* isort
* Further attempt at fixes [#6929](https://github.com/SickChill/SickChill/issues/6929)
* Release 2021.2.15.post2

### v2021.02.15-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.15-1...v2021.02.15-2)

* Undo nyaran fix for [#6945](https://github.com/SickChill/SickChill/issues/6945), try to use other fixes
* Try to fix build, again. Temporary fix for cryptography rust requirement. Image size reduced again.
* Fix build. Switch from python3.7-alpine to python3.8-slim base image for docker images. This increases the size of the docker images, but is a more complete installation and I could not get the build working for cryptography anymore on alpine because the rust compiler was finicky.
* Fix build by adding rust cargo to dockerfile
* Release sickchill-2021.2.15.post1

### v2021.02.15-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.14-1...v2021.02.15-1)

* 2021.2.14.post2.dev2+g480aa2717
* Fix manual snatch for nzb users Fixes [#6926](https://github.com/SickChill/SickChill/issues/6926) Fixes [#6959](https://github.com/SickChill/SickChill/issues/6959) Fixes [#6973](https://github.com/SickChill/SickChill/issues/6973)
* Release 2021.2.14.post1

### v2021.02.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.13-1...v2021.02.14-1)

* Fix getting api key using getkey endpoint Fixes [#7006](https://github.com/SickChill/SickChill/issues/7006)
* Alias tv4-se logo Fixes [#7005](https://github.com/SickChill/SickChill/issues/7005)
* Allow setting a custom url for nyaa. Fixes [#7009](https://github.com/SickChill/SickChill/issues/7009)
* Try to fix api status matching. Fixes [#6929](https://github.com/SickChill/SickChill/issues/6929)
* Release 2021.2.13.post1

### v2021.02.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.05-1...v2021.02.13-1)

* Try to clean up post processing when setting parent set-id bit fails.
* Update helpers.py
* Release 2021.2.5.post1

### v2021.02.05-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.02-3...v2021.02.05-1)

* Revert "Ignore abc.xyz.mkv"
* Release 2021.2.2.post3

### v2021.02.02-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.02-2...v2021.02.02-3)

* Merge branch 'develop'

### v2021.02.02-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2021.02.02-1...v2021.02.02-2)

* Merge branch 'develop'

### v2021.02.02-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.11.24-1...v2021.02.02-1)

* Merge branch 'develop'
* Develop ([#6986](https://github.com/SickChill/SickChill/issues/6986))
* Develop ([#6967](https://github.com/SickChill/SickChill/issues/6967))
* Fix [#6957](https://github.com/SickChill/SickChill/issues/6957)
* change yggtorrent url
* Fix [#6945](https://github.com/SickChill/SickChill/issues/6945)
* Fix [#6944](https://github.com/SickChill/SickChill/issues/6944)
* Fix [#6944](https://github.com/SickChill/SickChill/issues/6944)
* Fix [SickChill/SickChill#6942](https://github.com/SickChill/SickChill/issues/6942)
* Demonoid provider cleanup
* Enable demonoid tests
* Fix demonoid provider
* Bump ini from 1.3.5 to 1.3.7
* Ignore abc.xyz.mkv

### v2020.11.24-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.11.16-1...v2020.11.24-1)

* Corrected URL
* Fixes exception caused by UTF8 decoding attempt before decompression of long packets (>1400 bytes)
* Fixes [#6892](https://github.com/SickChill/SickChill/issues/6892)
* Release sickchill-2020.11.16.post1

### v2020.11.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.10.22-2...v2020.11.16-1)

* Fix some errors with sending telegram messages
* fixup: Fix [#6822](https://github.com/SickChill/SickChill/issues/6822) - Review comments
* Fix [#6822](https://github.com/SickChill/SickChill/issues/6822)
* iptorrents new style
* xo fixes
* Improve manual search table. [SickChill/SickChill#6879](https://github.com/SickChill/SickChill/issues/6879)  - Add filtering option  - Stylize quality column  - Improve sort order for quality column  - Improve sort order for file size column
* Release 2020.10.22.post2

### v2020.10.22-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.10.22-1...v2020.10.22-2)

* Yarn upgrade

### v2020.10.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.28-2...v2020.10.22-1)

* Fix None comparison with ==
* Fix [#5298](https://github.com/SickChill/SickChill/issues/5298)
* adba band-aid
* Update Emby API Library updates
* New networks logos
* Update debian-ubuntu-install.sh
* Fix backstretch. Doesn't need scRoot with meta tag
* Release 2020.9.28.post2

### v2020.09.28-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.28-1...v2020.09.28-2)

* Allow selection of whether to verify cert for qbittorrent Do not force port to 8080 if user did not supply a port for qbittorrent (breaks running with privileged ports) Fixes [#6808](https://github.com/SickChill/SickChill/issues/6808)
* Release 2020.9.28.post1

### v2020.09.28-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.26-1...v2020.09.28-1)

* Typo
* Use custom background on displayshow if fanart is not found
* Remove include_date, fix static_url include_version
* Fix fetch custom images when using authentication
* Fixes [SickChill/SickChill#6809](https://github.com/SickChill/SickChill/issues/6809)
[network] add some new covers
* Release 2020.9.26.post1

### v2020.09.26-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.24-3...v2020.09.26-1)

* Sanitize names when doing a get_show to better match existing shows
* Fixes [SickChill/SickChill#6803](https://github.com/SickChill/SickChill/issues/6803)
* Release 2020.9.24.post3

### v2020.09.24-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.24-2...v2020.09.24-3)

* Update webapi.py
* Fix mako error on add-movies page

### v2020.09.24-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.24-1...v2020.09.24-2)

* Set the host/username/password labels when selecting synology on nzb client page.

### v2020.09.24-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.23-2...v2020.09.24-1)

* Make the restart page wait longer to check for SC to restart Fixes [#6798](https://github.com/SickChill/SickChill/issues/6798)
* Release 2020.9.23.post2

### v2020.09.23-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.23-1...v2020.09.23-2)

* Rework pushover notifier to use requests, and be able to verify the server https certificate
* Release 2020.9.23.post1

### v2020.09.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.22-5...v2020.09.23-1)

* Fix mistake when searching tvdb over api Fixes [#6791](https://github.com/SickChill/SickChill/issues/6791)
* Make sure to catch all requests exceptions. Fixes [#6786](https://github.com/SickChill/SickChill/issues/6786)
* Fix build
* Release 2020.9.22.post5

### v2020.09.22-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.22-4...v2020.09.22-5)

* Make sure good search results are also added to the cache to use for manual search
* Fix domain for torrentz
* Add ability to snatch season packs manually. Fixes [#6790](https://github.com/SickChill/SickChill/issues/6790)
* Release 2020.9.22.post4

### v2020.09.22-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.22-3...v2020.09.22-4)

* Better mako error handling, still show a pretty page when we run out of disk space
* Release 2020.9.22.post3

### v2020.09.22-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.22-2...v2020.09.22-3)

* Fix problem with imdbpy when version > 2020.09.20
* Release 2020.9.22.post2

### v2020.09.22-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.22-1...v2020.09.22-2)

* Fix pip version strings for updater again
* isort
* Release 2020.9.22.post1

### v2020.09.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.21-2...v2020.09.22-1)

* Fix help&info for pip installs Fixes [#6788](https://github.com/SickChill/SickChill/issues/6788)
* Fix restarting when using a pip install Fix cache dir permissions issues (symlink no longer needed)
* Release 2020.9.21.post2

### v2020.09.21-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.21-1...v2020.09.21-2)

* Fix version numbers for pip installs for checking changes when an update is available Fixes [#6787](https://github.com/SickChill/SickChill/issues/6787) Signed-off-by: miigotu <miigotu@gmail.com>
* Release 2020.9.21.post1

### v2020.09.21-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-7...v2020.09.21-1)

* Remove backports_abc, use tarball for imdbpy for users who do not have git (maybe it fixes the issue?)
* Release 2020.9.20.post7

### v2020.09.20-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-6...v2020.09.20-7)

* Set context for nzbget and bsplayer for ssl_verify
* Release 2020.9.20.post6

### v2020.09.20-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-5...v2020.09.20-6)

* Disable check_hostname in urllib.request if not verifying certs

### v2020.09.20-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-4...v2020.09.20-5)

* Remove -rrequirements.txt from tox so that it wirks with dependency_links

### v2020.09.20-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-3...v2020.09.20-4)

* Fix checking remote db version for pip installs in the updater
* Fix imdbpy requirement. Replaces [#6782](https://github.com/SickChill/SickChill/issues/6782) Fixes [#6781](https://github.com/SickChill/SickChill/issues/6781)

### v2020.09.20-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-2...v2020.09.20-3)

* Add hbo max image Attempt to fix [#6773](https://github.com/SickChill/SickChill/issues/6773)

### v2020.09.20-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.20-1...v2020.09.20-2)

* Fix requirement version for imdbpy
* Fix dependency link for imdbpy

### v2020.09.20-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.19-2...v2020.09.20-1)

* Set ssl_verify properly on the default urllib.reuest opener and respect sickchill settings

### v2020.09.19-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.19-1...v2020.09.19-2)

* Yarn upgrade

### v2020.09.19-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-6...v2020.09.19-1)

* Fix naming anime pattern.  ([#6774](https://github.com/SickChill/SickChill/issues/6774))

### v2020.09.17-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-5...v2020.09.17-6)

* Do not depend on sysconfig to check if sickchill was installed with pip, use importlib instead

### v2020.09.17-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-4...v2020.09.17-5)

* Quiet error for tvsubtitulo and subtitulamos Fixes [#6724](https://github.com/SickChill/SickChill/issues/6724)

### v2020.09.17-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-3...v2020.09.17-4)

* Fix an expected type error in scene exceptions

### v2020.09.17-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-2...v2020.09.17-3)

* Fix similar variable name confusion

### v2020.09.17-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.17-1...v2020.09.17-2)

* Do not error with outdated imdbpy

### v2020.09.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.16-3...v2020.09.17-1)

* Try adding show_name and custom_name to all_seasons exceptions
* Release sickchill-2020.9.16.post3

### v2020.09.16-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.16-2...v2020.09.16-3)

* Fix problem with name cache/get_show, probably fixes the post processing problem
* Add imdbpy as a dependancy link
* Release sickchill-2020.9.16.post2

### v2020.09.16-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.16-1...v2020.09.16-2)

* Fix error with replace_map and fstrings. Fixes [#6751](https://github.com/SickChill/SickChill/issues/6751)

### v2020.09.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.14-2...v2020.09.16-1)

* Fix changed bencodepy exception names and method names Fixes [#6745](https://github.com/SickChill/SickChill/issues/6745)
* Remove exceptionsSeasonCache and get_scene_seasons Refactor scene_exceptions and name_cache Fixes [#6743](https://github.com/SickChill/SickChill/issues/6743)
* Fix rebuild_exception_cache ([#6752](https://github.com/SickChill/SickChill/issues/6752))
* Change function to arrow function
* Fixes [SickChill/SickChill#6746](https://github.com/SickChill/SickChill/issues/6746)
* Better imdb_id verification for tv

### v2020.09.14-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.14-1...v2020.09.14-2)

* Locale for imdbpy is broken
* Fix bundled libs, Remove imdbpie re-add imdbpy ([#6740](https://github.com/SickChill/SickChill/issues/6740))

### v2020.09.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.13-2...v2020.09.14-1)

* Disable re-register of legendas and fix indentation error in addic7ed

### v2020.09.13-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.13-1...v2020.09.13-2)

* Fixes [SickChill/SickChill#6732](https://github.com/SickChill/SickChill/issues/6732) ([#6736](https://github.com/SickChill/SickChill/issues/6736))
* Release 2020.9.13.post1

### v2020.09.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.12-3...v2020.09.13-1)

* Use certifi for cert verification Replaces [#6737](https://github.com/SickChill/SickChill/issues/6737)
* Update bundled libs in lib3

### v2020.09.12-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.12-2...v2020.09.12-3)

* Episode thumbs only have one option. Fixes multiple error Fixes [#6735](https://github.com/SickChill/SickChill/issues/6735)
* Update init.freebsd
* Release 2020.9.12.post2

### v2020.09.12-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.12-1...v2020.09.12-2)

* Do not log an error if a show has no network on thetvdb
* Release 2020.9.12.post1

### v2020.09.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.11-3...v2020.09.12-1)

* Fix extra blank line
* Fix encoding error in sb.searchtvdb webapi, by not casting =P Fixes [#6733](https://github.com/SickChill/SickChill/issues/6733)
* Release 2020.9.11.post3

### v2020.09.11-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.11-2...v2020.09.11-3)

* Fix labelling when snatching manual (provide the show in the result) Fixes [#6693](https://github.com/SickChill/SickChill/issues/6693)#issuecomment-691201067
* Release 2020.9.11.post2

### v2020.09.11-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.11-1...v2020.09.11-2)

* Fix getting show from scene exception Thanks Nyaran

### v2020.09.11-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.10-3...v2020.09.11-1)

* Fix image selector for shows Fixes [#6721](https://github.com/SickChill/SickChill/issues/6721)
* isort
* Release 2020.9.10.post3

### v2020.09.10-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.10-2...v2020.09.10-3)

* Fix error on add from imdb popular and make the code use imdbpie (for now) Fixes [#6719](https://github.com/SickChill/SickChill/issues/6719)
* Release 2020.9.10.post2

### v2020.09.10-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.10-1...v2020.09.10-2)

* Fix error on testRename Fixes [#6711](https://github.com/SickChill/SickChill/issues/6711)

### v2020.09.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.09-2...v2020.09.10-1)

* Use the date string as q when doing nzb tvdbid search for shows that are air by date, and leave season and ep out Fixes [#6718](https://github.com/SickChill/SickChill/issues/6718)
* Fix error in rarbg Fixes [#6715](https://github.com/SickChill/SickChill/issues/6715)
* isort
* Release 2020.9.9.post2

### v2020.09.09-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.09-1...v2020.09.09-2)

* Fix emby notifications Fixes [#6701](https://github.com/SickChill/SickChill/issues/6701)
* Relase 2020.9.9.post1

### v2020.09.09-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.08-1...v2020.09.09-1)

* Fix sending with qbittorrent Fix error with manual snatching on qbit (all will use regualr sickchill label on manual snatch for now) Fixes [#6706](https://github.com/SickChill/SickChill/issues/6706)
* Release 2020.9.8.post1

### v2020.09.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.07-5...v2020.09.08-1)

* Fix adding labels in deluged Fixes [#6693](https://github.com/SickChill/SickChill/issues/6693)

### v2020.09.07-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.07-4...v2020.09.07-5)

* Fix toggling log level (debug on/off) which was stopping all logging (It was set to critical level) Fixes [#6691](https://github.com/SickChill/SickChill/issues/6691)
* Release pypi 2020.9.7.post4

### v2020.09.07-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.07-3...v2020.09.07-4)

* Fix sending torrent-file results to transmission, deluge, and deluged Fixes [#6690](https://github.com/SickChill/SickChill/issues/6690)
* Make sure tvdb image url does not have _cache in it
* Fix url for update comparison
* Merge branch 'develop'
* Revert "Pypi release 2020.9.7.post3"
* Pypi release 2020.9.7.post3

### v2020.09.07-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.07-2...v2020.09.07-3)

* Fix failure to start due to translations by byassing if it fails (hacky) Try to fix an empty environment variable for language Fixes [#6702](https://github.com/SickChill/SickChill/issues/6702)

### v2020.09.07-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.07-1...v2020.09.07-2)

* PyPi release 2020.9.7.post1

### v2020.09.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-7...v2020.09.07-1)

* Fix rtorrent (bug in new-rtorrent-python) Add debug around rtorrent error and update lib3
* Release 2020.9.6.post7

### v2020.09.06-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-6...v2020.09.06-7)

* Use pills for episode statuses in displayShow Clean up updater code a bit, set url for pip updater to take the user to pypi Do not show branch warning on pip installs Better classes for true/false on status page
* PiPy 2020.9.6.post6

### v2020.09.06-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-5...v2020.09.06-6)

* Fix updater checking if installed via pip

### v2020.09.06-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-4...v2020.09.06-5)

* Fix build
* Isort

### v2020.09.06-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-3...v2020.09.06-4)

* Fix error when creating hash for torrent files (bencode error) Fixes [#6686](https://github.com/SickChill/SickChill/issues/6686)

### v2020.09.06-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-2...v2020.09.06-3)

* Disable urllib3 warnings so that log is not spammed when settings.SSL_VERIFY is False. Fixes [#6687](https://github.com/SickChill/SickChill/issues/6687)

### v2020.09.06-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.06-1...v2020.09.06-2)

* Set external loggers back to critical level. Stops logging of missing static files Fixes [#6683](https://github.com/SickChill/SickChill/issues/6683)

### v2020.09.06-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.05-5...v2020.09.06-1)

* Fix error on displayshow if you have a download url set in settings. Fixes [#6688](https://github.com/SickChill/SickChill/issues/6688)
* Resize ctv drama
* Added CTV Drama icon

### v2020.09.05-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.05-4...v2020.09.05-5)

* Fix missed string decode on massEDit Fixes [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-687687584

### v2020.09.05-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.05-3...v2020.09.05-4)

* Fix error on status page when show queue has items. Fixes [#6682](https://github.com/SickChill/SickChill/issues/6682)

### v2020.09.05-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.05-2...v2020.09.05-3)

* Ignore sickbeard.db

### v2020.09.05-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.09.05-1...v2020.09.05-2)

* Yarn upgrade
* Release 0.0.56 to PyPi

### v2020.09.05-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.08.07-1...v2020.09.05-1)

* Yarn upgrade
* Add cookie auth to speedcd (cookies required due to cloudflare), fix search and page parsing. Fixes [#6562](https://github.com/SickChill/SickChill/issues/6562)
* Add s to update message when number of commits is not 1
* Bump pypy version to 0.0.55
* Fix loggers displaying access messages after enabling/disabling debug and show imdb images for movies index and details
* Fix error when uid/gid is passed to docker and the user does not exist in the container. Try to fix logging levels for tornado.access
* gitignore movies.db
* Instantiate movie list for tests, fix build
* Make rss work better for movies with rarbg
* Make rss work for movies with rarbg
* More
* Add movie backlog queue item
* RARBG provider supports movies
* Work on methods to search for movies
* Cleaner merged imdb/tmdb data on adding movies
* Add adult option checkbox for movies, and get both imdb and tmdb data regardless of which was used to add the movie
* Clean up movie-search page, imdb/tmdb popular movies
* Fix xo errors
* Add genres, fix title on movie-details
* Grunt
* Make adding movies work, add some info to movie-details
* Isort
* More fleshing out of movies GUI
* More work on getting movies added to the DB
* Bump pypi to 0.0.54
* Make some more concise error/debug logging in name parser tests and disable testing anime_bare without specifying anime. anime_bare is only when adding existing shows or the folder name has the group/release name.
* Clear name parser cache between tests
* Run anime tests...
* Add some tests
* Fix string.format to fstrings, some cleanup, and undo the filtering for series_name
* Apply fixes and suggestions by @miigotu
* Extra checks
* Improve anime series detection [SickChill/SickChill#6646](https://github.com/SickChill/SickChill/issues/6646)
* Bump pypi to 0.0.53
* Fix SORT_ARTICLE
* Remove hardcoded ref in checkout for deploy runner
* Fix core.js import when DEVELOPER mode is enabled
* Remove hardcoded ref in checkout for test runner
* Bump pypi to 0.0.52
* Enum34 should not be installed in lib3
* Bump pypi to 0.0.51
* Update bundled libs
* Some more
* More work on views, hidden unless developer=True
* Add some skeleton-views and methods for movies
=P
* Fixing xo alerts
* Fix scrollable content on ui-dialog (file dialog and image selector dialog)
* Shh, anyone wanna help?
* Bump pypi to 0.0.50
* Fix thread statuses when --daemon is set, fork before starting threads =P, Fixes [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-678732143 Fixes [#6637](https://github.com/SickChill/SickChill/issues/6637)
* Make update method call the correct updater
* isort
* Bump pypi to 0.0.49
* Fixes [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-678068706
* Bump pypi to 0.0.48
* Fix update url
* Bump pypi version to 0.0.47
* Bring back support for python 3.6
* Bump pypi to 0.0.46
* Fix rtorrent connection
* Bump pypi to 0.0.45
* Fixes [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-677995622
* Fix clearing warnings button
* Clean up unused imports
* Bump pypi to 0.0.44
* Some cleanup of unused variables
* Fix error parsing rss cache items (horriblsubs) [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-675506303
* Fix error in proper finder [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-675506303
* Bump pypi to 0.0.43
* Try to fix delete rar contents (Almost never need to save those) Drop support for python 3.6 due to text parameter of subprocess.Popen
* Fix build
* Merge pull request [#6663](https://github.com/SickChill/SickChill/issues/6663) from RB14060/RB14060-bet+
* Remove old db upgrades. We will only support db 44+ now. Improves speedup and code.
* Some fstrings and translatable strings
* fix() Duplicated line
* feat() ui-dialog: Pin browser input & imageSelector drowdown to top
* Fix xo error
* fix() Hotfix to remove "Close" text on dialogs
* isort
* Make show image selector work with adblockers by self-proxying
* Bump pypy to 0.0.42
* Merge pull request [#6655](https://github.com/SickChill/SickChill/issues/6655) from SickChill/custom_show
* feat() Add network logo for Audience, La Uno (TVE1), Jiangsu TV, YTV (JP)
* Bump pypi to 0.0.41
* Make status prettier with timeago
* Make status page prettier with more thread status colors. Try to fix is_alive error.
* Clean up api builder and use main navbar, and add a link to it in the config menu
* Fix season/episode selection on apiBuilder
* Fix some deprecated and incompatible tags in html/mako
* Add itv encore network image
* Add font-awesome into bower instead of included in source manually. Add fork-awesome css map
* Add slack and telegram links to help&info and menu
* Add discord invite link and add fork-awesome fonts/css.
* Bump pypi to 0.0.40
* Remove random_user_agent altogether (slows startup and triggers CF). Re-enable yggtorrent and torrentz
* yarn upgrade
* Bump pypi to 0.0.39
* Fix error with tornado returning bytes for requests arguments causing nzbToMedia to fail. Fixes [#1765](https://github.com/clinton-hall/nzbToMedia/issues/1765)#issuecomment-673974074
* Use real user agent for xem and non-providers, spoof only on a case-by-case basis if necessary
* Refactor tv from oldbeard to sickchill
* Fix startup on python3.8 when libs arent install in the environment. Rename deprecated mathods
* Python3 - Fix issue with new tv dirty setter not always being marked dirty ([#6636](https://github.com/SickChill/SickChill/issues/6636))
* Python3 ([#6635](https://github.com/SickChill/SickChill/issues/6635))
* Python3 - Fix magentDL ([#6634](https://github.com/SickChill/SickChill/issues/6634))
* Add method mass_upsert, and use it for cache entries. Add test making sure it works. ([#6633](https://github.com/SickChill/SickChill/issues/6633))
* Cleanup a bit and make tests work through setuptools ([#6631](https://github.com/SickChill/SickChill/issues/6631))
* Fix url for main db version check ([#6630](https://github.com/SickChill/SickChill/issues/6630))
* Fix error on traktTrending: [#6545](https://github.com/SickChill/SickChill/issues/6545)#issuecomment-672630826 ([#6629](https://github.com/SickChill/SickChill/issues/6629))
* Python3 fixes ([#6628](https://github.com/SickChill/SickChill/issues/6628))
* isort
* Bump version for pypi
* Fix editShow
* Fix telegram and some other type mismatches
* Isort
* Bump pypi version to 0.0.28
* First preview of manual snatch. There will probably be a few hiccups but it seems to work
* Minor cleaning
* Bump pypi version 0.0.27
* Fix restore of sickbeard.db to sickchill.db
* Fix mako error on login page
* Remove unused imports, bump versionb
* Fix error in web api
* Bump version
* Fix missed comma
* Fix undefined on errorlogs page
* Fix quirk with urllib3 proxies not working without a default scheme set. Fixes [#6621](https://github.com/SickChill/SickChill/issues/6621)
* Fix dynamic import for clients, Fixes [#6622](https://github.com/SickChill/SickChill/issues/6622)
* Add view and template for manual snatch selection. Unfinished Fix cache duping, add indexes and use SQLITE CONFLICT syntax
* Bump version
* Add seeders, leechers, size, added to provider cache and keep results
* Bump pypi to 0.0.22
* Eliminate tox.ini
* bump pypi version to 0.0.21
* Fix mistake in backup resotre Fixes [#6619](https://github.com/SickChill/SickChill/issues/6619)
* Bump pypi to 0.0.20
* Rename sickchill.sickbeard to sickchill.oldbeard and clean up some md
* Move logger from sickchill.sickbeard to sickchill
* Refactor updater, rename and move it, add preliminary pip updater/notifier
* Bump pypi version
* Fix backlog overview error. Fixes [#6618](https://github.com/SickChill/SickChill/issues/6618)
* Update version for pypi
* Rename sickbeard.db to sickchill.db Fix some errors with PROG_DIR and DATA_DIR Fix problem with the git updater Check if installed by pip, use /home/dusted/sickchill for DATA if so and disable updater for now. Use /home/dusted/sickchill for default DATA_DIR if old location does not have existing db/ini
* Add setuptools-scm
* Try to get codecov working again
* Cleanup ical/googlecal events and image
* Merge pull request [#6572](https://github.com/SickChill/SickChill/issues/6572) from SickChill/py3-again

### v2020.08.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.07.18-1...v2020.08.07-1)

* Merge branch 'develop'

### v2020.07.18-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.07.09-1...v2020.07.18-1)

* Merge branch 'develop'
* Bump lodash from 4.17.15 to 4.17.19 ([#6577](https://github.com/SickChill/SickChill/issues/6577))
* Update pythonpackage.yml ([#6569](https://github.com/SickChill/SickChill/issues/6569))

### v2020.07.09-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.07.08-1...v2020.07.09-1)

* Update pythonpackage.yml ([#6566](https://github.com/SickChill/SickChill/issues/6566))

### v2020.07.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.07.06-1...v2020.07.08-1)

* testRename
* Update libs

### v2020.07.06-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.20-2...v2020.07.06-1)

* push default arch only to github packages only if master
* push default arch only to github packages
* Undo changes to deploy
* Bump tmdbsimple from 2.2.25 to 2.4.0 ([#6561](https://github.com/SickChill/SickChill/issues/6561))
* switch from unrar-free to unrar ([#6555](https://github.com/SickChill/SickChill/issues/6555))
* useful discord notifications ([#6558](https://github.com/SickChill/SickChill/issues/6558))
* Update libs
* Bump tmdbsimple from 2.2.23 to 2.2.25 ([#6550](https://github.com/SickChill/SickChill/issues/6550))
* Bump html5lib from 1.0.1 to 1.1 ([#6551](https://github.com/SickChill/SickChill/issues/6551))
* Test deploy to pkg.github
* Cache docker layers for the whole branch rather than just a commit
* lowercase docker image name

### v2020.06.20-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.20-1...v2020.06.20-2)

* Use local build caching for docker buildx and also push to github packages

### v2020.06.20-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.17-1...v2020.06.20-1)

* Fix is-alive callback for restarting SC. Fixes [#6543](https://github.com/SickChill/SickChill/issues/6543)
* Merge pull request [#6546](https://github.com/SickChill/SickChill/issues/6546) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.23

### v2020.06.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.15-4...v2020.06.17-1)

* Some gui updates, use https for github/thetvdb/sickchill.github.io
* Merge pull request [#6542](https://github.com/SickChill/SickChill/issues/6542) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.22
* Merge pull request [#6540](https://github.com/SickChill/SickChill/issues/6540) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.21

### v2020.06.15-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.15-3...v2020.06.15-4)

* Use full size images for thumbs since tvdb would rather waste bandwidth than allow us to use the cached thumbnails. Fixes [#6537](https://github.com/SickChill/SickChill/issues/6537)
* New Crowdin updates ([#6538](https://github.com/SickChill/SickChill/issues/6538))
* Fix issues with updating inside linuxserver.io docker container, by checking out master instead of the tag. You will need to update with watchtowerrr or another method once to get this fix once the container is built, or run: docker exec -it sickchill /bin/bash -c 'cd /app/sickchill && git checkout master' && docker restart sickchill
* Rename inc_home_showList.mako -> inc_home_show_list.mako
* Bump tmdbsimple from 2.2.17 to 2.2.20 ([#6535](https://github.com/SickChill/SickChill/issues/6535))

### v2020.06.15-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.15-2...v2020.06.15-3)

* Add post processor queue tasks to the status page. Refactor and clean up html/mako for status page
* Allow forcing an auto post process on the manage searches page. Add post processor task scheduler to status page Sort schedulers on status page Refactor Auto post processor Clean up log lines for clarity in code for post processor

### v2020.06.15-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.15-1...v2020.06.15-2)

* Show release_name in logging when post processing a specific release. Fixes [#6509](https://github.com/SickChill/SickChill/issues/6509)

### v2020.06.15-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.14-4...v2020.06.15-1)

* Show release_name in response to webapi post process call if it was provided, otherwise show the path. Fixes [#6509](https://github.com/SickChill/SickChill/issues/6509)

### v2020.06.14-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.14-3...v2020.06.14-4)

* Fix docker deploy

### v2020.06.14-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.14-2...v2020.06.14-3)

* Add specific keys to edit in config.ini when the forced credentials message appears.

### v2020.06.14-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.14-1...v2020.06.14-2)

* Allow all private IP ranges without a password, in addition to  local IPs, until we can parse ip routes for docker and other container installs. Fixes [#6531](https://github.com/SickChill/SickChill/issues/6531)

### v2020.06.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.12-3...v2020.06.14-1)

* Update requirements.txt
* Fix code errors, optimize method, and replace is_ip_private with is_ip_local
* Don't require passwords local networks

### v2020.06.12-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.12-2...v2020.06.12-3)

* grunt
* Make an attempt to fix dbCompare when it errors, by trying https instead of http, and just checking master. Fixes [#6510](https://github.com/SickChill/SickChill/issues/6510)

### v2020.06.12-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.12-1...v2020.06.12-2)

* Prevent sbfdate and sbfdatetime from causing an error. Fixes [#6155](https://github.com/SickChill/SickChill/issues/6155)

### v2020.06.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-6...v2020.06.12-1)

* Update the docker-compose with suggested gui/cache and timezone mounts Set the source to 777 so git updater works with docker (makes the image larger) and provide a docker run example in the Dockerfile Add more logging for [#6522](https://github.com/SickChill/SickChill/issues/6522)
* Bump tmdbsimple from 2.2.15 to 2.2.17 ([#6527](https://github.com/SickChill/SickChill/issues/6527))
* Bump tmdbsimple from 2.2.11 to 2.2.15 ([#6515](https://github.com/SickChill/SickChill/issues/6515))
* New Crowdin translations ([#6516](https://github.com/SickChill/SickChill/issues/6516))
* Add missing Discovery Canada logo ([#6524](https://github.com/SickChill/SickChill/issues/6524))
* Adding Rocket.Chat Notifications ([#6526](https://github.com/SickChill/SickChill/issues/6526))

### v2020.06.07-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-5...v2020.06.07-6)

* Prevent tvshow-trailer.mp4 from being mistaken as a media file Fixes [#6513](https://github.com/SickChill/SickChill/issues/6513)

### v2020.06.07-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-4...v2020.06.07-5)

* Try to get all data removed from all places of the db when removing a show. Fixes [#6511](https://github.com/SickChill/SickChill/issues/6511) Hopefully

### v2020.06.07-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-3...v2020.06.07-4)

* Fix issue with setting correct port. Fixes [#6512](https://github.com/SickChill/SickChill/issues/6512)

### v2020.06.07-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-2...v2020.06.07-3)

* Better logging when nfo file has bunk info

### v2020.06.07-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.07-1...v2020.06.07-2)

* Add ability to pass release_name (nzbName/TorrentName) when calling post process from the api Fixes [#6509](https://github.com/SickChill/SickChill/issues/6509)

### v2020.06.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.03-4...v2020.06.07-1)

* Allow certs external to SC to be set without having to link or copy them to the SC source root Add logging around creating ssl certs (There is an x509 error currently when creating certs)
* Bump websocket-extensions from 0.1.3 to 0.1.4 ([#6508](https://github.com/SickChill/SickChill/issues/6508))
* Update tmdbsimple
* Bump tmdbsimple from 2.2.10 to 2.2.11 ([#6505](https://github.com/SickChill/SickChill/issues/6505))

### v2020.06.03-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.03-3...v2020.06.03-4)

* Adjust deluge clients to not set paths when they arent set in SC, so that defaults work in deluge.

### v2020.06.03-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.03-2...v2020.06.03-3)

* Use new github action for buildx

### v2020.06.03-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.06.03-1...v2020.06.03-2)

* Allow cross origin for api if the correct api key is given. Fixes [#6475](https://github.com/SickChill/SickChill/issues/6475)

### v2020.06.03-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.30-1...v2020.06.03-1)

* Update libs
* Adding missing network logos ([#6490](https://github.com/SickChill/SickChill/issues/6490))
* Merge pull request [#6493](https://github.com/SickChill/SickChill/issues/6493) from SickChill/dependabot/pip/develop/mako-1.1.3
* Merge pull request [#6494](https://github.com/SickChill/SickChill/issues/6494) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.10

### v2020.05.30-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.28-1...v2020.05.30-1)

* Add ParseError exception catching for update_episode_metadata - Best I can do for now (needs refactored) Fixes [#6484](https://github.com/SickChill/SickChill/issues/6484)

### v2020.05.28-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.26-2...v2020.05.28-1)

* Deluge: Also set completed path and move_completed paramter to override client defaults. Fixes [#6474](https://github.com/SickChill/SickChill/issues/6474)
* Update included tmdbsimple
* Bump tmdbsimple from 2.2.5 to 2.2.6 ([#6473](https://github.com/SickChill/SickChill/issues/6473))
* Catch error preventing show from loading from the database if imdb cannot be reached. Fixes [#6481](https://github.com/SickChill/SickChill/issues/6481)

### v2020.05.26-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.26-1...v2020.05.26-2)

* Fix build

### v2020.05.26-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.25-1...v2020.05.26-1)

* Fixes iptorrents, and automagically parse the login form from the login page. Fixes [#6472](https://github.com/SickChill/SickChill/issues/6472)
* Merge pull request [#6471](https://github.com/SickChill/SickChill/issues/6471) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.5

### v2020.05.25-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.23-5...v2020.05.25-1)

* Fix library update on emby Fixes [#6469](https://github.com/SickChill/SickChill/issues/6469)

### v2020.05.23-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.23-4...v2020.05.23-5)

* Fix show refresh after a show update happens. It was being blocked because the update was still being performed Fixes [#6417](https://github.com/SickChill/SickChill/issues/6417)

### v2020.05.23-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.23-3...v2020.05.23-4)

* Fix build

### v2020.05.23-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.23-2...v2020.05.23-3)

* Update episode nfo's when update, force refresh, post process, etc. Fixes [#6468](https://github.com/SickChill/SickChill/issues/6468)

### v2020.05.23-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.23-1...v2020.05.23-2)

* Put a try block around set attributes in refine_video, so we can see what fails. Fixes [#6465](https://github.com/SickChill/SickChill/issues/6465)

### v2020.05.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.19-1...v2020.05.23-1)

* Merge branch 'master' into develop
* Not sure why this is indented in pypi but not github, mistake somewhere in the release maybe. Fixes [#6467](https://github.com/SickChill/SickChill/issues/6467)
* Update libs
* Py35 fixes
* Merge pull request [#6462](https://github.com/SickChill/SickChill/issues/6462) from SickChill/dependabot/pip/develop/httplib2-0.18.1
* Merge pull request [#6460](https://github.com/SickChill/SickChill/issues/6460) from SickChill/dependabot/pip/develop/httplib2-0.18.0
* Merge pull request [#6456](https://github.com/SickChill/SickChill/issues/6456) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.2
* Merge pull request [#6455](https://github.com/SickChill/SickChill/issues/6455) from SickChill/dependabot/pip/develop/httplib2-0.17.4
* Merge pull request [#6452](https://github.com/SickChill/SickChill/issues/6452) from SickChill/dependabot/pip/develop/tmdbsimple-2.2.1

### v2020.05.19-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.17-1...v2020.05.19-1)

* Merge branch 'develop'

### v2020.05.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.16-4...v2020.05.17-1)

* Merge branch 'develop'

### v2020.05.16-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.16-3...v2020.05.16-4)

* Merge branch 'develop'

### v2020.05.16-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.16-2...v2020.05.16-3)

* Merge branch 'develop'

### v2020.05.16-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.16-1...v2020.05.16-2)

* Merge branch 'develop'

### v2020.05.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-6...v2020.05.16-1)

* Merge branch 'develop'

### v2020.05.15-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-5...v2020.05.15-6)

* Merge branch 'develop'

### v2020.05.15-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-4...v2020.05.15-5)

* Merge branch 'develop'

### v2020.05.15-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-3...v2020.05.15-4)

* Merge branch 'develop'

### v2020.05.15-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-2...v2020.05.15-3)

* Merge branch 'develop'

### v2020.05.15-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.15-1...v2020.05.15-2)

* Merge branch 'develop'

### v2020.05.15-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.14-1...v2020.05.15-1)

* Merge branch 'develop'

### v2020.05.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.13-2...v2020.05.14-1)

* Merge branch 'develop'

### v2020.05.13-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.13-1...v2020.05.13-2)

* Merge branch 'develop'

### v2020.05.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.12-3...v2020.05.13-1)

* Merge branch 'develop'
* fix: requirements.txt to reduce vulnerabilities ([#6424](https://github.com/SickChill/SickChill/issues/6424))

### v2020.05.12-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.12-2...v2020.05.12-3)

* See if this helps cfshit

### v2020.05.12-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.12-1...v2020.05.12-2)

* Allow shows to be refreshed en-mass from mass update even if they are paused. Fixes [#6419](https://github.com/SickChill/SickChill/issues/6419)

### v2020.05.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.08-4...v2020.05.12-1)

* Fix mistake in emby code. Fixes [#6418](https://github.com/SickChill/SickChill/issues/6418)
* Fix exception when downloading subtitles Fixes [#6421](https://github.com/SickChill/SickChill/issues/6421) Fix error when removing shows and show dir does not exist
* Merge pull request [#6410](https://github.com/SickChill/SickChill/issues/6410) from SickChill/dependabot/pip/develop/validators-0.15.0

### v2020.05.08-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.08-3...v2020.05.08-4)

* Dont skip refresh on ended shows Fixes [#6355](https://github.com/SickChill/SickChill/issues/6355)

### v2020.05.08-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.08-2...v2020.05.08-3)

* Add back missing send2trash library Fixes [#6356](https://github.com/SickChill/SickChill/issues/6356)

### v2020.05.08-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.08-1...v2020.05.08-2)

* Add some network images Fixes [#6346](https://github.com/SickChill/SickChill/issues/6346)

### v2020.05.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.07-3...v2020.05.08-1)

* Fix build
* Remove accidentally added shared objects from libs
* Use the SC Cache dir for imdbpie, hopefully fixing the issue of adding shows for some people. Fail gracefully if we cannot get IMDB info Fixes [#6350](https://github.com/SickChill/SickChill/issues/6350) Fixes [#6370](https://github.com/SickChill/SickChill/issues/6370)
* Remove hachoir completely, use imagesize_py to guess image aspect ratio, use rtorrent9.lib.torrentparser.NewTorrentParser to verify torrent file downloads
* Update libs per new requirements.txt and fix imports for new subliminal

### v2020.05.07-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.07-2...v2020.05.07-3)

* Allow specifying http/https in the empy host, while maintaining previous functionality. Also, In the future a special host with path can be specified with a starting !, such as !https://localhost:5555/path/to/api Fixes [#6351](https://github.com/SickChill/SickChill/issues/6351)
* Fix error testing kodi notifications when specifying port. Fixes [#6358](https://github.com/SickChill/SickChill/issues/6358)
* Fixes [#6375](https://github.com/SickChill/SickChill/issues/6375) - Update filelist provider url

### v2020.05.07-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.07-1...v2020.05.07-2)

* Revert "Update Dockerfile"

### v2020.05.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.05.03-1...v2020.05.07-1)

* New Crowdin translations ([#6365](https://github.com/SickChill/SickChill/issues/6365))
* Bump subliminal from 2.0.5 to 2.1.0 ([#6373](https://github.com/SickChill/SickChill/issues/6373))
* Bump cloudscraper from 1.2.34 to 1.2.36 ([#6374](https://github.com/SickChill/SickChill/issues/6374))
* Revert "Docker permissions ([#6081](https://github.com/SickChill/SickChill/issues/6081))" ([#6406](https://github.com/SickChill/SickChill/issues/6406))
* Merge pull request [#6378](https://github.com/SickChill/SickChill/issues/6378) from nopoz/deluge

### v2020.05.03-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.28-3...v2020.05.03-1)

* Fix bug when TVDB returns 0 or -1 for airdate -.- Disable log line that people confuse for an error.
* New translations messages.pot (French) ([#6349](https://github.com/SickChill/SickChill/issues/6349))

### v2020.04.28-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.28-2...v2020.04.28-3)

* isort to fix build

### v2020.04.28-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.28-1...v2020.04.28-2)

* Fix some issues with getting tvdb favorites

### v2020.04.28-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.27-2...v2020.04.28-1)

* Basic feature implementation to add shows from tvdb favorites list. Adds with default set show options User key is on https://thetvdb.com/dashboard/account/editinfo Fixes [#6334](https://github.com/SickChill/SickChill/issues/6334)

### v2020.04.27-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.27-1...v2020.04.27-2)

* Add BBC iPlayer network image Fixes [#6337](https://github.com/SickChill/SickChill/issues/6337)

### v2020.04.27-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-9...v2020.04.27-1)

* Undo default hidden seasons for now. Fixes [#6333](https://github.com/SickChill/SickChill/issues/6333)

### v2020.04.25-9

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-8...v2020.04.25-9)

* Improve sorting by completeion percentage. Fixes [#6330](https://github.com/SickChill/SickChill/issues/6330)

### v2020.04.25-8

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-7...v2020.04.25-8)

* Fix error getting imdb info  when a show has a "World Wide" title Fixes [#6329](https://github.com/SickChill/SickChill/issues/6329) Fixes [#6327](https://github.com/SickChill/SickChill/issues/6327)

### v2020.04.25-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-6...v2020.04.25-7)

* Missed record

### v2020.04.25-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-5...v2020.04.25-6)

* Fix error getting imdb info that was causing problems adding some shows Fixes [#6329](https://github.com/SickChill/SickChill/issues/6329) Fixes [#6327](https://github.com/SickChill/SickChill/issues/6327)

### v2020.04.25-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-4...v2020.04.25-5)

* Fix error when show airdate is missing entirely Fixes [#6304](https://github.com/SickChill/SickChill/issues/6304)

### v2020.04.25-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-3...v2020.04.25-4)

* Fix build by sorting imports

### v2020.04.25-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-2...v2020.04.25-3)

* Fix exception in tpb tracker if a user has a broken js2py

### v2020.04.25-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.25-1...v2020.04.25-2)

* Fix KeyError: region in imdb code

### v2020.04.25-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.24-3...v2020.04.25-1)

* Missed reference to imdbpy exceptions
* Fix missed import removal
* Use imdbpie instead of imdbpy, because it does not rely on c-extensions/lxml/sqlalchemy Fixes [#6264](https://github.com/SickChill/SickChill/issues/6264) [#6254](https://github.com/SickChill/SickChill/issues/6254) [#6239](https://github.com/SickChill/SickChill/issues/6239) [#6322](https://github.com/SickChill/SickChill/issues/6322)

### v2020.04.24-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.24-2...v2020.04.24-3)

* Fix build

### v2020.04.24-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.24-1...v2020.04.24-2)

* Fix error when a show is not completely populated in the database, causing a rendering error Fixes [#6304](https://github.com/SickChill/SickChill/issues/6304)

### v2020.04.24-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-8...v2020.04.24-1)

* Fix fake useragent pool creation when a user starts SC before network is up. Fixes [#6314](https://github.com/SickChill/SickChill/issues/6314)
* New Crowdin translations ([#6311](https://github.com/SickChill/SickChill/issues/6311))

### v2020.04.23-8

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-7...v2020.04.23-8)

* Fix issue with kodi notifier always doing full library update when show name has a space in it, and not honoring settings Fixes [#6306](https://github.com/SickChill/SickChill/issues/6306)

### v2020.04.23-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-6...v2020.04.23-7)

* Fix displaying more than one entry for related episodes on Preview Rename Fixes [#6307](https://github.com/SickChill/SickChill/issues/6307)

### v2020.04.23-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-5...v2020.04.23-6)

* Fix another one of the errors in imdbpy

### v2020.04.23-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-4...v2020.04.23-5)

* Fix one of the errors in imdbpy

### v2020.04.23-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-3...v2020.04.23-4)

* Update cloudscraper and httplib2
* Bump cloudscraper from 1.2.33 to 1.2.34 ([#6303](https://github.com/SickChill/SickChill/issues/6303))
* Bump httplib2 from 0.17.2 to 0.17.3 ([#6302](https://github.com/SickChill/SickChill/issues/6302))

### v2020.04.23-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-2...v2020.04.23-3)

* Fix hiding season headers when filtering episodes on the show page. Fixes [#6259](https://github.com/SickChill/SickChill/issues/6259)
* New translations messages.pot (French) ([#6292](https://github.com/SickChill/SickChill/issues/6292))

### v2020.04.23-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.23-1...v2020.04.23-2)

* Fix error with js updating text on adding existing shows. Fixes [#6265](https://github.com/SickChill/SickChill/issues/6265)

### v2020.04.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.22-4...v2020.04.23-1)

* Fix error getting episode. Fixes [#6297](https://github.com/SickChill/SickChill/issues/6297)

### v2020.04.22-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.22-3...v2020.04.22-4)

* Fix mistake

### v2020.04.22-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.22-2...v2020.04.22-3)

* New Crowdin translations ([#6263](https://github.com/SickChill/SickChill/issues/6263))
* Revert to using name parser over guessit for the release groups Fixes [#6268](https://github.com/SickChill/SickChill/issues/6268)
* Fix growl.py for GNTP 1.0.3 update ([#6267](https://github.com/SickChill/SickChill/issues/6267))

### v2020.04.22-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.22-1...v2020.04.22-2)

* Merge branch 'develop'
* Update Crowdin configuration file

### v2020.04.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.21-4...v2020.04.22-1)

* Avoid error when apibay is failing to return results. Fixes [#2614](https://github.com/SickChill/SickChill/issues/2614) Fixes [#6256](https://github.com/SickChill/SickChill/issues/6256)

### v2020.04.21-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.21-3...v2020.04.21-4)

* Try to improve Preview Rename speed and memory usage. Might not help much Fixes [#5984](https://github.com/SickChill/SickChill/issues/5984)

### v2020.04.21-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.21-2...v2020.04.21-3)

* Fix Greetings
* Fix build

### v2020.04.21-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.21-1...v2020.04.21-2)

* Try a new slick way to change root dirs when a user moves their library from  windows to linux or vice versa and does a massEdit to change the root. Fixes [#6249](https://github.com/SickChill/SickChill/issues/6249) (I hope)

### v2020.04.21-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-8...v2020.04.21-1)

* Make rescan on show page into a force refresh, so people can refresh ended/paused shows manually.

### v2020.04.20-8

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-7...v2020.04.20-8)

* Fix adba for anidb errors. Fixes [#6244](https://github.com/SickChill/SickChill/issues/6244)

### v2020.04.20-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-6...v2020.04.20-7)

* Set airdates to Never for wanted/unaired/unknown episodes that no longer have an airdate on TVDB, without deleting them Minor datetime cleanup

### v2020.04.20-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-5...v2020.04.20-6)

* Update/remove broken links and images from the readme

### v2020.04.20-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-4...v2020.04.20-5)

* Always collapse if  show has more than one season, show at most the most recent 3 seasons expanded by default Fixes slow load for large shows Fixes [#6179](https://github.com/SickChill/SickChill/issues/6179)

### v2020.04.20-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-3...v2020.04.20-4)

* Prevent show episodes from being deleted when tvdb does not answer Fixes [#6176](https://github.com/SickChill/SickChill/issues/6176) Fixes [#6091](https://github.com/SickChill/SickChill/issues/6091)

### v2020.04.20-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-2...v2020.04.20-3)

* Fix mistake in lib cleaner code.

### v2020.04.20-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.20-1...v2020.04.20-2)

* Fix sorting by number of downloads on home page Fixes [#4978](https://github.com/SickChill/SickChill/issues/4978)

### v2020.04.20-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-9...v2020.04.20-1)

* Fix issue re-testing email notifications after save and page reload due to passwords being masked in the loaded page. Fixes [#4943](https://github.com/SickChill/SickChill/issues/4943)
* Fix build
* Seems to fix issues with post processor sometimes not processing files. Unknown why yet. Fixes [#6215](https://github.com/SickChill/SickChill/issues/6215)

### v2020.04.19-9

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-8...v2020.04.19-9)

* Fixes renamer not moving associated files when MOVE_ASSOCIATED_FILES is disabled in the post processor settings. Fixes [#6191](https://github.com/SickChill/SickChill/issues/6191)

### v2020.04.19-8

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-7...v2020.04.19-8)

* Js2Py does not work on Python less than 2.7.9 - Disable grabbing tpb provided trackers and only use custom_trackers if this is the case This will disable the provider if you do not have python 2.7.9 OR set custom trackers in config/search on the torrent tab. Fixes [#6236](https://github.com/SickChill/SickChill/issues/6236)
* Remove pyc and empty folders from libs when SC updates. Hopefully this prevents [#6230](https://github.com/SickChill/SickChill/issues/6230) in the future
* Fix missed coding change in tvdb handler Fixes [#6190](https://github.com/SickChill/SickChill/issues/6190)

### v2020.04.19-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-6...v2020.04.19-7)

* Fix KeyError with imdb_info on show page Fixes [#6227](https://github.com/SickChill/SickChill/issues/6227)

### v2020.04.19-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-5...v2020.04.19-6)

* Fix imports for rtorrent

### v2020.04.19-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-4...v2020.04.19-5)

* Remove extensions
* Add more libs back

### v2020.04.19-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-3...v2020.04.19-4)

* Add synchronousdeluge dirty

### v2020.04.19-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-2...v2020.04.19-3)

* Add more libs back

### v2020.04.19-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-10...v2020.04.19-2)

* Do not download propers for paused shows. Fixes [#6210](https://github.com/SickChill/SickChill/issues/6210)

### v2020.04.19-10

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.19-1...v2020.04.19-10)

* Fix build
* Seems to fix issues with post processor sometimes not processing files. Unknown why yet. Fixes [#6215](https://github.com/SickChill/SickChill/issues/6215)

### v2020.04.19-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.18-3...v2020.04.19-1)

* Update imdbpy to IMDbPY-6.9.dev20200419 (fixes etree issue, hopefully), Add certgen from pyopenssl example to create certs
* Rework libs and enable fanart.tv for images Updates python-fanart Fixes lib dir to be 100% vanilla, moved adba and trakt to root for now Replaced growl lib with gntp Replaced python-fanart with python3-fanart
* Fix adding from imdbpopular
* Update translations (build 11159) [skip ci]

### v2020.04.18-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.18-2...v2020.04.18-3)

* Remove lxml - pip install lxml manually if you have issues related to elementree/etree/lxml
* Update thepiratebay to use API. Fixes [#6195](https://github.com/SickChill/SickChill/issues/6195)
* Update translations (build 11156) [skip ci]

### v2020.04.18-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.18-1...v2020.04.18-2)

* Update libs, need to figure out issue with binaries
* Update translations (build 11152) [skip ci]

### v2020.04.18-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.01-2...v2020.04.18-1)

* Bump httplib2 from 0.17.1 to 0.17.2 ([#6197](https://github.com/SickChill/SickChill/issues/6197))
* Bump twilio from 6.38.0 to 6.38.1 ([#6202](https://github.com/SickChill/SickChill/issues/6202))
* Workaround for SickChill[#6199](https://github.com/SickChill/SickChill/issues/6199) to support RFC 4007 IPv6 Scoped Literal Addresses in remote_ip ([#6201](https://github.com/SickChill/SickChill/issues/6201))
* Update yarn packages, add missed requirements commit
* Update subliminal, sqlalchemy, dogpile.cache
* Tornado to 4.5.3 (5.0 breaks SC for unknown reason)
* Update libs based on requirements. Pin Tornado to 4.5
* Bump putio-py from 8.6.0 to 8.6.2 ([#6173](https://github.com/SickChill/SickChill/issues/6173))
* Bump beautifulsoup4 from 4.8.2 to 4.9.0 ([#6174](https://github.com/SickChill/SickChill/issues/6174))
* Bump certifi from 2019.11.28 to 2020.4.5.1 ([#6175](https://github.com/SickChill/SickChill/issues/6175))
* Add BSPlayer subtitle provider ([#6177](https://github.com/SickChill/SickChill/issues/6177))
* Bump httplib2 from 0.17.0 to 0.17.1 ([#6170](https://github.com/SickChill/SickChill/issues/6170))
* Bump tus-py from 1.2.0 to 1.3.4 ([#6165](https://github.com/SickChill/SickChill/issues/6165))
* Update Dockerfile
* Bump twilio from 6.37.0 to 6.38.0 ([#6166](https://github.com/SickChill/SickChill/issues/6166))
* Docker permissions ([#6081](https://github.com/SickChill/SickChill/issues/6081))
* Update translations (build 11109) [skip ci]

### v2020.04.01-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.04.01-1...v2020.04.01-2)

* Fixes [#6138](https://github.com/SickChill/SickChill/issues/6138) - API::sb.searchtvdb error
* Update translations (build 11107) [skip ci]

### v2020.04.01-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.15-1...v2020.04.01-1)

* Fix issue where user cannot add a scene exception for the latest season of a show. Fix issue of Season torrents that are tried to be splitted when snatched through torznab
* Bump beautifulsoup4 from 4.5.3 to 4.8.2 ([#6145](https://github.com/SickChill/SickChill/issues/6145))
* Bump httplib2 from 0.9.2 to 0.17.0 ([#6146](https://github.com/SickChill/SickChill/issues/6146))
* Bump pytz from 2019.1 to 2019.3 ([#6147](https://github.com/SickChill/SickChill/issues/6147))
* Bump pymediainfo from 2.0 to 4.1 ([#6148](https://github.com/SickChill/SickChill/issues/6148))
* Bump tzlocal from 1.4 to 2.0.0 ([#6149](https://github.com/SickChill/SickChill/issues/6149))
* Bump ndg-httpsclient from 0.3.3 to 0.5.1 ([#6150](https://github.com/SickChill/SickChill/issues/6150))
* Bump xmltodict from 0.11.0 to 0.12.0 ([#6151](https://github.com/SickChill/SickChill/issues/6151))
* Bump pysrt from 1.1.1 to 1.1.2 ([#6152](https://github.com/SickChill/SickChill/issues/6152))
* Bump fake-useragent from 0.1.2 to 0.1.11 ([#6153](https://github.com/SickChill/SickChill/issues/6153))
* Bump mako from 1.0.12 to 1.1.2 ([#6154](https://github.com/SickChill/SickChill/issues/6154))
* Bump profilehooks from 1.5 to 1.11.2 ([#6139](https://github.com/SickChill/SickChill/issues/6139))
* Bump validators from 0.10 to 0.14.2 ([#6140](https://github.com/SickChill/SickChill/issues/6140))
* Bump idna from 2.5 to 2.9 ([#6141](https://github.com/SickChill/SickChill/issues/6141))
* Bump futures from 3.1.1 to 3.3.0 ([#6142](https://github.com/SickChill/SickChill/issues/6142))
* Bump markdown2 from 2.3.6 to 2.3.8 ([#6143](https://github.com/SickChill/SickChill/issues/6143))
* Bump pyjwt from 1.5.0 to 1.7.1 ([#6127](https://github.com/SickChill/SickChill/issues/6127))
* Bump unidecode from 0.04.21 to 1.1.1 ([#6128](https://github.com/SickChill/SickChill/issues/6128))
* Bump twilio from 6.36.0 to 6.37.0 ([#6129](https://github.com/SickChill/SickChill/issues/6129))
* Bump enum34 from 1.0.4 to 1.1.10 ([#6131](https://github.com/SickChill/SickChill/issues/6131))
* Bump backports-ssl-match-hostname from 3.5.0.1 to 3.7.0.1 ([#6130](https://github.com/SickChill/SickChill/issues/6130))
* Bump certifi from 2017.4.17 to 2019.11.28 ([#6116](https://github.com/SickChill/SickChill/issues/6116))
* Bump decorator from 4.0.10 to 4.4.2 ([#6117](https://github.com/SickChill/SickChill/issues/6117))
* Bump pygithub from 1.34 to 1.45 ([#6118](https://github.com/SickChill/SickChill/issues/6118))
* Bump putio-py from 6.1.0 to 8.6.0 ([#6119](https://github.com/SickChill/SickChill/issues/6119))
* Bump python-dateutil from 2.8.0 to 2.8.1 ([#6120](https://github.com/SickChill/SickChill/issues/6120))
* Bump six from 1.12.0 to 1.14.0 ([#6122](https://github.com/SickChill/SickChill/issues/6122))
* Bump pysocks from 1.6.7 to 1.7.1 ([#6123](https://github.com/SickChill/SickChill/issues/6123))
* Bump oauthlib from 2.0.2 to 3.1.0 ([#6124](https://github.com/SickChill/SickChill/issues/6124))
* Bump guessit from 3.0.4 to 3.1.0 ([#6125](https://github.com/SickChill/SickChill/issues/6125))
* Bump configobj from 4.6.0 to 5.0.6 ([#6126](https://github.com/SickChill/SickChill/issues/6126))
[Security] Bump markdown2 from 2.3.4 to 2.3.6 ([#6110](https://github.com/SickChill/SickChill/issues/6110))
* Bump html5lib from 1.0b10 to 1.0.1 ([#6111](https://github.com/SickChill/SickChill/issues/6111))
* Bump stevedore from 1.10.0 to 1.32.0 ([#6112](https://github.com/SickChill/SickChill/issues/6112))
* Bump tmdbsimple from 0.3.0 to 2.2.0 ([#6113](https://github.com/SickChill/SickChill/issues/6113))
* Bump requests-oauthlib from 0.8.0 to 1.3.0 ([#6114](https://github.com/SickChill/SickChill/issues/6114))
* Update translations (build 10991) [skip ci]

### v2020.03.15-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-6...v2020.03.15-1)

* Sleep 3 seconds in between requests to xthor (2 + 1 for good measure) Fixes [#6107](https://github.com/SickChill/SickChill/issues/6107)
* Update some libs and update the docker packaging script ([#6106](https://github.com/SickChill/SickChill/issues/6106))
* Bump tornado from 4.5.1 to 5.1.1 ([#6102](https://github.com/SickChill/SickChill/issues/6102))
* Bump cachecontrol from 0.11.5 to 0.12.6 ([#6101](https://github.com/SickChill/SickChill/issues/6101))
* Bump rebulk from 1.0.0 to 2.0.0 ([#6103](https://github.com/SickChill/SickChill/issues/6103))
* Bump twilio from 5.7.0 to 6.36.0 ([#6104](https://github.com/SickChill/SickChill/issues/6104))
* Bump python-twitter from 3.3 to 3.5 ([#6105](https://github.com/SickChill/SickChill/issues/6105))
* Update translations (build 10956) [skip ci]

### v2020.03.13-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-5...v2020.03.13-6)

* Merge branch 'develop'
* Update translations (build 10948) [skip ci]

### v2020.03.13-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-4...v2020.03.13-5)

* Update build
* Update translations (build 10946) [skip ci]

### v2020.03.13-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-3...v2020.03.13-4)

* Update build
* Update translations (build 10943) [skip ci]

### v2020.03.13-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-2...v2020.03.13-3)

* Typo space

### v2020.03.13-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.13-1...v2020.03.13-2)

* Update greetings so it doesnt build unless an issue or pr was opened
* Update translations (build 10936) [skip ci]

### v2020.03.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.12-1...v2020.03.13-1)

* Test SC and build multiarch (linux/amd64,linux/arm/v6,linux/arm/v7,linux/arm64,linux/386,linux/ppc64le,linux/s390x) docker images with buildx through github workflow
* Update translations (build 10933) [skip ci]

### v2020.03.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.10-2...v2020.03.12-1)

* Change API key for TVDB. https://thetvdb.com
* Update translations (build 10881) [skip ci]

### v2020.03.10-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.10-1...v2020.03.10-2)

* Add amazon (japan) logo Fixes [#6035](https://github.com/SickChill/SickChill/issues/6035)
* Update translations (build 10879) [skip ci]

### v2020.03.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.08-4...v2020.03.10-1)

* Add '-xpost' to removeWords Fixes [#6079](https://github.com/SickChill/SickChill/issues/6079)
* Update translations (build 10863) [skip ci]

### v2020.03.08-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.08-3...v2020.03.08-4)

* Typo

### v2020.03.08-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.08-2...v2020.03.08-3)

* Create pythonpackage.yml ([#6077](https://github.com/SickChill/SickChill/issues/6077))
* Update translations (build 10853) [skip ci]

### v2020.03.08-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.08-1...v2020.03.08-2)

* Temporary solution for bower warning. TODO: Get rid of bower entirely.
* Update translations (build 10850) [skip ci]

### v2020.03.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.07-4...v2020.03.08-1)

* Add yaml for issue bot
* Update translations (build 10847) [skip ci]

### v2020.03.07-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.07-3...v2020.03.07-4)

* Fixes [#6069](https://github.com/SickChill/SickChill/issues/6069)
* Update translations (build 10844) [skip ci]

### v2020.03.07-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.07-2...v2020.03.07-3)

* Lets see if TVDB fixed their updates api. Starts at today and gets the last 7 days first rather than last update time in case limits are hit, and always updates the last 7 days.
* Update translations (build 10841) [skip ci]

### v2020.03.07-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.07-1...v2020.03.07-2)

* Fix branch list in config
* Update translations (build 10839) [skip ci]

### v2020.03.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.03.02-1...v2020.03.07-1)

* fix login when rev proxy has auth basic ([#6070](https://github.com/SickChill/SickChill/issues/6070))
* Update translations (build 10834) [skip ci]

### v2020.03.02-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.27-2...v2020.03.02-1)

* Check if queueing is enabled in qbittorrent before trying to set priority. Fixes [#5980](https://github.com/SickChill/SickChill/issues/5980)
* Update translations (build 10832) [skip ci]

### v2020.02.27-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.27-1...v2020.02.27-2)

* Add ipaddress package Fixes [#6032](https://github.com/SickChill/SickChill/issues/6032)

### v2020.02.27-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.26-3...v2020.02.27-1)

* is_ip_private() should handle IPv6 addresses ([#6030](https://github.com/SickChill/SickChill/issues/6030))
* Update translations (build 10824) [skip ci]

### v2020.02.26-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.26-2...v2020.02.26-3)

* Make sure a failing kodi connection doesnt prevent a user from accessing displayShow
* Update translations (build 10822) [skip ci]

### v2020.02.26-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.26-1...v2020.02.26-2)

* Make sure SC still starts if user does not have cryptography, which is needed for the jwt auth.

### v2020.02.26-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-8...v2020.02.26-1)

* Implement SC login FROM Cloudflare Access using jwt token auth ([#6021](https://github.com/SickChill/SickChill/issues/6021))
* Add IPv6 loopback support to is_ip_private() ([#6024](https://github.com/SickChill/SickChill/issues/6024))
* Update translations (build 10803) [skip ci]

### v2020.02.25-8

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-7...v2020.02.25-8)

* Update cloudscraper and cfscrape. Good Luck
* Update translations (build 10801) [skip ci]

### v2020.02.25-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-6...v2020.02.25-7)

* Fix problem when using black hole and a bittorrent cache site must be used (Hundreds of No schema supplied. Perhaps you meant lines in the logs)
* Update translations (build 10798) [skip ci]

### v2020.02.25-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-5...v2020.02.25-6)

* Do not refresh shows on startup Update all shows every night until TVDB fixes their updates api
* Update translations (build 10794) [skip ci]

### v2020.02.25-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-4...v2020.02.25-5)

* Oops, this allowed Bearer : as authorization if the user had no user/pass set. Also return false if incorrect header is present.
* Update translations (build 10791) [skip ci]

### v2020.02.25-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-3...v2020.02.25-4)

* Change value of port to an int when port is passed in KODI_HOST.
* Update translations (build 10788) [skip ci]

### v2020.02.25-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-2...v2020.02.25-3)

* Allow basic auth to bypass login (for reverse proxies, unsecure if used outside of a local network!) Fixes [#6018](https://github.com/SickChill/SickChill/issues/6018)
* Update translations (build 10784) [skip ci]

### v2020.02.25-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.25-1...v2020.02.25-2)

* Link cache data ([#6014](https://github.com/SickChill/SickChill/issues/6014))

### v2020.02.25-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.24-3...v2020.02.25-1)

* Improve login code from remote, log the access attempt if the error page was shown.
* Update translations (build 10774) [skip ci]

### v2020.02.24-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.24-2...v2020.02.24-3)

* Adjust code for login page
* Update translations (build 10769) [skip ci]

### v2020.02.24-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.24-1...v2020.02.24-2)

* Force users to set a username and password if accessible from the internet, or block the con
* Update translations (build 10765) [skip ci]

### v2020.02.24-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.23-2...v2020.02.24-1)

* Try to fix itorrents error with skytorrents and limetorrents Fixes [#6012](https://github.com/SickChill/SickChill/issues/6012) Fixes [#5942](https://github.com/SickChill/SickChill/issues/5942)
* Fixes [#5108](https://github.com/SickChill/SickChill/issues/5108)
* Update translations (build 10749) [skip ci]

### v2020.02.23-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.23-1...v2020.02.23-2)

* New limetorrents url
* Update translations (build 10745) [skip ci]

### v2020.02.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.22-1...v2020.02.23-1)

* Upgrade requests, idna
* Update tvdb series/poster/banner/fanart/season images ordering to get the most popular images when adding
* Update translations (build 10743) [skip ci]

### v2020.02.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.15-3...v2020.02.22-1)

* Hide kodi play button when kodi is not enabled and prevent the modal from causing an exception Fixes [#5990](https://github.com/SickChill/SickChill/issues/5990)
* Network Logos - Duplicate Chiba TV for "CTC (JA)" network ([#6001](https://github.com/SickChill/SickChill/issues/6001))
* Network logo - Add CraveTV ([#5997](https://github.com/SickChill/SickChill/issues/5997))
* Update translations (build 10736) [skip ci]

### v2020.02.15-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.15-2...v2020.02.15-3)

* Fall back to english for series images if the show has a non-english language and the language-specific image is not found. Fixes [#5979](https://github.com/SickChill/SickChill/issues/5979)
* Option to restrict backlog searches to 'missing' episodes only ([#5977](https://github.com/SickChill/SickChill/issues/5977))
* Update translations (build 10730) [skip ci]

### v2020.02.15-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.15-1...v2020.02.15-2)

* Fix [#5981](https://github.com/SickChill/SickChill/issues/5981) - Kodi notifications if you put the port on the settings line. via kyuuk (thanks) [untested]
* Update translations (build 10726) [skip ci]

### v2020.02.15-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.11-3...v2020.02.15-1)

* iSort and fix build. Disable demonoid rss search until I can finish it.
* Force cache dir to be in gui/slick/cache and remove setting. Force Log dir to be in data_dir/Logs and remove setting Add demonoid and kat providers
* Update translations (build 10721) [skip ci]

### v2020.02.11-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.11-2...v2020.02.11-3)

* Only run rarbg test manually

### v2020.02.11-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.11-1...v2020.02.11-2)

* Use rarbg for search test, as it is one of our most reliable providers
* Fixes [#5972](https://github.com/SickChill/SickChill/issues/5972) - mede8er xml not being created Fixes [#5962](https://github.com/SickChill/SickChill/issues/5962) - Rating tag set to mpp rating rather than site rating
* Update translations (build 10715) [skip ci]

### v2020.02.11-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.09-3...v2020.02.11-1)

* Hide debug logging about items/images not found on tvdb
* Update translations (build 10711) [skip ci]

### v2020.02.09-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.09-2...v2020.02.09-3)

* Fixes [#5964](https://github.com/SickChill/SickChill/issues/5964) - Mistake
* Fixes [#5964](https://github.com/SickChill/SickChill/issues/5964)
* Update translations (build 10707) [skip ci]

### v2020.02.09-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.09-1...v2020.02.09-2)

* Temp fix for image_url so it doesnt error everyone
* Update translations (build 10705) [skip ci]

### v2020.02.09-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.05-2...v2020.02.09-1)

* Fixes [#5963](https://github.com/SickChill/SickChill/issues/5963)
* Fix reverse parsing scene names, and possibly match scene releases better as well as when re-adding already-renamed show folders.
* Add ability to play file on kodi over api in the notifier, remove old kodi notifier code ([#5938](https://github.com/SickChill/SickChill/issues/5938))
* Fix image cache, only works if cache dir is inside gui dir ([#5961](https://github.com/SickChill/SickChill/issues/5961))
* Update translations (build 10687) [skip ci]

### v2020.02.05-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.05-1...v2020.02.05-2)

* Fix build

### v2020.02.05-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.02-2...v2020.02.05-1)

* Force show updater to run on startup. Fix error where last_update was always set so older shows never updated. Get all show updates if not updated before rather than just 6 months in the past (older shows) Fix episodeguide in kodi nfo's and a logging bug
* Update translations (build 10681) [skip ci]

### v2020.02.02-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.02.02-1...v2020.02.02-2)

* Fix build

### v2020.02.02-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.29-4...v2020.02.02-1)

* Let's catch tvdbapi exceptions better
* Update translations (build 10675) [skip ci]

### v2020.01.29-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.29-3...v2020.01.29-4)

* Update cloudscraper and urllib3
* Update translations (build 10672) [skip ci]

### v2020.01.29-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.29-2...v2020.01.29-3)

* Fix error when adding show by tvdbid
* Update translations (build 10669) [skip ci]

### v2020.01.29-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.29-1...v2020.01.29-2)

* Add status as a sorting option on poster view. Sort better when loading page on poster view for next episode
* Do not cache posters, thumbs, banners, network logos until cachebreaking can be worked in or cache and gui can be combined for staticfiles.
* Update translations (build 10666) [skip ci]

### v2020.01.29-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.25-1...v2020.01.29-1)

* Fix ebuild
* Fix error when a show is added by the trakt checker
* Fixes [#5944](https://github.com/SickChill/SickChill/issues/5944) - Sorting posters by next episode
* Fixes [#5944](https://github.com/SickChill/SickChill/issues/5944) - Sorting posters by next episode
* Update translations (build 10650) [skip ci]

### v2020.01.25-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.24-1...v2020.01.25-1)

* Fixes [#5923](https://github.com/SickChill/SickChill/issues/5923)
* Update translations (build 10647) [skip ci]

### v2020.01.24-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.23-2...v2020.01.24-1)

* Fix apibuilder syntax error Fixes [#5922](https://github.com/SickChill/SickChill/issues/5922)

### v2020.01.23-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.23-1...v2020.01.23-2)

* Fix build
* Ability to sort the search results when adding a show. Click the table headers Fixes [#5917](https://github.com/SickChill/SickChill/issues/5917)

### v2020.01.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.21-1...v2020.01.23-1)

* Allow searching with imdbid (tt6546758 or 6546758 will bring up schooled) Do not delete episode if tvdb fails. Keep the data we have. [#5915](https://github.com/SickChill/SickChill/issues/5915) [#5912](https://github.com/SickChill/SickChill/issues/5912)
* Ability to append year to end of show dirs when adding shows. ([#5912](https://github.com/SickChill/SickChill/issues/5912))

### v2020.01.21-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.20-5...v2020.01.21-1)

* Force add 5090 to default nzb provider categories when HEVC is enabled. Fix being able to edit builtin nzb providers settings (on the Configure Custom Newznab Providers page)
* Don't warn when filling cache with show images and the show dir doesnt exist
* Fix footer rowspan on schedule and add trakt link to schedule poster and list layouts
* Use personal access tokens only for submitting issues (new github policy) ([#5909](https://github.com/SickChill/SickChill/issues/5909))

### v2020.01.20-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.20-4...v2020.01.20-5)

* Always include the show's all-season scene exception in search string, even if it has a season specific scene exception Fixes [#4974](https://github.com/SickChill/SickChill/issues/4974)

### v2020.01.20-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.20-3...v2020.01.20-4)

* Fix not being able to add scene season exceptions for most recent season of a show Fixes [#5905](https://github.com/SickChill/SickChill/issues/5905)

### v2020.01.20-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.20-2...v2020.01.20-3)

* Disable vcr for skytorrents, cloudflare breaking tests
* Fix parsing skytorrents
* Update requirements.txt (this file is NOT USED) Fixes [#5316](https://github.com/SickChill/SickChill/issues/5316)

### v2020.01.20-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.20-1...v2020.01.20-2)

* Fix skytorrents Fixes [#5579](https://github.com/SickChill/SickChill/issues/5579)

### v2020.01.20-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-7...v2020.01.20-1)

* Clean up some logs with proper thread names and make all missing networks go to the same issue
* Update isotope and dependancies. Try to fix empty space problem. Fixes [#5724](https://github.com/SickChill/SickChill/issues/5724)

### v2020.01.19-7

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-6...v2020.01.19-7)

* Don't error if show doesn't have any episodes

### v2020.01.19-6

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-5...v2020.01.19-6)

* Allow adding shows from the future with no episodes yet Fixes [#5588](https://github.com/SickChill/SickChill/issues/5588)

### v2020.01.19-5

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-4...v2020.01.19-5)

* Fixes [#5899](https://github.com/SickChill/SickChill/issues/5899)

### v2020.01.19-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-3...v2020.01.19-4)

* Typo, [#5900](https://github.com/SickChill/SickChill/issues/5900)
* Add a trakt icon link to the show page ([#5896](https://github.com/SickChill/SickChill/issues/5896))

### v2020.01.19-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-2...v2020.01.19-3)

* Only use nfo/xml when adding existing shows. Adding using the dir name to automatically search providers is unreliable. Instead, when metadata is missing, prompt to search and select the show manually

### v2020.01.19-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.19-1...v2020.01.19-2)

* Only show info log while creating kodi meta files when cannot find a show on tvdb, usually when the api is failing. Fixes [#5898](https://github.com/SickChill/SickChill/issues/5898)

### v2020.01.19-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.17-1...v2020.01.19-1)

* Allow lesser versions of python 2.7 (uses cfscrape, probably fails on many sites) Fixes [#5894](https://github.com/SickChill/SickChill/issues/5894)

### v2020.01.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.16-2...v2020.01.17-1)

* Also catch TypeError in episode_image_url when episode is not found. Fixes [#5874](https://github.com/SickChill/SickChill/issues/5874)
* Better way to check that a torrent was added in the old qbittorent client. Fixes [#5881](https://github.com/SickChill/SickChill/issues/5881) Fixes [#5016](https://github.com/SickChill/SickChill/issues/5016) Fixes [#4385](https://github.com/SickChill/SickChill/issues/4385) Thanks sumarimike

### v2020.01.16-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.16-1...v2020.01.16-2)

* Remove unnecessary api call to tvdb

### v2020.01.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.14-2...v2020.01.16-1)

* Use the correct method when loading episodes from indexer, so error handling is used. Fixes [#5879](https://github.com/SickChill/SickChill/issues/5879)
* check parent dir names in addition to current ([#5864](https://github.com/SickChill/SickChill/issues/5864))

### v2020.01.14-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.14-1...v2020.01.14-2)

* Handle regex substitution error when item to search for contains a repeat repeat such as ++ or ** Fixes [#5869](https://github.com/SickChill/SickChill/issues/5869)

### v2020.01.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.13-3...v2020.01.14-1)

* Handle adding a show when tvdb does not have it's start date. Fixes [#5867](https://github.com/SickChill/SickChill/issues/5867)

### v2020.01.13-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.13-2...v2020.01.13-3)

* Apply user supplied fix for bjshare from [#5591](https://github.com/SickChill/SickChill/issues/5591)#issuecomment-537029104 Fixes [#5591](https://github.com/SickChill/SickChill/issues/5591)

### v2020.01.13-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.13-1...v2020.01.13-2)

* Fixes [#5766](https://github.com/SickChill/SickChill/issues/5766) - Might need improved. Hides usernames/passwords if it is a full word. Also, hide jackett_apikey from logs
* Fixes [#5749](https://github.com/SickChill/SickChill/issues/5749) feature to avoid updating shows with status Ended for a set amount of days. Defaults to 7 days, configurable on config->general->interface

### v2020.01.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.12-4...v2020.01.13-1)

* Fix [#5863](https://github.com/SickChill/SickChill/issues/5863)

### v2020.01.12-4

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.12-3...v2020.01.12-4)

* Try again to fix build.

### v2020.01.12-3

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.12-2...v2020.01.12-3)

* Fix build hopefully. py3 is urgent
* Update FUNDING.yml

### v2020.01.12-2

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.12-1...v2020.01.12-2)

* Jacket url is returning a magnet when expecting a torrent file. Why not eliminate that 302 redirect and just put the magnet in the xml response instead.... Fixes [#5600](https://github.com/SickChill/SickChill/issues/5600) Fixes [#5862](https://github.com/SickChill/SickChill/issues/5862)

### v2020.01.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.11-1...v2020.01.12-1)

* Fixes [#5858](https://github.com/SickChill/SickChill/issues/5858) Fixes [#5859](https://github.com/SickChill/SickChill/issues/5859) Change rarbg url to rarbg.to

### v2020.01.11-1

[full changelog](https://github.com/SickChill/SickChill/compare/v2020.01.03-1...v2020.01.11-1)

* Update bower and eslint in yarn.lock and package.json
* Call _location instead of location for show where necessary Fix [#5836](https://github.com/SickChill/SickChill/issues/5836) when info in nfo has & included Go supersaiyan on finding correct show from nfo, indexer and id, or show name should be enough, it is working fairly well
* Create FUNDING.yml ([#5835](https://github.com/SickChill/SickChill/issues/5835))
* Fix a potentially undefined result variable
* Use cloudscraper when running 2.7.9, cfscrape when running 2.7-2.7.8
* cloudscraper requires Python 2.7.9+ but less than 3! [#5829](https://github.com/SickChill/SickChill/issues/5829)
* Use cloudscraper for now. cfscrape is borked ([#5828](https://github.com/SickChill/SickChill/issues/5828))
* Apply [Anorov/cloudflare-scrape#315](https://github.com/Anorov/cloudflare-scrape/issues/315) ([#5827](https://github.com/SickChill/SickChill/issues/5827))
* Fix error on kodi12+ metadata relating to imdb country codes. Improve search results when show is not found the first time Remove writers and directors from kodi12+ metadata (info is not on tvdb for shows, only episodes)
* Fix error  updating trakt watchlist
* Adding Parsing for WebUHD like ([#5824](https://github.com/SickChill/SickChill/issues/5824))
* Fix error on genre split in webapi Fixes [#5825](https://github.com/SickChill/SickChill/issues/5825)
* Fix error with coverage==5 breaking codecov. Fixes build
* Fix show forced update and refresh (all episodes having same or no data on displayshow)
* Fix airdates, fix mistake on mediabrowser metadata, fix the rest of metdata
* Fix failure on most metadata providers. FIXME: tvdbapi returning no airdate for some episodes, such as schooled
* Tvdb3 ([#5789](https://github.com/SickChill/SickChill/issues/5789))
* Update translations (build 10488) [skip ci]

### v2020.01.03-1

[full changelog](https://github.com/SickChill/SickChill/compare/2022.02.17...v2020.01.03-1)

* Fix error when sending a download to rtorrent9 that caused item to not be seen as snatched Fixes [#5802](https://github.com/SickChill/SickChill/issues/5802)
* Ygg have changed their URL to www2.yggtorrent.ws ([#5801](https://github.com/SickChill/SickChill/issues/5801))
* Rename Shudder icon to correct name. Fixes [#5790](https://github.com/SickChill/SickChill/issues/5790)
* Update translations (build 10420) [skip ci]

### 2022.02.17

[full changelog](https://github.com/SickChill/SickChill/compare/2022.02.16...2022.02.17)

* Merge branch 'develop'
* Merge branch 'develop'

### 2022.02.16

[full changelog](https://github.com/SickChill/SickChill/compare/2021.11.10...2022.02.16)

* Merge branch 'develop'

### 2021.11.10

[full changelog](https://github.com/SickChill/SickChill/compare/2021.11.07...2021.11.10)

* Merge branch 'develop'
* Merge branch 'develop' into master
* Update pyproject.toml ([#7645](https://github.com/SickChill/SickChill/issues/7645))
* Update pyproject.toml
* Merge branch 'develop'

### 2021.11.07

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.29...2021.11.07)

* Merge branch 'develop'
* Update stale.yml ([#7592](https://github.com/SickChill/SickChill/issues/7592))
* Bump tar from 6.1.0 to 6.1.3

### 2021.07.29

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.23-1...2021.07.29)

* Release 2021.7.29 to pypi
* Fix updater in pip mode

### 2021.07.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.23...2021.07.23-1)

* Publish 2021.7.23-1
* Try to add syno wheelhouse dir to search paths for pip

### 2021.07.23

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.22-2...2021.07.23)

* Release 2021.7.23
* Add ability to use existing venv module, try virtualenv as an alternative, and fall back to hacky pyz fail window
* Bump snyk from 1.664.0 to 1.666.0
* Bump webpack from 5.45.1 to 5.46.0
* Fix [#7147](https://github.com/SickChill/SickChill/issues/7147)

### 2021.07.22-2

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.22-1...2021.07.22-2)

* Release 2021.7.22-8
* Ignore incompatibility between xo and grunt-contrib-uglify
* Update JS

### 2021.07.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.22...2021.07.22-1)

* Fix tagging on release
* Release 2021.7.22-5
* Remove temp-babelfish, and use pre-release of babelfish 0.6.0b1

### 2021.07.22

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.14-6...2021.07.22)

* Release 2021.7.22-2
* Fix formatting
* Bump webpack from 4.46.0 to 5.45.1
* Bump eslint-plugin-unicorn from 29.0.0 to 34.0.1
* Bump grunt-contrib-sass from 1.0.0 to 2.0.0
* Bump eslint from 7.30.0 to 7.31.0
* Bump eslint-config-xo from 0.35.0 to 0.37.0
* Bump xo from 0.41.0 to 0.42.0
* Bump grunt-contrib-jshint from 1.1.0 to 3.0.0
* Bump load-grunt-tasks from 3.5.2 to 5.1.0
* Bump grunt-contrib-clean from 1.1.0 to 2.0.0
* Bump coveralls from 3.1.0 to 3.2.0
* Bump actions/stale from 3 to 4
* Bump ava from 0.24.0 to 3.15.0
* Bump black from 20.8b1 to 21.7b0
* Use kodipydent-alt and beekeeper-alt

### 2021.07.14-6

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.14-5...2021.07.14-6)

* Limit regex to new release number format

### 2021.07.14-5

[full changelog](https://github.com/SickChill/SickChill/compare/2021.07.14-4...2021.07.14-5)

* Limit changelog to last 2 years
* Fix changelog generation

### 2021.07.14-4

[full changelog](https://github.com/SickChill/SickChill/compare/2020.03.38-4...2021.07.14-4)

* Try to fix gruntfile for patchlevel
* Fix another pathlib error [#7279](https://github.com/SickChill/SickChill/issues/7279)#issuecomment-879784353 Signed-off-by: miigotu <miigotu@gmail.com>
* Use an output to set extra tags
* Path.unlink() does not have the bool_ok parameter until python 3.8
* Bump grunt-contrib-uglify from 3.4.0 to 5.0.1
* Use lowercase for docker tags
* Bump grunt-contrib-cssmin from 2.2.1 to 4.0.0
* Bump eslint-plugin-promise from 4.3.1 to 5.1.0
* Remove action-docker-tags because it does not work
* Add piwheels.org index to init_helpers to speed up installs and eliminate compiling on raspberry pi Thanks to @egrueda for help Signed-off-by: miigotu <miigotu@gmail.com>
* Use dnaka91/action-docker-tags to generate the correct docker tags for builds

### 2020.03.38-4

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.27-1...2020.03.38-4)

* Start adding pyproject.toml

* Signed-off-by: miigotu <miigotu@gmail.com>

### 2016.04.27-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.17-2...2016.04.27-1)

* Refactor FilterBadReleases to filter_bad_releases, and adjust the logic:
    **Show specific required/ignored words now totally override global settings if they are set**

    If show ignored words are not set, global ignored words will be used
    If show required words are not set, global required will be used

    If the show has required words, they will be removed from the overall calculated ignored list when evaluating
    If the show has ignored words, they will be removed from the overall calculated rquired words list when evaluating

    If a show has required words which are also in the global ignored words they will override the global ignored and the release will be accepted
    If a show has ignored words which are also in the global required words they will overrid the global required and the release will be discared

    Release must not contain ANY of the final ignored words list, and at least ONE of the final calculated required words.

    Added a unit test to make sure this behavior is as expected and remains that way

    Fixes [#1541](https://github.com/SickChill/SickChill/issues/1541)
    Fixes [#1619](https://github.com/SickChill/SickChill/issues/1619)
    Fixes [#1623](https://github.com/SickChill/SickChill/issues/1623)
    Fixes [#1629](https://github.com/SickChill/SickChill/issues/1629)

* Updated torrentproject to use api magnet ([#1632](https://github.com/SickChill/SickChill/issues/1632))
* Fix Legendas.tv subtitle provider not showing for some people (stevedore...) Fixes [#1626](https://github.com/SickChill/SickChill/issues/1626)
* Fixed [#1623](https://github.com/SickChill/SickChill/issues/1623)
* Fixed [#778](https://github.com/SickRage/sickrage-issues/issues/778)
* Fixed [#1578](https://github.com/SickChill/SickChill/issues/1578)
* Fixed [#1585](https://github.com/SickChill/SickChill/issues/1585)
* Removed phxbit, no longer exists ([#1605](https://github.com/SickChill/SickChill/issues/1605))
* Added put.io & Join logos to the GUI ([#1595](https://github.com/SickChill/SickChill/issues/1595))
* Added putio client and update search providers templates ([#1550](https://github.com/SickChill/SickChill/issues/1550))
* Added Join notifier ([#1588](https://github.com/SickChill/SickChill/issues/1588))
* Updated icon sprite sheet

### 2016.04.17-2

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.17-1...2016.04.17-2)

* Update translations
* Move github setup out of sickbeard init to sickrage.common.helper, so a restart isnt required after entering github credentials ([#1533](https://github.com/SickChill/SickChill/issues/1533))
* Fanart background in displayShow ([#1531](https://github.com/SickChill/SickChill/issues/1531))
* Change level of all loggers when enabling debug, so a restart isnt required! ([#1529](https://github.com/SickChill/SickChill/issues/1529))

### 2016.04.17-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.16-1...2016.04.17-1)

* Fix database upgrade to 43.1
* Update translations
* Add Bulgarian translations

### 2016.04.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.14-1...2016.04.16-1)

* Update translations
* Added more text for translation ([#1504](https://github.com/SickChill/SickChill/issues/1504)) ([#1503](https://github.com/SickChill/SickChill/issues/1503)) ([#1499](https://github.com/SickChill/SickChill/issues/1499))
* Update TtN , remove unnecessary fall back and change size to bytes to… ([#1508](https://github.com/SickChill/SickChill/issues/1508))
* Display banner on DisplayShow page. ([#1518](https://github.com/SickChill/SickChill/issues/1518))
* Add MBC 1 logo ([#1515](https://github.com/SickChill/SickChill/issues/1515))
* Clickable icon to open shows page on http://www.fanart.tv ([#1512](https://github.com/SickChill/SickChill/issues/1512))
* Added some missing buttons for translation ([#1506](https://github.com/SickChill/SickChill/issues/1506)) ([#1507](https://github.com/SickChill/SickChill/issues/1507)) ([#1509](https://github.com/SickChill/SickChill/issues/1509))

### 2016.04.14-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.13-1...2016.04.14-1)

* Update languages, add a few translation strings

### 2016.04.13-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.12-1...2016.04.13-1)

* Bump DB version to 43 to avoid issues updating when DB was previously used with SRTV
* Specify encoding for config file
* Update pushbullet info string in webui
* Fix typo in rename-selected url
* Improve handling of windows file operations, fix issue with getting free space
* Temporarily Disabled pymediainfo due to segfaults

### 2016.04.12-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.11-2...2016.04.12-1)

* Merge pull request [#1469](https://github.com/SickChill/SickChill/issues/1469) from SickRage/neoatomic-develop
* Update translations, add en_GB translation
* Fix a few syntax errors in mako embedded python Fix manageSearches page syntax error for translatable string and clean it up some
* Some additions for the translations.
* Fixes [#1463](https://github.com/SickChill/SickChill/issues/1463)
* Update subliminal to 2.0.rc1 (b48c0c9) VANILLA! ([#1459](https://github.com/SickChill/SickChill/issues/1459))
* Remove itasa subtitle provider and add shooter.cn subtitle provider
* Try to fix [#1446](https://github.com/SickChill/SickChill/issues/1446) [#1445](https://github.com/SickChill/SickChill/issues/1445) ([#1458](https://github.com/SickChill/SickChill/issues/1458))

### 2016.04.11-2

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.11-1...2016.04.11-2)

* Add ability to select your language for the web ui in config/general on the interface tab

### 2016.04.11-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.10-1...2016.04.11-1)

* Fix issue tracker link in readme
* Combine show req/ign words with global ign/req words when checking release names so it doesnt require a word from BOTH ign lists or BOTH req lists
* Fix issue with manual pp and nzbtomedia
* Fix a few str formatting errors and add a few localizable strings

### 2016.04.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.09-1...2016.04.10-1)

* Update translation strings
* Fix typos related to translations
* Fix selecting subtitle languages

### 2016.04.09-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.08-1...2016.04.09-1)

* Fix issue matching subtitles from the wrong show to downloads in the PP folder
* Add mediainfo integration for getting video screen size, to help guessing quality from unknown quality files. Can be used for more things in the future
* Translate the rest of the ui, still small tweaks here and there to-do
* Update with latest translations, you guys are on fire

### 2016.04.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.04.01-1...2016.04.08-1)

* Add ability to fully translate the web interface
  Use crowdin.com for managing translations

* Fix issue listing files associated with an episode or video file.
  This fixes subtitles and nfo not being moved during post processing,
  and not being renamed when renaming episodes

  Also fixes PP trying to double process a video, because the video itself
  was also returned as an "associated file"

* Fix issue where show refresh used an insane amount of memory/cpu
  and would hang on broken videos and avi files when quality was
  not detected from the name.

* Fix wrong show/episode air times
* Fix issue sending app image to boxcar2

* Small tweak to make web interface look just a little better on mobile, more to come.

* Fixed [#1373](https://github.com/SickChill/SickChill/issues/1373) ([#1378](https://github.com/SickChill/SickChill/issues/1378))
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

### 2016.04.01-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.31-1...2016.04.01-1)

* Fixes [#1309](https://github.com/SickChill/SickChill/issues/1309), [#1304](https://github.com/SickChill/SickChill/issues/1304), [#1285](https://github.com/SickChill/SickChill/issues/1285)
* Fix "Unable to determine free space"
* Fix issue where importing existing files that parsed to unknown quality would not change episode status to downloaded
* Fix issue causing incorrect airdates
* Fix issue with timezones causing Synology DSM6 to fail to start
* Fix bug where qualityFromFileMeta was getting double and triple called

### 2016.03.31-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.28-2...2016.03.31-1)

* Highlights:
    Allow sending NZB's to DSM on Synology
    Ignored/Required words for specific shows override global defaults now
    Add channels support for pushbullet
    Hella fixes? xD

* Fix port number in settings gui url note
* Use a set().difference for handling ignored/required words If a word is in the global ignored words and in the show's required words, it is required If a word is in the global required but in the show's ignored, it is ignored
* DSM: Make sure to use nzb client settings when sending nzb, and torrent settings when sending torrents
* Add docstrings
* Add ability to use Synology DSM for nzb also
* Allow trakt checker to continue when imdbid is not known for one show Fixes [#1287](https://github.com/SickChill/SickChill/issues/1287)
* release group sort is now case insensitive
* Fix tuple index out of range
* Make "Available Groups" sort by alphabetical order
* Fix typo from unicode_literals regexing...
* Disable OneRun wrapper for PP, we need a better solution Fixes [#1282](https://github.com/SickChill/SickChill/issues/1282) [#1389](https://github.com/SickRage/sickrage-issues/issues/1389)
...
* Handle when hash or size are missing
* Fix error with multiple search results per provider Thanks @p0psicles
[#1390](https://github.com/SickRage/sickrage-issues/issues/1390)
* Add debian/ubuntu install script contributed by @DirtyCajunRice
* Make sure df returns 1k blocks without the K suffix
* These arent coding errors, whoever made them logger.ERROR should be swatted Fixes [#1263](https://github.com/SickChill/SickChill/issues/1263)
* Make disk_usage return int, and convert it from K to B Assure df returns in KB (default on most systems, but lets be sure) Fixes [#1269](https://github.com/SickChill/SickChill/issues/1269)
* Remove helpers._getTempDir as it is unused Use platform.system instead of os.name in helpers
* Add functions to check for Pushbullet channels

### 2016.03.28-2

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.28-1...2016.03.28-2)

* Unicode literals for TorrentDay Try and parse size from a dict by default in GenericTorrentProvider
* Split out disk_usage logic so that verify_freespace and getDiskSpaceUsage use the same logic Replaces [#1262](https://github.com/SickChill/SickChill/issues/1262) Fixes [#1259](https://github.com/SickChill/SickChill/issues/1259)
* Update french fansub
* Added Subtile Provider Cache
* Call df in a subprocess, since OSX has a bug with volumes > 4TB when using statvfs. This will work in all unix-like environments Fixes [#1259](https://github.com/SickChill/SickChill/issues/1259)
* Remove nzbToMedia from source control. It auto updates and breaks git pull
* Use cookie auth for DSM Show error messages for error codes returned from DSM according to DSM docs Check DSM version, and fix the download location if it is absolute on DSM6
* Fix transmission test connection Replaces [#1247](https://github.com/SickChill/SickChill/issues/1247)
* Remove alt.binaries.teevee from binsearch provider (no longer exists) Fixes [#1238](https://github.com/SickChill/SickChill/issues/1238)
* Change code back to use original bencode Fix some logs Fixes wrong torrent hash calculation (labels sometimes not working in utorrent) Fixes [#1235](https://github.com/SickChill/SickChill/issues/1235) [#1203](https://github.com/SickChill/SickChill/issues/1203) [#1375](https://github.com/SickRage/sickrage-issues/issues/1375)
* Comment lines that cause most errors with bdecode
* Switch back to official libtorrent bencoder
* Update snyk Use .on('click'... instead of .click(... syntax in js Set a default value for downCurQuality in retryEpisode Use the callback in $.post in js to make sure the reload is after the post finishes, otherwise the reload is before eg. the episode status has changed
* Fix indice error when no results in an omgwtfnzbs search Fixes [#1380](https://github.com/SickRage/sickrage-issues/issues/1380) Fixes [#1225](https://github.com/SickChill/SickChill/issues/1225)
* Dont warn saying incorrect passkey for shazbat when it has no results Fixes [#283](https://github.com/SickRage/sickrage-issues/issues/283)
* showDir is utf-8 when addExisting shows Fixes [#1229](https://github.com/SickChill/SickChill/issues/1229)
* Fix Seeders and Leechers on TtN
* Add a few more non release groups
* Fix brassetv and add others
* Fix web_root prepend for redirects.
* Use tzlocal and pytz for everything except parsing date strings from the name parser
* Add tzlocal and pytz libs

### 2016.03.28-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.23-1...2016.03.28-1)

* Use cookie auth for DSM Show error messages for error codes returned from DSM according to DSM docs Check DSM version, and fix the download location if it is absolute on DSM6
* Fix transmission test connection Replaces [#1247](https://github.com/SickChill/SickChill/issues/1247)
* Remove alt.binaries.teevee from binsearch provider (no longer exists) Fixes [#1238](https://github.com/SickChill/SickChill/issues/1238)
* Change code back to use original bencode Fix some logs Fixes wrong torrent hash calculation (labels sometimes not working in utorrent) Fixes [#1235](https://github.com/SickChill/SickChill/issues/1235) [#1203](https://github.com/SickChill/SickChill/issues/1203) [#1375](https://github.com/SickRage/sickrage-issues/issues/1375)
* Comment lines that cause most errors with bdecode
* Switch back to official libtorrent bencoder
* Update snyk Use .on('click'... instead of .click(... syntax in js Set a default value for downCurQuality in retryEpisode Use the callback in $.post in js to make sure the reload is after the post finishes, otherwise the reload is before eg. the episode status has changed
* Fix indice error when no results in an omgwtfnzbs search Fixes [#1380](https://github.com/SickRage/sickrage-issues/issues/1380) Fixes [#1225](https://github.com/SickChill/SickChill/issues/1225)
* Dont warn saying incorrect passkey for shazbat when it has no results Fixes [#283](https://github.com/SickRage/sickrage-issues/issues/283)
* showDir is utf-8 when addExisting shows Fixes [#1229](https://github.com/SickChill/SickChill/issues/1229)
* Update btn.py
* Fix web_root prepend for redirects.

### 2016.03.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.22-1...2016.03.23-1)

* Quantified code, please dont force format tokens to strings, lol Fixes [#1370](https://github.com/SickRage/sickrage-issues/issues/1370)
* Show how many characters the url has exceeded the limit in the alert when operating on too many shows [#1203](https://github.com/SickRage/sickrage-issues/issues/1203)#issuecomment-200097373
* Pass true to loaction.reload, to ensure it doesnt reload from cache Fixes [#1202](https://github.com/SickChill/SickChill/issues/1202)
* Clean up generic client and utorrent client use unicode_literals and str.format()

### 2016.03.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.20-1...2016.03.22-1)

* Use unicode_literals in show_queue Use str.format() Lint, and fix some funkyness Normalize text between ui notifications and logger
* Send verify=False for sab requests Fixes [#1201](https://github.com/SickRage/sickrage-issues/issues/1201)
* add number index to string format replacements, normalize the search string log line
* match bs4 search results by direct parameter rather than attrs=
* Use bs4 objects as a method instead of explicitly calling findAll/find_all for shorter code
* Remove unnecessary cookielib
* Unify requests exception handling
* Unicode literals for common, helpers, naming, and tv Fixes [#1340](https://github.com/SickRage/sickrage-issues/issues/1340)
* Disable SSL verify in t411 since their cert does not match Fixes [#1341](https://github.com/SickRage/sickrage-issues/issues/1341)
* Only encode potential extra script params if there is actually a script to run Add some try/except. Might need one to catch the execv error Fixes [#1237](https://github.com/SickRage/sickrage-issues/issues/1237)
* Modified itasa provvider for better scores

### 2016.03.20-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.10-1...2016.03.20-1)

* Change wiki/issues links to main repo
* Clean up gui imports, and some other finagery
* Updating subliminal to [f40e79a](https://github.com/SickChill/SickChill/commit/f40e79a78b7c8c92b83399d4d8778ec54ee8b7d2) plus legendastv and itasa providers
* Avoid `None` as a redundant second argument to `dict.get()` Avoid using `not ... is` instead of `is not`
* Use set comprehension
* Avoid mutable defaults for method parameters
* Avoid using `len(x)` to check if x is empty
* Remove funkyness with torrentday, untested
* Hacky fix for 11.22.63, the warning was never really an error anyways, just a warning on one of the regex iterations that it didnt match to Fixes [#1221](https://github.com/SickRage/sickrage-issues/issues/1221)
* Only show commit hash for ERROR log lines
* Update nzbtomedia reference to V10.14
* Update requests to 2.9.1
* Update certifi to [3850279](https://github.com/SickChill/SickChill/commit/38502797954603558ebf5f2c93f3645279e18158)
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
* Try again for 1086 Fixes [SickRage/sickrage-issues#1086](https://github.com/SickRage/sickrage-issues/issues/1086)
* Cleanup sickbeard.\_\_init\_\_ to remove some global keywords and write out the config nicer
* If adding existing shows, and you have a show in your list with a missing show dir, re-use the existing show object in the db and update it's info rather than skipping it
* Add limit for massupdate url generated by js
* Limit url length generated by addExisting with an ugly js alert =P Temporary solution
* Fixes [#1198](https://github.com/SickRage/sickrage-issues/issues/1198)
* Switch bencode implementation, using https://pypi.python.org/pypi/python-bencode
* update dateutil to d05b837
* Remove some spamminous logging from name_cache, db upgrade checks, and setter sets location (tv.py) Cleanup db.py
* Add missing ITASA globals in sickbeard.\_\_init\_\_
* Some changes to nw timezones, hopefully will make it more reliable.
* Encode file path and episode location to SYS_ENCODING (usually utf-8) before calling popen Fixes [#1086](https://github.com/SickRage/sickrage-issues/issues/1086)
* Add .pullapprove.yml
* Added ItaSA subtitle provider

### 2016.03.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.03.05-1...2016.03.10-1)

* Don't save filter_Rows state through page refreshes Fixes [#1177](https://github.com/SickRage/sickrage-issues/issues/1177)
* No need to specify timezone in datetime.now() in the footer
* Newznab provider handles show id internally now, and rid is no longer used, so this is stray code that does nothing
* Use a better module property name for hachoir's log
* log ERROR=>DEBUG when show is already being updated and attempted to be done again Fixes [#1165](https://github.com/SickRage/sickrage-issues/issues/1165)
* Fix commit hash update notifications when using source install. Fixes [#1118](https://github.com/SickRage/sickrage-issues/issues/1118)
* Fix auth header for pushbullet [#1118](https://github.com/SickRage/sickrage-issues/issues/1118)
* Add custom notification email subject
* Fix WEB-DL and WEB-Rip detections * Optimize regex * Add WEB detection * Add DLMux detection
* Use sickrage.github.io for url to the icon, instead of rawgit
* Add icon and app name to boxcar notification
* Boxcar2, use requests, unicode literals, str.format
* Oops, need to send the session to getURL
* Rework pushbullet, might need some message improvements
* Rework pushalot notifier Fixes [#1034](https://github.com/SickRage/sickrage-issues/issues/1034)
* update dateutil to c2c9700
* Fix NoneType for CUR_COMMIT_HASH error when github is not available
* Updated "Sync File Extension" list for qBittorrent
* Fix typo in TTN Fixes [#1112](https://github.com/SickRage/sickrage-issues/issues/1112)
* Use request hook for download_file in providers, until we can be sure sessions are working correctly
* Don't require TLD with validators for providers that may be local (bitcannon, torznab, newznab) Fixes [#1117](https://github.com/SickRage/sickrage-issues/issues/1117)
* Rework how session and request parameters are handled Prevents residual params in the session Prevents session getting stuck in stream mode Allows ssl_verify to be disabled without a restart Allows passing verify as a kwarg to disable it on a per request basis Allows passing headers without contaminating the session Removes old code from glype that was poisoning the session/headers/proxies
* Add setup.py and tox
* Add better test coverage to GenericProvider
* Fixes [SickRage/sickrage-issues#1115](https://github.com/SickRage/sickrage-issues/issues/1115)
* Clean up scheduler thread formatting in `sickbeard.\_\_init\_\_` Set show updater to cycle time 1hr again, see if that fixes it not running Delay start of most threads at least a minute or two after startup Fix bug adding cycle time to last_run
* Make show filter on poster view case insensitive match.
* Add anime category for bluetiger provider
* Add code to send email on remote login and sickrage updates Use unicode literals Use str.format
* Fix network timezone reporting
* Refresh show from dir even when it hasnt been updated on tvdb, but do not rebuild metadata (force=False) Fixes [#1089](https://github.com/SickRage/sickrage-issues/issues/1089)
* Don't error when show was already removed from trakt or never was on trakt. Fixes [#1038](https://github.com/SickRage/sickrage-issues/issues/1038)
* Fix errant nzbget string after converting strings
* Fix searching tvdb to add shows when result contains a result that has no firstaired set. Clean up sickbeard.classes
* pre-sort qualities for quality list Fixes [#1087](https://github.com/SickRage/sickrage-issues/issues/1087)
* Hotfix dateutil error for timezone names on Windows
* Fix error where sometimes client did not log into the provider before downloading a torrent or nzb Fix error where sab was calling an undefined method Switch sab code over to completelt requests Pass returns= in all calls to get_url Remove json= and need_bytes= params from getURL and get_url Cleaner \_\_str\_\_ for search result class Remove some dupe logging

### 2016.03.05-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.22-1...2016.03.05-1)

* Use content when downloading nzbs
* Updated the provider icons & added viceland network logo.
* Fix "'NoneType' object has no attribute 'indexerid'" when deleting a show when new shows are being added.
* https://github.com/SickRage/SickRage/commit/[bbd1618](https://github.com/SickChill/SickChill/commit/bbd16184ae6f47d5d260cb08e4dde18cd7c1cd4d)#commitcomment-16505285
* Fix gingadaddy Fix nzb.su and other providers who don't support tvdbid Use dict for result lists in all torrent providers No need to override get_ratio Fix more get_url calls to use the request hook Fix issue with blank download url when using transmission 2.90+ Fix dupe quality from numDict Sort quality lists Much more
* Force mimetypes for commonly misconfigured types, ie: when a user has dreamweaver installed Fixes [#1078](https://github.com/SickRage/sickrage-issues/issues/1078)
* Fix login issue with tvchaosUK, fixes need to double login Fixes [#1077](https://github.com/SickRage/sickrage-issues/issues/1077)
* Update dateutil to 2.5.0 with updated zoneinfo
* Fix tvchaosuk, there is one persistent cookie for CF, then totals 4 cookies when authed Fix tntvillage login, has 3 cookies when logged in. RSS search still disabled in this provider Fixes [#1072](https://github.com/SickRage/sickrage-issues/issues/1072)
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
* Fixes [#1046](https://github.com/SickRage/sickrage-issues/issues/1046)
* Use a decorator to prevent processing a dir more than once at a time, regardless of caller Fixes [#1028](https://github.com/SickRage/sickrage-issues/issues/1028)
* Fixes [#1042](https://github.com/SickRage/sickrage-issues/issues/1042) Fixes touchFile to use ek and check file exists
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
* NewPCT:
  - Unicode literals
  - Fix string quotes
  - Fix get_url override
  - Conformity and cleanup
* Warn about database owner/permissions
* NewPCT:
  - Unicode literals
  - Fix string quotes
  - Fix get_url override
  - Conformity and cleanup
* Make the show updater run on startup Fix it so that it doesnt keep updating the same shows over and over Fix cycleTime for show updater for status page Clean up logging in tv.py when setting the next episode and updating show
* Disable subtitles code db check
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Catch shutil errors and proper display as error/warning
* Create gists as secret instead of public
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix [#235](https://github.com/SickRage/sickrage-issues/issues/235)#issuecomment-185068695
* Add "(musicbolt.com)" to removewordslist
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix [#235](https://github.com/SickRage/sickrage-issues/issues/235)#issuecomment-185068695
* Pass params through getRSSFeeds to get_url instead of urlencode Update string quotes, u prefix removal and unicode literals for bunsearch, nyaa, omg, rsstorrents, shazbat, womble Clean up and improve those providers
* Add option to ini to allow PMS update without token or user/pass when you dont require authentication config.ini only option for now
* Use provider's get_url for getting rss feeds instead of urllib/httplib2 Fixes bozo, and removes old code Normalizes logging
* Update contributing.md
* Dont run FINDSUBTITLES thread right on SR start
* Allow passing arguments future= and past= for range of weeks from today to add to the webcal http://localhost:8081/calendar?past=2&future=3 both default to 52
* Handle float log sizes Increase default log size to 10MB to reduce rolling over Fix SickRage/sickrage-issues/issues/892 Replaces [#1027](https://github.com/SickChill/SickChill/issues/1027)
* Fix typo preventing confirm modal not showing before submitting errors
* RARBG:
  - Show api error messages
  - Show log when no torrents differentiated from when no data returned
  - Move sleep to prevent hitting request limit and use CPU_PRESETS
* Fix btdigg api url
* It is returns= not response= now
* RARBG:
  - Use unicode literals, remove u prefixes, use " over ' for strings
  - Use .format over token string formatting
  - Pass returns="json"
  - Remove excess logging, pop elements as they are used from the json
* BTDigg:
  - Use unicode_literals, remove u prefixes, use " instead of ' for strings
  - Use .format instead of token string formatting throughout
  - Pass params to get_url, and specify json response type
  - Remove duplicitous logging
  - General BTDigg cleanup
  - Add ! to config_providers since btdigg api is currently not working.
* Revert "fixed, Newznab cats that are disabled, shouldn't be shown in configure options tab."
* Adjust requests hook just a bit
* Use a requests hook for get_url in providers, show post data for post requests
* KAT:
  - Use unicode_literals, remove u prefix, use " for strings
  - Use validators for custom_url
  - Use urljoin throughout
  - BS4Parser for better cleanup
  - Fix issue with magnets
* Fix seeders/leechers log lines
* Providers:
  - Only include freeleech in provider \_\_init\_\_ if provider supports it (same for minseed, minleech, etc)
  - No need to encode search_string, it is encoded in _get_*_search_strings
* TorrentBytes:
  - Use unicode_literals, remote u prefixes, use " over ' for strings
  - Use urljoin throughout
  - Pass search params to requests instead of building the url
  - Pass response="text" to get_url
  - Parse table headers and use for cell indexing
* TPB doesnt have freeleech
* ABNormal code doesnt support freeleech param
* Bitcannon:
  - Use unicode_literals and remove u prefixes
  - Use " over ' for strings
  - Use validators for custom_url
* Add missed dependancy for validator: decorator.py
* No need to check if torrent_table is None, it is handled in the next line to allow the log
* Update torrentleech
  - Use unicode_literals and remove u prefixes
  - Use " over ' for strings
  - Use .format over token formatting
  - Use urljoin over string concat for urls
  - Pass params to get_url instead of urlencoding
* Update search string log line for all providers
* Update BinSearch
  - Use unicode_literals and remove u prefix
  - Use " over ' for strings
  - Use .format over % token string formatting
  - Use urljoin instead of concat for urls
  - Import urljoin, urlencode from requests.compat
* AbNormal Updates
  - Pass response="text" for login and search
  - No need to use named format replacements unless you are using the same replacement more than once
  - Switch back to " over ' for strings
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
* Clean up airdate modify timestamp handling and make sure exceptions are caught. Fixes [#914](https://github.com/SickRage/sickrage-issues/issues/914)
* Make sure etree always adds xml declaration for mede8er and specify encoding explicitly Trying to fix [#862](https://github.com/SickRage/sickrage-issues/issues/862)
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
* Fail gracefully and continue PP when setting file timestamp to airdate chokes Fixes [#269](https://github.com/SickRage/sickrage-issues/issues/269)
* Allow changing categories for defautl newznab providers. Caveat: They are on the "Custom Newznab Providers" tab where you change the categories, until the js can be fixed
* Need to use generic exceptions for all seasons, not just season 1
* Need to use generic exceptions for all seasons, not just season 1
* Filter scene exceptions a bit different
* Fromstring is already the tree root -.-
* Explicitly encode in the exception raises for name parser Partial issue of [#12](https://github.com/SickRage/sickrage-issues/issues/12)
* Must use etree.fromstring instead of etree.parse since its a string instead of a stream now in PMS
* Must check if generic exceptions are in the exceptionList already before appending them. Fixes [#852](https://github.com/SickRage/sickrage-issues/issues/852)
* Add explanation about subliminal score math
* Don't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Fix SickRage/sickrage-issues/issues/824

### 2016.02.22-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.16-1...2016.02.22-1)

* Use a decorator to prevent processing a dir more than once at a time, regardless of caller Fixes [#1028](https://github.com/SickRage/sickrage-issues/issues/1028)
* Fixes [#1042](https://github.com/SickRage/sickrage-issues/issues/1042) Fixes touchFile to use ek and check file exists
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
* NewPCT:
  - Unicode literals
  - Fix string quotes
  - Fix get_url override
  - Conformity and cleanup
* Make the show updater run on startup Fix it so that it doesnt keep updating the same shows over and over Fix cycleTime for show updater for status page Clean up logging in tv.py when setting the next episode and updating show
* Disable subtitles code db check
* Fix searches with ABNormal Replace double quotes with single quotes as per our decided convention
* Catch shutil errors and proper display as error/warning
* Create gists as secret instead of public
* Add "(musicbolt.com)" to removewordslist
* Fixes detection of "nothing found" when search result set is empty for torrentbytes. Fix [#235](https://github.com/SickRage/sickrage-issues/issues/235)#issuecomment-185068695
* Pass params through getRSSFeeds to get_url instead of urlencode Update string quotes, u prefix removal and unicode literals for bunsearch, nyaa, omg, rsstorrents, shazbat, womble Clean up and improve those providers

### 2016.02.16-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.11-1...2016.02.16-1)

* Add option to ini to allow PMS update without token or user/pass when you dont require authentication config.ini only option for now
* Use provider's get_url for getting rss feeds instead of urllib/httplib2 Fixes bozo, and removes old code Normalizes logging
* Update contributing.md
* Dont run FINDSUBTITLES thread right on SR start
* Allow passing arguments future= and past= for range of weeks from today to add to the webcal http://localhost:8081/calendar?past=2&future=3 both default to 52
* Handle float log sizes Increase default log size to 10MB to reduce rolling over Fix SickRage/sickrage-issues/issues/892 Replaces [#1027](https://github.com/SickChill/SickChill/issues/1027)
* Fix typo preventing confirm modal not showing before submitting errors
* RARBG:
  - Show api error messages
  - Show log when no torrents differentiated from when no data returned
  - Move sleep to prevent hitting request limit and use CPU_PRESETS
* RARBG:
  - Use unicode literals, remove u prefixes, use " over ' for strings
  - Use .format over token string formatting
  - Pass returns="json"
  - Remove excess logging, pop elements as they are used from the json
* BTDigg:
  - Use unicode_literals, remove u prefixes, use " instead of ' for strings
  - Use .format instead of token string formatting throughout
  - Pass params to get_url, and specify json response type
  - Remove duplicitous logging
  - General BTDigg cleanup
  - Add ! to config_providers since btdigg api is currently not working.
* TorrentBytes:
  - Use unicode_literals, remote u prefixes, use " over ' for strings
  - Use urljoin throughout
  - Pass search params to requests instead of building the url
  - Pass response="text" to get_url
  - Parse table headers and use for cell indexing
* Bitcannon:
  - Use unicode_literals and remove u prefixes
  - Use " over ' for strings
  - Use validators for custom_url
* TorrentLeech
  - Use unicode_literals and remove u prefixes
  - Use " over ' for strings
  - Use .format over token formatting
  - Use urljoin over string concat for urls
  - Pass params to get_url instead of urlencoding
* KAT:
  - Use unicode_literals, remove u prefix, use " for strings
  - Use validators for custom_url
  - Use urljoin throughout
  - BS4Parser for better cleanup
  - Fix issue with magnets
* AbNormal Updates
  - Pass response="text" for login and search
  - No need to use named format replacements unless you are using the same replacement more than once
  - Switch back to " over ' for strings
* Alpharatio updates * Use urljoin over string concat * Use unicode_literals * Remove search url log and pass response param to get_url
* TPB: * Use unicode_literals and remove u prefix * Use " over ' for strings * Use .format over string tokens * Remove extra search url log and pass response='text' to get_url * use validators to validate custom_url
* BinSearch:
  - Use unicode_literals and remove u prefix
  - Use " over ' for strings
  - Use .format over % token string formatting
  - Use urljoin instead of concat for urls
  - Import urljoin, urlencode from requests.compat
* Use a requests hook for get_url in providers, show post data for post requests
* Fix seeders/leechers log lines
* Providers:
  - Only include freeleech in provider \_\_init\_\_ if provider supports it (same for minseed, minleech, etc)
  - No need to encode search_string, it is encoded in _get_*_search_strings
* Add URL logging to GenericProvider.get_url
* Add raw response object as a getURL return type Add pending deprecation warnings for getURL arguments json, need_bytes Add pending deprecation warning for getURL returning text
* Update search string and mode log line for all providers
* Add lib/validators to be used with custom_urls and email and ip validation of user input and other places
* Import urlencode from requests.compat instead
* Clean up airdate modify timestamp handling and make sure exceptions are caught. Fixes [#914](https://github.com/SickRage/sickrage-issues/issues/914)
* Make sure etree always adds xml declaration for mede8er and specify encoding explicitly Trying to fix [#862](https://github.com/SickRage/sickrage-issues/issues/862)
* Allow file globs in "Sync File Extensions" setting to postpone postprocessing
* Remove old_scene_quality Remove quality assertion Refactor sceneQuality => scene_quality Fix anime bluray detection
* Append show name to show search strings regardless of searched season
* Fix logging when result is None fixes SickRage/sickrage-issues/issues/902
* Fix apikey shown in log when = is urlencoded as %3D
* Don't limit allowed extensions to 3 chars in post processor
* Reduce subtitle score to match only Series, Season, Episode and Year
* Fail gracefully and continue PP when setting file timestamp to airdate chokes Fixes [#269](https://github.com/SickRage/sickrage-issues/issues/269)
* Allow changing categories for default newznab providers. Caveat: They are on the "Custom Newznab Providers" tab where you change the categories, until the js can be fixed
* Use generic exceptions for all seasons, not just season 1

### 2016.02.11-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.10-1...2016.02.11-1)

* Explicitly encode in the exception raises for name parser Partial issue of [#12](https://github.com/SickRage/sickrage-issues/issues/12)
* Must check if generic exceptions are in the exceptionList already before appending them. Fixes [#852](https://github.com/SickRage/sickrage-issues/issues/852)
* Add explanation about subliminal score math
* Don't show CC button for 'snatched' episodes that used to be 'downloaded' but failed
* Fix SickRage/sickrage-issues/issues/824
* Added network logo's  for RMC decouverte and UP TV.
* Use .eu for podnapisi
* Fix cyclic dependancy in notifiers so we can use helpers, clean up some crazy
* Updated subliminal develop (864ecf4) and legendastv provider, adjusted scores for subtitles
* Rewrite a good bit of plex notifier to use requests and maintain headers
* Fix download url generation in alpharatio, danishbits, gft, speed.cd Fixes [#818](https://github.com/SickRage/sickrage-issues/issues/818)
* Fix anime bluray qualities

### 2016.02.10-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.09-2...2016.02.10-1)

* Use json scene exceptions
* Only get scene exceptions matching season we are searching for
* Set "Authentication Failed" as warning
* Fixes issue of MTV not downloading
* Add an API method to clear the logs
* Remove need for ek() in subtitles
* Fixe size on transmithenet

### 2016.02.09-2

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.08-1...2016.02.09-2)

* Use xem absolute numbers for tvdb mapping if tvdb doesnt provide them, fixes american dad if you disable scene numbering
* Dont pass q on rss update, use sickbeard.USENET_RETENTION directly regardless of mode
* Set search string for subsequent scene exceptions after tvdbid has been popped
* Fix provider log message by decoding to utf-8 instead
* Fix daily search in ABNormal.ws Fixes [#768](https://github.com/SickRage/sickrage-issues/issues/768)

### 2016.02.08-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.02.07-1...2016.02.08-1)

* Fix decode by using utf-8 instead Fix unnecessary decode on urlencoded string
* Make sickbeard.gh work even when github login settings are incorrect so that the updater still works Lint sickbeard.\_\_init\_\_
* Revert "Add 5020 (foreign) to default newznab providers (and some missing nzb…"
* Add 5020 (foreign) to default newznab providers (and some missing nzbs.org cats)
* Fix Unicode decoding errors in newznab logging and ex
* Display exception text from NameParser in validateDir
* Fix for nzb indexers who dont support tvdbid or happen to have missed a tvdbid mapping for some shows/episodes. Fixes [#667](https://github.com/SickRage/sickrage-issues/issues/667) Fixes [#782](https://github.com/SickRage/sickrage-issues/issues/782)
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
* Make sure - is at the end of character groups in regex to avoid future mistakes, even if they arent preceeded by another char Add , as a seperator between episode and extra_info for normal regex Fixes [#771](https://github.com/SickRage/sickrage-issues/issues/771)
* Fix schedule so it doesnt bork when db upgrade
* Remove the rest of the unnecessary len() in if's Rework the find_search_results a bit to use scene numbers depending if the show is scene or not to determine if the result matches or should be skipped, it was quite iffy, and still is.
* Fix bug that caused plex server/client password to be set to all * when saving notifications if you did not type them in after loading the page
* Use a better exception text for InvalidShow and InvalidName.
* Normalize more name_parser.parse calls and exception handling
* Use the string passed when raising InvalidNameException or InvalidShowException to avoid maintaining log text in too many places.
* Fix small mistake in name_parser, use better variable names in quality pills
* No need to use len to check if a list is not empty (name_parser.parser) No need to cast to list before iterating a set (name_cache) Lint name_parser.parser, fix small bug preventing S00 from being able to be parsed
* Rename initial to preferred in quality pill text

### 2016.02.07-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.01.31-1...2016.02.07-1)

* encode io.open in helper with ek()
* Updated subliminal develop (f245383)
* Updated guessit (28b6789)
* Updated rebulk (68a4588)
* Updated legendastv provider. Fixed a few things in subtitles.py
* Improve bitcannon provider Fixes [#763](https://github.com/SickRage/sickrage-issues/issues/763)
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
* Fixes [#736](https://github.com/SickRage/sickrage-issues/issues/736)
* Add editorconfig
* Dont show traceback if error sending torrent
* Dont clear old snatch history in failed.db, see if that fixes some issues with fdh
* Various flaking/code cleanup Change log from debug to info for http status code returned from clients Change log from error to warning when sending to client failed (the request failed, client down or network error maybe)
* Fix Attribute Error object has no attribute 'errno'
* Revert "Added add from popular anime list."
* Revert "Added anidb http client."
* Clean up recommended.py
* Optimize order of usage of parameters in \_\_init\_\_, optimize imports
* Fix spacing, tabs, spelling errors, non-unicode strings, docstrings, license information, encoding declarations, EOF, unused variables
* Group french team fansub, new encompassing anime regex
* Some changes to the help & info page.

### 2016.01.31-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.01.23-1...2016.01.31-1)

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

### 2016.01.23-1

[full changelog](https://github.com/SickChill/SickChill/compare/2016.01.20-1...2016.01.23-1)

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

### 2016.01.20-1


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


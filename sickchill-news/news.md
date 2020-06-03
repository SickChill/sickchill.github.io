####Please read the [Wiki/FAQ](https://github.com/SickChill/SickChill/wiki) before opening an issue####
All issues and bug reports must be opened at [GitHub](https://github.com/SickChill/SickChill/issues) and you **MUST** follow **ALL** [guidelines](https://github.com/SickChill/sickchill.github.io#submitting-a-bugissue-ticket).  


<br/>

####2020-06-03####

Thanks to some generous users, I have been able to get an older laptop to use until I can get a new one, so I am now able to help and release more fixes again.
Thank you to those who donated, we moved 2900 miles last year and have tons of expenses around the house and a laptop was out of the question for our current budget. <3
<br/>

####2020-05-30####

My laptop randomly stopped working so it might be a few weeks until I can get it fixed or save for a new one.
I will try and help with issues from my phone until then, but updates will be limited until then. Hope nobody has any major issues.

<br/>

####2020-01-21####

On the next release I will be merging code that forces you to use an access token for github to use the issue submitter. Username/Password login is deprecrated 
with github's new policy, and won't work much longer. If you want to keep submitting issues, go to settings->general->advanced and click the `Generate Token` 
button, or add one that you have already created. This is good because you can now control what permissions that token has with your account, and it is easy 
to revoke individual tokens if it happens to be compromised without changing your GitHub password. It is also required for 2FA if you decide to use that.

I have just fixed a glaring bug where tons of networks were not being added to the network_timezones since the scraper we built just for that was broken due 
to the new tvdb site. Episodes should start coming on time again.

TVDB api should be working on our end as long as their side is working. It does go down from time to time while they are 
working on it. If you see an APIkey error, its on theTVDB side and we cannot fix it so just be patient. 

<br/>

####2020-01-08####

Huge changes in develop will in the next day or 2 come to master, including the total switch over to the new TVDB api, using cloudscraper to fix cloudflare issues, and possibly updating subliminal. These changes are VERY pervasive,
and effect adding shows, updating shows, all images, metadata, notifications, trakt, and more. around 60k lines changed. Two notes of caution:

Before updating, make sure you have at least Python 2.7.9, because it will not run with anything lower, and it will not run on Python 3+.
If you are worried, wait a few days once the release to master is made before you update.

I hope this goes smoothly, it has been brutal the last few weeks with long hours trying to get it right.
Happy Snatchin and Happy New Year.

<br/>

####2019-06-26####

Greetings ill chill army! I am all packed up and moving across the country to the east coast. During this time I will be without much connectivity, so I will not be able to do much coding if any at all. I have been slacking for a bit, but I will try and merge contributions if anyone sends in any pull requests and I will be much more active once we settle in. Moving is expensive, tiresome, and scary driving a 30 foot 1996 RV a whole 2400 miles lol.  Once we get settled in our new state I will be adding the size limits for qualities, a new/better post processor, reworking providers and notifiers to use less memory, and more.

Please keep me, my wife, and our 2 kids in your thoughts (and prayers if that is your sort of thing) for a safe trip!

<br/>

####2018-11-22####

Happy Thanksgiving SickChillers! I am thankful for all of the loyal users and supporters. Hope you all have a great day!  

<br/>

####2018-11-2####

I plan on enforcing a strict policy to use SSL and web authentication, and adding hardware authentication.  
When you are using localhost or an IP only a self signed certificate will be used, and when you have a domain a letsencrypt certificate will be created.  
Also, I am trying to get my hands on a Yubikey 5 NFC so that I can implement FIDO2, U2F, OTAP and other secure hardware key authentication.  
Please go and vote thumbs up or down if you are interested in these features on [SickChill#5159](https://github.com/SickChill/SickChill/issues/5159)  

<br/>

####2018-10-30####

For any of you who have given up on Jackett+SickChill due to a bug with SC, the torznab issue with adding double season/episode to the search string has just been fixed and pushed to master.  
I am working on some big refactors for you all, in order to give more flexibility with installation options. I will be taking a break today and maybe tomorrow trying to clear my head of SC (since it is my birthday today, yay! lol)  
and try to avoid checking github for a full 24 hours. Don't worry, I will be back to adress any new issues!  

<br/>

####2018-10-24####

Due to a phony trademark claim, we have renamed the organization and application to SickChill.  
Note that echel0n is in control of the old SickRage organization and is neither trusted or afiliated with this project.  
(even references to the old organization and application name have been renamed in this file)  

</br>

####2017-08-05####

Our main repository on Github [SickChill/SickChill](https://github.com/SickChill/SickChill) is now available.  
If you installed SickChill using a mirror of **our** repository, or switched your installation to get updates from a mirror, please make sure that you're back on the main repo URL in order to be able to receive future updates.  
The basic set of commands is described [here](https://github.com/SickChill/sickchill.github.io#before-you-open-an-issue):  
```
git remote set-url origin https://github.com/SickChill/SickChill.git  
git fetch origin  
git checkout master  
git branch -u origin/master  
git reset --hard origin/master  
git pull  
```

<br/>


####2017-07-20####

A false DMCA takedown request was sent to GitHub, resulting in multiple repositories, including SickChill/SickChill, to be taken down.
We're countering this and should have the repo back very soon. We thank you for your patience.

<br/>

####2017-02-21####

It seems that the long-time free `Womble's Index` for nzb's has been taken offline.
We thank Womble for all of the years providing this free usenet index, and as a result of it going down we have had to remove the provider code for it from SickChill.

<br/>

####2017-01-26####

WINDOWS ONLY: SickChill now requires WinRar to be installed for windows users to be able to unrar releases.
The location of unrar should now be autodetected with the latest update, but if it is not you may need to add `C:\Program Files\WinRar` to your system path and restart SickChill.
As you windows users should know, restarting SickChill from the interface does not work, you will have to restart the service either through the service manager,
or from an administrator level command prompt with the following commands:
<br/>
```
    net stop sickchill
```
<br/>
```
    net start sickchill
```
<br/>
The library we use to interface with unrar had to be changed for several reasons, including unrar lockups, memory issues, and a lack of support for newer RAR5 format.


<br/>

####2016-12-20####

There is a small issue related to network timezones after the recent commits to make them case insensitive.
If stopping SickChill completely and then starting it again does not work, stopping it and deleting cache.db and then starting it back up should resolve the issue.

<br/>

####2016-04-11####

With my next commit, your web interface may revert to english translation. However, it is now a configurable option as to which language you want to use.  
You can find the option to change the language on http://localhost:8081/config/general/ at the top of the 'Interface' tab.
I hope you all are enjoying the translations, and please feel free to help out with them on [crowdin.com](https://crowdin.com/project/sickchill)

<br/>

####2016-04-08####

Among the many fixes in today's release, there is something special.  
**The web interface in SickChill is now translatable into any language!**  
If you would like to help translating the strings some information can be found on the [WIKI](https://github.com/SickChill/SickChill/wiki/Translations)  
Also, we would like to thank [CrowdIn](https://crowdin.com/project/sickchill) for our free open source project account to help managing the translations.

<br/>

####2016-03-25####

Quick note for Synology users. Yesterday Synology released [DSM 6,](https://www.synology.com/en-global/dsm/6.0) we advice users to wait with the update.
The problem is that the Sickbead-custom (and other Synocommunity) packages are not fully compatible yet.
If the packages are installed on DSM 5.2 and you upgrade they will keep working, but on a fresh DSM6 install or if you need to re-install the package they wont work anymore. More info and workarounds can be found on our [issue tracker](https://github.com/SickChill/SickChill/issues/587#issuecomment-201275502)

<br/>

####2016-03-14####

Some users can experience that air-dates are not updated for every show.  
If that is the case, than go to "Mass-update" and select "Update" for all shows, and let it run.  

Also when you get a warning in your log like **Missing time zone for network:** those can be added [here.](https://github.com/SickChill/sickchill.github.io/blob/master/sb_network_timezones/network_timezones.txt)  
They are used to calculate the exact airtime of a show in your specific timezone. This allows SickChill to start searching more precise, without this the search starts at exactly midnight local time.  

<br/>

####2016-01-12####

Here are another 200+ commits for you guys, which brings many bug fixes. Many providers were fixed up,
and a new 404 and error page has been added, along with the usual code cleaning and optimization.
Hope you enjoy!

<br/>

####2015-12-22####

The next release brings **many** fixes (~200 commits), and along with it will come some changes to how qualities are handled. Most specifically, **Archive on First Match** has been removed.

Before it is released tomorrow, we wanted to inform you of the changes, and steps you may need to take to keep your setup operating as expected. Please read [this wiki page](https://github.com/SickChill/SickChill/wiki/Qualities-Changes) and take any necessary action before updating. You may also disable automatic updates until you can take the time to do so.

<br/>

####2015-12-01####

Currently we are (still) in the process of a large cleaning-up and optimization of the SickChill code.  
This was really overdue, and will pave the road to all the new and cool features we plan to implement for you.  
However there is always a risk that it will expose minor bugs, that we weren't able to catch during testing.  
In case you encounter one, please make sure to report it on the [issue-tracker](https://github.com/SickChill/SickChill/issues) or [IRC channel](https://kiwiirc.com/client/irc.freenode.net/?theme=basic#(?<!old-)sickchill).  

This week we also launched our new [SickChill website](http://sickchill.github.io/).  

<br/>  

####2015-11-21####

For those who are not yet aware, we were forced to change/migrate the Repository on GitHub.
We apologize for any inconvenience this may have caused.  
As you can see, the team is up and running again and providing updates and support as before. Please make sure you update your bookmarks and links to point to the new repository:  

- New repository   :   https://github.com/SickChill/   
- New Issue tracker:   https://github.com/SickChill/SickChill  
- New Wiki page    :   https://github.com/SickChill/SickChill/wiki  

Please get the word out so your friends, package builders and tutorial makers are aware.  
For the Synology users, we made a tutorial so they can easily switch to the new [repository](https://github.com/SickChill/SickChill/wiki/Switching-your-Synology's-SickChill-to-the-new-repository).  
Again, apologies for any inconvenience this has caused.   

<br/>  

####2015-10-22####

There has been some confusion about yesterday's news about [nzbToMedia](https://github.com/SickChill/SickChill/wiki/NZBtoMedia) and the removal of the outdated autoProcessTV files/folder.

- The built-in post-processor is not being changed or effected in any way. If you use The built in post-processor, these changes do not affect you whatsoever and you do not need to make changes to your setup.

- SickChill will still support the use of autoProcessTV and sabtosickbeard.py, but we are no longer including them in the SickChill folder. If you still prefer to use the (old) autoProcessTV script package then you will have to manually download and store it somewhere outside of SickChill. It is however, recommended that you start switching over to the newer/better nzbToMedia in this case.

- [nzbToMedia](https://github.com/SickChill/SickChill/wiki/NZBtoMedia) is a rewrite/improvement upon autoProcessTV that adds support for Torrents, among other things. nzbToMedia is now included in the SickChill source in the contrib folder and you can find information about nzbToMedia and setup on our [Wiki](https://github.com/SickChill/SickChill/wiki/NZBtoMedia) and the [nzbToMedia Wiki](https://github.com/clinton-hall/nzbToMedia/wiki).

<br/>

####2015-10-21####

- New subtitles changes in today's version include the very latest and greatest subliminal. We have also added a new
subtitle provider [Legendas.TV](http://legendas.tv/) on top of what subliminal has to offer, and added some options to the subtitles settings page. You now have the option to download hearing impaired subtitles, and set login information for OpenSubtitles, Addic7ed, and Legendas.TV. Enjoy.

- Just 9 days left before we remove autoProcessTV from SickChill, since it has been deprecated about a month ago in favor of nzbToMedia. Please make sure to switch over before then if you are using it, or make sure to be using an autoProcessTV that resides outside of the SickChill source directory.

<br/>

####2015-10-02####

- Recently we improved the searching of the KAT & TPB Torrent providers. Some users report that they are not able to find new downloads anymore. If that is the case, shut down SickChill and remove the cache.db file. That should solve the problem.  

<br/>

####2015-09-20####

- *ShowsRage*
- One of our contributors (MGaetan89) has released his Android application for managing SickChill to Google Play. Be sure to check it out, rate, and provide feedback to show your support.
You can read the full description and information on [Google Play](https://play.google.com/store/apps/details?id=com.mgaetan89.showsrage) and the [ShowsRage GitHub Project](https://github.com/MGaetan89/ShowsRage)

<br />

####2015-09-09####

- As you might have noted the [TVRage](http://www.tvrage.com) website pulled the plug/shut down. And that is causing some issues we needed to address. We pushed a fix that automatically converts the TVRage ID to a TheTVDB ID. So that new data is pulled from theTVDB.com instead. That works for most users but sadly not all. So be aware that when you used TVRage shows, you might experience some issues. Be assured that we are working hard to get this all sorted out.
Also as a consequence of the TVRage shutdown we where forced to push some changes for the theme/layout that where not completely tested. Therefore the Network logos are currently not working. Fix coming soon.

- But not only bad news, we have a brand new [SickChill installer](https://github.com/SickChill/SickChill/wiki/SickChill-Windows-Installer) for Windows!

<br />

####2015-09-08####

- We are removing support for autoProcessTV in favor of Clinton Hall's nzbToMedia project, which we have imported in `contrib`
- autoProcessTV will be removed by 31-10-2015. Please update your post-processing scripts or they will break.

<br />

####2015-08-16####

- Switched to using mako templates in master. We should have ironed out all the issues regarding mako in past week. If not, please open an issue, using the guidelines above!

<br />

####2015-08-08####

- Switched to mako in develop branch. Please test it out and report in IRC, or on github. Security improvements such as moving sql out of the templates, form/input/uri validation coming soon. Performance improvements coming also, such as moving js out of the templates.

<br />

####2015-08-06####

 - We need some help writing the Wiki for Anime. If you want to help please contact neoatomic in IRC
 - All Wiki pages are now at this [URL](https://github.com/SickChill/SickChill/wiki) so users can contribute

<br/>

####2015-07-24####

 - if you have issues with strange characters (ie. ƒÆ'A+â?TAƒâ) in files names and/or in the SR interface and/or your database file (sickbeard.db) is suddenly way bigger than it should be please FULL update & refresh all your shows and force a mass rename after. Depending on your library size it can take some minutes or some hours. Backup DB first.

<br/>

####2015-07-23####

 - Now you can choose your default page when opening/logging to SR (General Options > Misc > Initial page)

<br/>

####2015-07-21####

- Added ability to run an external script for every subtitle downloaded (can be used to embed subs in mkv/mp4)
    For info about the parameters passed see [PR#2139](https://github.com/SickChill/SickChill/pull/2139)

- Added IRC tab in web ui, to connect to the SickChill IRC channel

<br />

####2015-07-18####

- Added setting to disable SSL certificate verification under Config -> General -> Advanced Settings
  (Committed on July 15)

  This might help if you have SSL errors

<br/>

####2015-07-17####

- Added new sub-menu called "Changelog". You can check what has changed in SickChill in each release

<br/>

####2015-07-16####

+ **Default Episode Status**: We recently fixed this feature so you need  to:

    - Edit your shows via 'Mass update' and set the default status to WANTED instead of SKIPPED (if you want unaired episodes to be downloaded)
    - Set all new episodes that were marked SKIPPED before that to WANTED. You can check all of them at "Episode Status Management" selecting "SKIPPED" in "Manage episodes with status". Be careful with this! Make sure you have a backup of your database. Be advised!
    - Now when you will add a **NEW** show you will be asked for two status settings: already aired episodes and unaired episodes.

<span style="margin-left:100px">
<img src="https://cloud.githubusercontent.com/assets/2620870/8724471/3cb943f4-2ba6-11e5-99cd-d645fb9e824f.png" width="300">
</span>

+ **Providers:** Sick beard index and Womble provider are blocking SR application so avoid using them

+ **Develop branch**

    - We are upgrading Subliminal module and this may and will break your installation
    - Please avoid using the develop branch until we fully tested everything unless you know what you are doing

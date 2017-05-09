py-udownloader
==========

py-udownloader is a lightweight script to download youtube/dailymotion/Liveleaks videos in different audio and video formats.
YouTube and Dailymotion are the most popular video-sharing platform in the world and as a user you may encounter a situation where you want to download the videos. For this I present to you py-udownloader. 

py-udownloader makes zero assumptions and give the user freehand by simply exposing all the available formats and resolutions, giving you the user the power to define what is "best" for you.

Description
-----------
py-udownloader automate the youtube/dailymotion/liveleaks videos downloading process using the selenium library from the https://www.onlinevideoconverter.com/mp3-converter website


Features
--------
* Supported Audio Formats : mp3, aac, ogg, m4a, wma, flac, wav
* Supported Video Formats : mp4, m4v, mov, avi, flv, mpg, wmv
* command-line utlity

Dependencies
------------
py-udownloader depend on third party libraries
* Selenium ( http://selenium-python.readthedocs.io/ )
* geckodriver (https://github.com/mozilla/geckodriver/releases )
* Beautiful soup (https://www.crummy.com/software/BeautifulSoup/ )
* urrlib

Comman-Line Example
-------------------
You need to add geckodriver to your path 

    $ export PATH=$PATH:/path/to/geckdriver/directory/
    $ ./py-udownloader #command-line utility to save demo youtube video in mp3 format
    $ ./py-udownloader -u videourl -f format -p path #command-line utility to save user provided youtube video in user specified url

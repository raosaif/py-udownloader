py-udownloader
==========

py-udownloader is a lightweight script to download youtube/dailymotion/Liveleaks videos in different audio and video formats.
YouTube and Dailymotion are the most popular video-sharing platform in the world and as a user you may encounter a situation where you want to download the videos. For this I present to you py-udownloader. 

py-udownloader makes zero assumptions and give the user freehand by simply exposing all the available formats and resolutions, giving you the user the power to define what is "best" for you.

Features
--------
* Supported Audio Formats : mp3, aac, ogg, m4a, wma, flac, wav
* Supported Video Formats : mp4, m4v, mov, avi, flv, mpg, wmv
* command-line utlity

Dependencies
------------
py-udownloader depend on third party libraries
* Selenium 
* Beautiful soup
* urrlib

Comman-Line Example
-------------------
    $ udownloader -u videourl -f format -p path

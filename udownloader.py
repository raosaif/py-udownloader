#!/usr/bin/env python3

import sys
import io
import getopt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib.request

website_url = 'https://www.onlinevideoconverter.com/mp3-converter'

def main(argv):

	def usage():
		print(('usage: %s [-d] [-u videoURL] [-f format] [-p path][-h help] ...' % argv[0]))
		return 100
	try:
	    (opts, args) = getopt.getopt(argv[1:], 'd:u:f:p:h')
	except getopt.GetoptError:
		return usage()

	def help():
		print("You can now download YouTube/Dailymotion/Liveleak videos as" 
			" MP3 and video files with HD video and audio quality."
			"\nSupported Audio Formats: [mp3,aac,ogg,m4a,wma,flac,wav]"
			"\nSupported Video Formats: [mp4,m4v,mov,avi,flv,mpg,wmv]")

	def supported_format():
		print("UnSupported Video or Audio Format. Please select from below mentioned formats."
			"\nSupported Audio Formats: [mp3,aac,ogg,m4a,wma,flac,wav]"
			"\nSupported Video Formats: [mp4,m4v,mov,avi,flv,mpg,wmv]")


	youtube_video_url = "https://www.youtube.com/watch?v=94dY-Qxj"
	format_to_be_saved = 'mp3'
	filePath = ''

	for (k, v) in opts:
		if k == '-d': debug = True
		elif k == '-u': 
			youtube_video_url= v 

		elif k == '-f': 
			format_to_be_saved = v
			if '.' in format_to_be_saved:
				format_to_be_saved=format_to_be_saved.replace('.','')

		elif k == '-p': filePath = v

		elif k == '-q' : file_quality = v
		elif k == '-h' : return help()


	with urllib.request.urlopen(website_url) as response:
		html = response.read()

	soup = BeautifulSoup(html,'lxml')

	audio_formats = []
	video_formats = []
	audio = soup.findAll("a", { "class" : ["audio-format","flac-wav" ]})
	for aud in audio:
		if 'data-value' in aud.attrs:
			audio_formats.append(aud.attrs['data-value'])

	video = soup.findAll("a", { "class" : ["video-format","video-format-2" ]})
	for vid in video:
		if 'data-value' in vid.attrs:
			video_formats.append(vid.attrs['data-value'])

	if format_to_be_saved not in audio_formats and format_to_be_saved not in video_formats:
		return supported_format()

	quality = ['64','96','128','192','256','320']

	active_values = soup.findAll("a",{'class':'active'})
	#print ('Active Format: .',active_values[0]['data-value'])
	#print ('Active Audio Quality: ',active_values[1]['data-value'], "kbps")

	print('File will be saved in .', format_to_be_saved, ' format.')

	driver = webdriver.Firefox() # user need to install geckodrive.
	#driver = webdriver.PhantomJS() # user can use PhantomJs also if they don't want firefox to run everytime.
	driver.get(website_url)

	assert "YouTube" in driver.title

	elem_link = driver.find_element_by_id("texturl")
	elem_link.clear()
	elem_link.send_keys(youtube_video_url)

	if format_to_be_saved != active_values[0]['data-value']:
		elem_link = driver.find_element_by_id("select_main")
		elem_link.click()
		li = driver.find_element_by_link_text('.' + format_to_be_saved)
		li.click()

	elem_link.send_keys(Keys.RETURN)

	while True:
		try:
			WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "download")))
			print('Video is processed Successfully....')
			break
		except TimeoutException:
			print ('Video is being Processed.....')

	html_page = driver.page_source

	title = ''
	soup = BeautifulSoup(html_page,'lxml')
	title_of_video = soup.findAll("a", { "href" :  youtube_video_url})
	for tov in title_of_video:
		if 'title' in tov.attrs:
			title = tov.attrs['title']

	download_link = soup.findAll("a", { "class" : "download-button" })
	for link in download_link:
		if 'href' in link.attrs:
			if 'http' in link.attrs['href']:
				#print('Link for Youtube Video: ',link.attrs['href'])
				print('Downloading the file........')
				urllib.request.urlretrieve(link.attrs['href'],filePath+title+'.'+ format_to_be_saved)

	print("Downloading Finished")
	driver.quit()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
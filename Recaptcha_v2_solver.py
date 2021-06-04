""" 
There are many different types of CAPTCHAs that are widely used to mitigate automation/web scraping
The most popular and predominantly used CAPTCHAs are the ones developed by Google, also known as reCAPTCHA
Furthermore, there are 4 unique variants of reCAPTCHA; for more info! --> https://developers.google.com/recaptcha/docs/versions
For this module, we will attempt to solve the [reCAPTCHA v2 "I'm not a robox Checkbox"] with a fairly decent accuracy
Note: not always guaranteed success
"""

# Used for solving/handling recaptcha by having system miscelllaneous/selenium/other libs to be integrated into our module and run smoothly
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
# We can test our reCAPTCHA solver using the url below
#driver.get("https://www.google.com/recaptcha/api2/demo")

def delay():
	time.sleep(random.randint(2, 3))

def bypass(driver):

# This is the usual procedure when dealing with iframe, where our reCAPTCHA is located inside of 
# (May be present in other popular websites/forms to promote unnecessary extra steps to deter automation)
	frame1 = driver.find_element_by_xpath("//iframe[contains(@src, 'https://www.google.com/recaptcha/api2/anchor')]")
	driver.switch_to.frame(frame1)
	recaptcha_checkbox = driver.find_element_by_class_name("recaptcha-checkbox-border")
	recaptcha_checkbox.click()
	delay()

# After clicking on the checkbox, we stumble upon another iframe and hence we have to repeat the procedure
# First get out of the current iframe
	driver.switch_to.default_content()

# Now we need to enter into the new iframe so that we can click on the audio button
	frame2 = driver.find_element_by_xpath("//iframe[contains(@src, 'https://www.google.com/recaptcha/api2/bframe')]")
	driver.switch_to.frame(frame2)
	delay()
	delay()
	audio_button = driver.find_element_by_xpath("//button[@class='rc-button goog-inline-block rc-button-audio']")
	audio_button.click()

# We are in the same iframe, so we dont have to repeat the procedure before clicking on the play button
	delay()
	play_button = driver.find_element_by_id(":2")
	play_button.click()

# Get the link of the audio file and print the url
	src = driver.find_element_by_class_name("rc-audiochallenge-tdownload-link").get_attribute("href")
	print("[INFO] Audio src: %s"%src)

# Download the file and save it in our current directory saved as "sample.mp3"
	urllib.request.urlretrieve(src, os.getcwd() + "\\sample.mp3")

# Convert the mp3 file to wav so that we can utilise our speech recognition
	sound = pydub.AudioSegment.from_mp3(os.getcwd() + "\\sample.mp3")
	sound.export(os.getcwd() + "\\sample.wav", format = "wav")

# Translate the audio to text and print the text
	r = sr.Recognizer()
	with sr.AudioFile(os.getcwd() + "\\sample.wav") as source:
		audio = r.record(source)			
	key = r.recognize_google(audio)
	print("[INFO] Recaptcha Passcode: %s:"%key)

# We can then enter this result(key) to complete the captcha!
	delay()
	driver.find_element_by_id("audio-response").send_keys(key.lower())
	delay()
	driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)

	driver.switch_to.default_content()

#submit_button = driver.find_element_by_id("recaptcha-demo-submit")
#submit_button.click()

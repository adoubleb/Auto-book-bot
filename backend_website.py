from selenium import webdriver
from selenium.webdriver import ActionChains
from Recaptcha_v2_solver import bypass
from ChromeOptions import performance
from fake_useragent import UserAgent
import random
import time

def delay():
	time.sleep(random.randint(1, 2))

def bot(name, mail, num):

	# Create an instance of a headless web driver of random useragent with our url destination
	driver = performance()
	driver.get("https://ourmosques.commonspaces.sg")
	driver.get_screenshot_as_file("screenshot.png")

	actions = ActionChains(driver)
	prayer_type = driver.find_element_by_xpath("//label[@for='typeof_prayer_1']")
	prayer_type.click()

	date = driver.find_element_by_xpath("//div[@ng-show='typeofprayer_id == 1']/div[@class='checkbox_group']/span[2]/label[1]")
	date.click()

	prayer_time = driver.find_element_by_xpath("//div[@ng-show='typeofprayer_id == 1 && daily_prayer_date']/div[@class='checkbox_group']/span[1]/label[1]")
	prayer_time.click()

	cluster= driver.find_element_by_xpath("//div[@ng-show='typeofprayer_id == 1 || typeofprayer_id == 2 || typeofprayer_id == 3 || typeofprayer_id == 4 || typeofprayer_id == 5']/div[@class='checkbox_group']/span[1]/label[1]")
	cluster.click()

	delay()
	mosque_selection = driver.find_element_by_xpath("//div[@ng-show='cluster_id >= 1']/ul[1]/li[7]")
	actions.move_to_element_with_offset(mosque_selection, 11, 17).click().perform()

	full_name = driver.find_element_by_xpath("//div[contains(@ng-class, 'bookingForm.first_person_name.$error.required')]/input[1]")
	full_name.send_keys(name)

	email = driver.find_element_by_xpath("//div[contains(@ng-class, 'bookingForm.contact_email.$error.required')]/input[1]")
	email.send_keys(mail)
	email_confirmation = driver.find_element_by_xpath("//div[contains(@ng-class, 'bookingForm.contact_email_confirmation.$error.required')]/input[1]")
	email_confirmation.send_keys(mail)

	contact_number = driver.find_element_by_xpath("//div[contains(@ng-class, 'bookingForm.contact_num.$error.required')]/input[1]")
	contact_number.send_keys(num)

	terms_checkbox = driver.find_element_by_xpath("//div[contains(@ng-class, 'bookingForm.termandcond.$error.required')]/div[@class='checkbox-custom checkbox-default']/input[1]")
	actions.move_to_element(terms_checkbox).click().perform()

	delay()
	ok_button = driver.find_element_by_xpath("//button[@class='btn btn_three btn-default mt-none bootbox-accept']")
	ok_button.click()

	driver.get_screenshot_as_file("captcha.png")
	bypass(driver)
	driver.get_screenshot_as_file("bypass.png")

	delay()
	driver.get_screenshot_as_file("bypass1.png")
	booking_submit_button = driver.find_element_by_xpath("//button[@id='booking__submit_btn']")
	booking_submit_button.click()
	driver.get_screenshot_as_file("success.png")

	print("Operation Successful!")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ourmosques.commonspaces.sg/")

daily_prayer = driver.find_element_by_id("typeof_prayer_1")
daily_prayer.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()

person_name = driver.find_element_by_name("first_person_name")
person_name.send_keys("test")
contact_email = driver.find_element_by_name("contact_email")
contact_email.send_keys("test@what.com")
contact_email_confirmation = driver.find_element_by_name("contact_email_confirmation")
contact_email_confirmation.send_keys("test@what.com")
contact_number = driver.find_element_by_name("contact_num")
contact_number.send_keys("84840303")


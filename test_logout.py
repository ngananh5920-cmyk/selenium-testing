from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "a.button").click()

time.sleep(2)

message = driver.find_element(By.ID, "flash").text

if "You logged out of the secure area!" in message:
    print("TC03 PASS - Logout Success")
else:
    print("TC03 FAIL")

driver.save_screenshot("TC03_LogoutSuccess.png")

time.sleep(2)
driver.quit()
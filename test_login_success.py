from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("TC01 PASS - Login Success")
else:
    print("TC01 FAIL")

driver.save_screenshot("TC01_LoginSuccess.png")

time.sleep(2)
driver.quit()
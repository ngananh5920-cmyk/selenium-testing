from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

message = driver.find_element(By.ID, "flash").text

if "Your username is invalid!" in message:
    print("TC02 PASS - Login Failed")
else:
    print("TC02 FAIL")

driver.save_screenshot("TC02_LoginFail.png")

time.sleep(2)
driver.quit()
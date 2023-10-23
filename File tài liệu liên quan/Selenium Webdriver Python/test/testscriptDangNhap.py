import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import csv
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://wordpress.com/log-in/")
time.sleep(2)
try:
    username = driver.find_element(By.NAME,'usernameOrEmail')
    username.send_keys("denmapkhung123")
    driver.find_element(By.CLASS_NAME,'form-button').click()
    driver.implicitly_wait(2)
    password = driver.find_element(By.NAME,'password')
    password.send_keys("Nguyenmanhphuong")
    driver.implicitly_wait(2)
    password.send_keys(Keys.ENTER)
    driver.implicitly_wait(2)
    print('dang nhap thanh cong')

except Exception as ex:
    print(ex)
    print("Dang nhap khong thanh cong")

driver.close()
driver.quit()
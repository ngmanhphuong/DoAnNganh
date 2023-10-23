import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://2051052105phuong.wordpress.com/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 250);")
time.sleep(2)
driver.find_element(By.CLASS_NAME,'wp-block-search__input').click()
time.sleep(2)
(driver.find_element(By.CLASS_NAME,'wp-block-search__input').send_keys("bảo hiểm"))
time.sleep(2)
driver.find_element(By.CLASS_NAME,'wp-block-search__button').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 250);")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="post-157"]/a/img').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 5200);")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="comment"]').click()
time.sleep(1)
(driver.find_element(By.XPATH,'//*[@id="comment"]')).send_keys("Bài báo rất bổ ích!")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="comment-form__verbum"]/div[2]/div/div/div/div[3]/div/div/label[1]/input').click()
(driver.find_element(By.XPATH,'//*[@id="comment-form__verbum"]/div[2]/div/div/div/div[3]/div/div/label[1]/input')).send_keys("denmapkhung123@gmail.com")
driver.find_element(By.XPATH,'//*[@id="comment-form__verbum"]/div[2]/div/div/div/div[3]/div/div/label[2]/input').click()
(driver.find_element(By.XPATH,'//*[@id="comment-form__verbum"]/div[2]/div/div/div/div[3]/div/div/label[2]/input')).send_keys("Phuong")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="comment-submit"]').click()
time.sleep(5)
driver.close()
driver.quit()
print("Binh luan thanh cong")
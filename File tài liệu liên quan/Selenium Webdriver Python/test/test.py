import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://2051052105phuong.wordpress.com/")
time.sleep(2)

print(driver.title)

articles = driver.find_elements(By.CSS_SELECTOR, 'div.site-content')
for item in articles:
    title = item.find_element(By.CSS_SELECTOR, 'h6.wp-block-heading').text
    link = item.find_element(By.CSS_SELECTOR, 'h6.wp-block-heading>a').get_attribute('href')
    image = item.find_element(By.CSS_SELECTOR, 'figure.wp-block-image>a').get_attribute('href')
    print(title)
    print(link)
    print(image)
    print('---------')
driver.close()
driver.quit()
print("Done")

# doc du lieu tu trang chu

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

driver.find_element(By.XPATH, '//*[@id="menu-item-30"]/a').click()
time.sleep(2)

results = driver.find_elements(By.CSS_SELECTOR, 'article.post')

for item in results:
    title = item.find_element(By.CSS_SELECTOR, 'h2.entry-title>a').text
    link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
    # content = item.find_element(By.TAG_NAME,'a').text
    print(title)
    print(link)
    # print(content)
    print('---------------')

driver.close()
driver.quit()
print("Done")



# lay ra title va link tung bai bao trong muc tong hop tin tuc
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
driver.find_element(By.XPATH, '//*[@id="menu-item-139"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,
                    '//*[@id="post-129"]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/h6/strong/a').click()
time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR, 'article.post')
for item in results:
    title = item.find_element(By.CSS_SELECTOR, 'h2.wp-block-heading').text
    content = item.find_element(By.TAG_NAME, 'p').text
    author = item.find_element(By.CSS_SELECTOR, 'p.has-text-align-right').text
    print(title)
    print(content)
    print(author)
    print('---------------')
driver.close()
driver.quit()
print("Done")

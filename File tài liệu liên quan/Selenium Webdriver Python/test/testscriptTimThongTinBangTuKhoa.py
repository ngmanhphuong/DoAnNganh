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

str = input("Nhap vao tu khoa can tim: ")

inp = driver.find_element(By.NAME,'s')
inp.send_keys(str)
inp.submit()

results = driver.find_elements(By.CSS_SELECTOR,'article.post')
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 2000);")

for item in results:
    try:
        content = item.find_element(By.CSS_SELECTOR,'h2.entry-title>a').text
        print(content)
        print('---------------')
    except NoSuchElementException:
        print('loi')

time.sleep(5)
driver.close()
driver.quit()
print("Done")

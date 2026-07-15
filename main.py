from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCond
import time
import datetime
# from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options) 

driver.implicitly_wait(10)
driver.get("https://www.scrapethissite.com/pages/simple/")
print(datetime.datetime.now().time())
# element = driver.find_element(By.XPATH, "//*[@id='main-content']/devsite-content/article/h1")
WebDriverWait(driver,20).until(
    ExCond.presence_of_element_located(
        (By.CLASS_NAME, 'country-name')
        )
    )

driver.get("https://facebook.com")
time.sleep(5)

driver.close()
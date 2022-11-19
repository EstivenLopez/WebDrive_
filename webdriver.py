from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https:/youtube.com')
def Tendencias():
    shorts = driver.find_element(By.LINK_TEXT,'Shorts').click()
Tendencias()
time.sleep(60)
driver.quit()

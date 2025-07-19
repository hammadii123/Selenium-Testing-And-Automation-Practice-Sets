from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get("hhtps://demoqa.com/alerts")

driver.find_element(By.ID,"alertButton").click()
time.sleep(2)

driver.find_element(By.ID,"timerAlert").click()
time.sleep(6)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"confirmBtn").click()
time.sleep(2)
driver.switch_to.alert.dismiss()




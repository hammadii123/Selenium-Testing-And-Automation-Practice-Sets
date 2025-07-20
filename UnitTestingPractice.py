import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class TestLoginForm:
    def setUp(self):
        driver=webdriver.Chrome()
        driver.get("//https:www.example.com")
        driver.maximize_window()

    def test_positive_valid_username(self):
        driver=self.driver
        driver.find_element(By.ID,"username").send_keys("SE-2022f")
        driver.find_element(By.ID,"password").send_keys("1234")
        driver.find_element(By.ID,"submitBtn").click()
        self.assertIn("Dashboard",driver.title)
        time.sleep(2)


    def test_positive_invalid_username1(self):
        driver=self.driver
        driver.find_element(By.ID,"username").send_keys("12")

        driver.find_element(By.ID,"password").send_keys("correct password")
        driver.find_element(By.ID,"submitBtn").click()

        self.assertIn("Dashboard",driver.title)

        time.sleep(2)

        error_msg=driver.find_element(By.XPATH,"//div[@id=asa]")
        error_msg=driver.find_element(By.XPATH,"//*[contains(text(),'Login failed')]")

        self.assertTrue(error_msg.is_displayed())

    def test_negative_invalid_password(self):
        driver=self.driver
        driver.find_element(By.ID,"username").send_keys("hammad")
        driver.find_element(By.ID,"password").send_keys("123")


        driver.find_element(By.ID,"submitBtn").click()
        
        error_msg=driver.find_element(By.XPATH,"//*[contains(text(),'login failed')]")
        self.assertTrue(error_msg.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ =="__main__":
    unittest.main()






    
        
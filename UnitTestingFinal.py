# import unittest
# from selenium.webdriver.common.by import By
# from selenium import webdriver


# class UnitTest(unittest.TestCase):

#     def setUp(self):
#         self.driverdriver=driver
#         driver=webdriver.Chrome()
#         driver.get('https:www,eample.com')

#     def test_positive_accountNumber1(self):
#         driver=self.driver
#         driver.find_element(By.ID,"account_number").send_keys("1212121232134")

#     def test_negative_accountNumber1(self):
#         self.driver.find(By.ID,"account_number").send_keys("")
#         self.assertIn("dashboard",self.driver.title)

#     def test_negative_accountNumber1(self):
#         self.driver.find(By.ID,"account_number").send_keys("ab")
#         error_msg=self.driver.find_element("//[contains(text(),'Register failed')]")
#         self.assertTrue(error_msg.display())


    
    
# 2)))
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.driverdriver=driver
        driver=webdriver.Chrome()
        driver.get('https:www,eample.com')

    def test_positive_accountNumber1(self):
        driver=self.driver
        driver.find_element(By.ID,"account_number").clear()
        driver.find_element(By.ID,"account_number").send_keys("1212121232134")

        # 2)
        driver.find_element(By.ID,"consumer_number").clear()
        driver.find_element(By.ID,"consumer_number").send_keys("23432")
        # 3)
        driver.find_element(By.ID,"mobile_number").clear()
        driver.find_element(By.ID,"mobile_number").send_keys("03321232223")
        # 4)
        driver.find_element(By.ID,"consumer_name").clear()
        driver.find_element(By.ID,"consumer_name").send_keys("Hammad")
        # 5)
        driver.find_element(By.ID,"consumer_address").clear()
        driver.find_element(By.ID,"consumer_address").send_keys("Karachi")
        # 6)
        driver.find_element(By.ID,"complaintType").clear()
        driver.find_element(By.ID,"complaintType").send_keys("Refund")
        # 7)
        driver.find_element(By.ID,"complaint_description").clear()
        driver.find_element(By.ID,"complaint_description").send_keys("Hello i wanna refund of my money")

        # 8)Register button if any:
        driver.find_element(By.ID,"submit").click()

        driver.assertIn("Submitted",driver.title)


# Negative1:empty field
def test_negative_empty_fields(self):
    driver = self.driver
    driver.find_element(By.ID, "account_number").clear()
    driver.find_element(By.ID, "account_number").send_keys("")

    driver.find_element(By.ID, "consumer_number").clear()
    driver.find_element(By.ID, "consumer_number").send_keys("")

    driver.find_element(By.ID, "mobile_number").clear()
    driver.find_element(By.ID, "mobile_number").send_keys("")

    driver.find_element(By.ID, "consumer_name").clear()
    driver.find_element(By.ID, "consumer_name").send_keys("")

    driver.find_element(By.ID, "consumer_address").clear()
    driver.find_element(By.ID, "consumer_address").send_keys("")

    driver.find_element(By.ID, "complaintType").clear()
    driver.find_element(By.ID, "complaintType").send_keys("")

    driver.find_element(By.ID, "complaint_description").clear()
    driver.find_element(By.ID, "complaint_description").send_keys("")

    driver.find_element(By.ID, "submit").click()

    # Validate error message or unsuccessful submission
    self.assertNotIn("Submitted", driver.title)

# Negative Test Case 2: Invalid Account & Consumer Numbers
def test_negative_invalid_account_consumer(self):
    driver = self.driver
    driver.find_element(By.ID, "account_number").clear()
    driver.find_element(By.ID, "account_number").send_keys("abc123")  # not 13 digits

    driver.find_element(By.ID, "consumer_number").clear()
    driver.find_element(By.ID, "consumer_number").send_keys("!@#$$")  # special characters

    driver.find_element(By.ID, "mobile_number").clear()
    driver.find_element(By.ID, "mobile_number").send_keys("03123")  # too short

    driver.find_element(By.ID, "consumer_name").clear()
    driver.find_element(By.ID, "consumer_name").send_keys("12345")  # numeric name

    driver.find_element(By.ID, "consumer_address").clear()
    driver.find_element(By.ID, "consumer_address").send_keys("###")  # invalid address

    driver.find_element(By.ID, "complaintType").clear()
    driver.find_element(By.ID, "complaintType").send_keys("123")  # invalid

    driver.find_element(By.ID, "complaint_description").clear()
    driver.find_element(By.ID, "complaint_description").send_keys("")  # empty description

    driver.find_element(By.ID, "submit").click()

    self.assertNotIn("Submitted", driver.title)


# Negative Test Case 3: Invalid Mobile Format & Long Complaint
def test_negative_invalid_mobile_and_description(self):
    driver = self.driver
    driver.find_element(By.ID, "account_number").clear()
    driver.find_element(By.ID, "account_number").send_keys("1212121232134")

    driver.find_element(By.ID, "consumer_number").clear()
    driver.find_element(By.ID, "consumer_number").send_keys("23432")

    driver.find_element(By.ID, "mobile_number").clear()
    driver.find_element(By.ID, "mobile_number").send_keys("12345678901")  # does not start with 03

    driver.find_element(By.ID, "consumer_name").clear()
    driver.find_element(By.ID, "consumer_name").send_keys("Hammad")

    driver.find_element(By.ID, "consumer_address").clear()
    driver.find_element(By.ID, "consumer_address").send_keys("Karachi")

    driver.find_element(By.ID, "complaintType").clear()
    driver.find_element(By.ID, "complaintType").send_keys("Refund")

    # Very long complaint description (assume max 255 characters allowed)
    long_description = "a" * 500
    driver.find_element(By.ID, "complaint_description").clear()
    driver.find_element(By.ID, "complaint_description").send_keys(long_description)

    driver.find_element(By.ID, "submit").click()

    self.assertNotIn("Submitted", driver.title)
   
    


if __name__== "_main_":
    unittest.main()

        





        



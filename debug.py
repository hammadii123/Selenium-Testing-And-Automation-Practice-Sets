# # 2a
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# driver=webdriver.chrome()


# from selenium.webdriver.common.by import By

# class Practice():

#     def __init__(self):
#         self.driver=driver
#         self.firstname_id="firstName"
#         self.lastname_id="lastName"
#         self.email_id="lastName"

#     def enter_firstName(self,data):
#         self.driver.find_element(By.ID,self.firstname_id).clear()




# # # 2))
# # from webdriver_manager import ChromeDriverManager

# # driver=webdriver_manager(ChromeDriverManager()).install()



# 3)
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver= webdriver.Chrome()

# driver.get("https://www.google.com")

# driver.find_element(By.ID,"username").send_keys("hammad")
# driver.find_element(By.ID,"pass").send_keys("hammad123")
# driver.find_element(By.ID,"loginBtn").click()

# driver.quit()



# 4))
from selenium.webdriver.common import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver=ChromeDriverManager().install()


driver.find_element(By.ID,"alertBtn").click()
time.sleep(2)

driver.switch_to.alert.accept()


driver.find_element(By.ID,"timeAlert").click()
time.sleep(6)

driver.switch_to.alert.accept()

driver.find_element(By.ID,"confirm").click()
time.sleep(2)

driver.switch_to.alert.dismiss()


driver.find_element(By.ID,"alertBtn").click()
time.sleep(2)

alert=driver.switch_to.alert
alert.send_keys("Password")
alert.accept()


time.sleep(2)

driver.quit()


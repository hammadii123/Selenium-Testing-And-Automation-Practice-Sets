from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

class DragPage:
    def _init_(self,driver):
        self.driver=driver

        self.drag_source=(By.XPATH,"//div[@id=draggable]")
        self.drag_target=(By.XPATH,"//div[@id=droppable]")


    def perform_drag_and_drop(self):
        source=self.driver.find_element(*self.drag_source)
        target=self.driver.find_element(*self.drag_target)

        actions=ActionChains(self.driver)
        actions.drag_and_drop(source,target).perform()
# test scrpit

driver=webdriver.Chrome()
driver.get("https://www.example.com")
drag_test=DragPage(driver)

print("Testing start hogyi he")
drag_test.perform_drag_and_drop()


time.sleep(2)



# Form class
class FormPage:
    def __init__(self,driver):
        self.driver=driver

        self.first_name=(By.ID,"firstName")
        self.last_name=(By.ID,"lastName")
        self.phone=(By.ID,"Phone")
        self.email=(By.ID,"Email")
        self.password=(By.ID,"Password")
        self.country=(By.ID,"Country")
        self.state=(By.ID,"State")
        self.city=(By.ID,"City")
        self.fax=(By.ID,"Fax")
        self.postal_code=(By.ID,"Postal_code")
        self.submitBtn=(By.ID,"submit_btn")

    def fill_form(self,data):
        self.driver.find(*self.first_name).send_keys(data["first_name"])
        self.driver.find(*self.lastName).send_keys(data["lastName"])
        self.driver.find(*self.phone).send_keys(data["Phone"])
        self.driver.find(*self.email).send_keys(data["Email"])
        self.driver.find(*self.password).send_keys(data["Password"])
        self.driver.find(*self.country).send_keys(data["Country"])
        self.driver.find(*self.state).send_keys(data["State"])
        self.driver.find(*self.city).send_keys(data["City"])
        self.driver.find(*self.fax).send_keys(data["Fax"])
        self.driver.find(*self.postal_code).send_keys(data["Postal_code"])

    def submitForm(self):
        self.driver.find_element(*self.submitBtn).click()




# Form Testing

driver.get("https://www.formExample.com")
form_test=FormPage(driver)

form_data={
    'first_name':"Hammad",
    'lastName':'Mustafa',
    'Email':'hammadworks123@gmail.com',
    'Country':'Pakistan',
    'State':'xyz',
    'City':'Karachi',
    'Fax':'abc',
    'Postal_code':'123'

}
form_test.fill_form(form_data)
form_test.submitForm()
print("automation test completed")

time.sleep(5)


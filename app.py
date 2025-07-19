from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragPage:
    def _init_(self,driver):
        self.driver=driver

        self.drag_source=(By.XPATH,"//div[@id=draggable]")
        self.drag_target=(By.XPATH,"//div[@id=droppable]")


    def perform_drag_and_drop(self):
        source=self.driver.find_element(*self.drag_source)
        target=self.driver.find_element(*self.drag_target)

        actions=ActionChains(self.driver)
        ActionChains.drag_and_drop(source,target).perform()
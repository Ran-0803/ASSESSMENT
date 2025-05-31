"""
LoginPage contains the methods related to the login page only
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

# import the data and locators
from TestData.data import TodoData
from TestLocators.locators import TodoLocators
from selenium.webdriver.common.keys import Keys

class Todo:

    driver = webdriver.Chrome()

    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(TodoData.url)
        self.driver.set_page_load_timeout(10)
        self.action = ActionChains(self.driver)
        return True
    
    def enter_text(self,textValue):
        self.wait = WebDriverWait(self.driver,10)
        element = self.wait.until(ec.presence_of_element_located((By.ID, TodoLocators.textBox)))
        element.clear()
        element.send_keys(textValue)
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        return True

    def delete_Item(self):
        self.wait = WebDriverWait(self.driver,10)
        document = self.wait.until(ec.presence_of_element_located(By.ID))
        self.action.move_to_element(document).perform()
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, TodoLocators.first_item)))
        element.click()
        time.sleep(3)

    def complete_item(self):
        self.wait = WebDriverWait(self.driver, 10)
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, TodoLocators.second_item)))
        element.click()
        time.sleep(3)



    def shutdown(self):
        self.driver.quit()
        return None

"""
test_login file contains all the test cases
"""
from PageObjects.LoginPage import Todo
from TestData.data import TodoData

from TestLocators.locators import TodoLocators


def test_enterItems():
    Todo().start()
    Todo().enter_text(TodoData.data1)
    Todo().enter_text(TodoData.data2)
    Todo().enter_text(TodoData.data3)
    Todo().complete_item()
    Todo().delete_Item()







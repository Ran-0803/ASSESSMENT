"""
Locators file used to store all the web locators
"""
class TodoLocators:
    textBox = 'todo-input'
    first_item = '//label[text()="Buy Milk"]//following-sibling::button'
    second_item = '//label[text()="Buy Groceries"]//preceding-sibling::input'
    delete_item = "(//ul[@class='todo-list']//li[@data-testid='todo-item'])[1]//button[@class='destroy']"



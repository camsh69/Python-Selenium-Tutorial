from config import driver
from selenium.webdriver.common.by import By

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.NAME, 'radioButton')
radioButtons[1].click()
assert radioButtons[1].is_selected()

displayText = driver.find_element(By.ID, 'displayed-text')
assert displayText.is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not displayText.is_displayed()

driver.quit()

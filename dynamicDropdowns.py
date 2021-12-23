from config import driver
from selenium.webdriver.common.by import By
import time

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

menu = driver.find_element(By.ID, 'autosuggest')
menu.send_keys('Ind')
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
for country in countries:
    if country.text == 'India':
        country.click()
        break

assert menu.get_attribute('value') == 'India'

driver.quit()

from config import driver
from selenium.webdriver.common.by import By
import time

driver.get('https://rahulshettyacademy.com/seleniumPractise/')


driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys('ber')
time.sleep(3)

count = len(driver.find_elements(
    By.CSS_SELECTOR, "[class='products'] div.product"))
assert count == 3

addToCartBtns = driver.find_elements(
    By.CSS_SELECTOR, '.product-action button')
for button in addToCartBtns:
    button.click()

driver.find_element(By.CSS_SELECTOR, '.cart-icon').click()

driver.find_element(
    By.CSS_SELECTOR, '.cart-preview div button').click()

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys(
    'rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)

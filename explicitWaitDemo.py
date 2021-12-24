from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://rahulshettyacademy.com/seleniumPractise/')


driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys('ber')

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

wait = WebDriverWait(driver, 5)
promoCode = driver.find_element(By.CSS_SELECTOR, '.promoCode')
wait.until(EC.element_to_be_clickable(promoCode))
promoCode.send_keys('rahulshettyacademy')

driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

wait = WebDriverWait(driver, 5)
promoInfo = driver.find_element(By.CSS_SELECTOR, '.promoInfo')
wait.until(EC.visibility_of(promoInfo))
print(promoInfo.text)

driver.quit()

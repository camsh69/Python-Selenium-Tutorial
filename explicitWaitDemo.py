from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://rahulshettyacademy.com/seleniumPractise/')


driver.find_element(By.CSS_SELECTOR, "[type='search']").send_keys('ber')

count = len(driver.find_elements(
    By.CSS_SELECTOR, '.products div.product'))
assert count == 3

list = []
addToCartBtns = driver.find_elements(
    By.CSS_SELECTOR, '.product-action button')
for button in addToCartBtns:
    list.append(button.find_element(
        By.XPATH, "parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element(By.CSS_SELECTOR, '.cart-icon').click()

driver.find_element(
    By.CSS_SELECTOR, '.cart-preview div button').click()

wait = WebDriverWait(driver, 5)
promoCode = driver.find_element(By.CSS_SELECTOR, '.promoCode')
wait.until(EC.element_to_be_clickable(promoCode))
discountTextPre = driver.find_element(By.CLASS_NAME, 'discountAmt').text
promoCode.send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

list2 = []
veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veggie in veggies:
    list2.append(veggie.text)
print(list2)
assert list == list2

wait = WebDriverWait(driver, 5)
promoInfo = driver.find_element(By.CSS_SELECTOR, '.promoInfo')
wait.until(EC.visibility_of(promoInfo))
print(promoInfo.text)

discountCodePost = driver.find_element(By.CLASS_NAME, 'discountAmt').text
print(discountTextPre, discountCodePost)
assert discountTextPre > discountCodePost

amounts = 0
totals = driver.find_elements(
    By.CSS_SELECTOR, "tbody tr td:nth-child(5)")
for total in totals:
    amounts += int(total.text)
print(amounts)

totalAmt = driver.find_element(By.CLASS_NAME, 'totAmt').text
print(totalAmt)

assert amounts == int(totalAmt)


driver.quit()

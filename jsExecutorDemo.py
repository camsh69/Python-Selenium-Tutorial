from config import driver
from selenium.webdriver.common.by import By

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME, 'name').send_keys('Campbell')
print(driver.find_element(By.NAME, 'name').get_attribute('value'))

print(driver.execute_script(
    'return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# driver.quit()

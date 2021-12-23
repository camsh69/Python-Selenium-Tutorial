from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, 'name').send_keys("Campbell")
# driver.find_element(By.NAME, 'email').send_keys('dummy@email.com')
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(
    'dummy@email.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('Password')
driver.find_element(By.ID, 'exampleCheck1').click()

dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
# dropdown.select_by_index(0)


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
# print(driver.find_element(
#     By.XPATH, "//*[contains(@class, 'alert-success')]").text)
# print(driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text)

assert "success" in message

driver.quit()

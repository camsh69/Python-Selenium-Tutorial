from config import driver
from selenium.webdriver.common.by import By

driver.get('https://login.salesforce.com/?locale=uk')

driver.find_element(By.CSS_SELECTOR, '#username').send_keys("Campbell")
driver.find_element(By.CSS_SELECTOR, '.password').send_keys('Password')
driver.find_element(By.CSS_SELECTOR, '.password').clear()
driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()
# driver.find_element(By.XPATH, "//*[text()='Need Help Logging In?']").click()
driver.find_element(By.NAME, 'cancel').click()
print(driver.find_element(
    By.XPATH, "//form[@id='login_form']/div[1]/label").text)
# print(driver.find_element(By.CSS_SELECTOR, "#login_form label:nth-child(4)").text)

driver.quit()

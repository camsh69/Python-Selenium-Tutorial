from config import driver
from selenium.webdriver.common.by import By

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

inputBox = driver.find_element(By.ID, 'name')
alertButton = driver.find_element(By.ID, 'alertbtn')
confirmBtn = driver.find_element(By.ID, 'confirmbtn')
validateText = 'Campbell'

inputBox.send_keys("Campbell")
alertButton.click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()

inputBox.send_keys('Campbell')
confirmBtn.click()
alert = driver.switch_to.alert
alert.dismiss()

driver.quit()

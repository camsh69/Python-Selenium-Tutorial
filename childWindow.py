from config import driver
from selenium.webdriver.common.by import By

driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element(By.LINK_TEXT, 'Click Here').click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, 'h3').text


driver.quit()

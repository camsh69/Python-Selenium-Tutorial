from config import driver
from selenium.webdriver.common.by import By

driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys('I am able to automate')
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME, 'h3').text)

driver.quit()

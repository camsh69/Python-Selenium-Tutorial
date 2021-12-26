from config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
action = ActionChains(driver)
menu = driver.find_element(By.ID, 'mousehover')
action.move_to_element(menu).perform()
childMenu = driver.find_element(By.LINK_TEXT, 'Top')
action.move_to_element(childMenu).click().perform()


driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
action = ActionChains(driver)
button = driver.find_element(By.ID, 'double-click')
action.double_click(button).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

driver.quit()

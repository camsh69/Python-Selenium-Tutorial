from config import driver, options
from selenium.webdriver.common.by import By

options.add_argument('--start-maximised')
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')

driver.get('https://rahulshettyacademy.com/angularpractice/')

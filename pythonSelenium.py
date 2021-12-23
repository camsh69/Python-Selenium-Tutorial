from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\camsh\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# service = Service("C:\\Users\\camsh\\Webdrivers\\geckodriver.exe")
# driver = webdriver.Firefox(service=service)
# service = Service("C:\\Users\\camsh\\Webdrivers\\msedgedriver.exe")
# driver = webdriver.Edge(service=service)
# service = Service("C:\\Users\\camsh\\Webdrivers\\IEDriverServer.exe")
# driver = webdriver.Ie(service=service)


driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()

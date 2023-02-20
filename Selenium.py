from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# /Users/bberreby/Downloads/chromedriver_mac64
driver = webdriver.Chrome(service=Service("/Users/bberreby/Downloads/chromedriver_mac64/chromedriver"))
driver.get('http://ynet.co.il')
driver.maximize_window()
driver.minimize_window()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/bberreby/Downloads/chromedriver_mac64/chromedriver")

# Question 1,2
# driver.get('http://www.walla.co.il')
# web_title = driver.title
# print(web_title)
# driver.refresh()

# Question 3
# Elements remain equal/equivalent between two browsers instances.

# Question 4
# driver.get('https://translate.google.com/')
# driver.find_element(By.XPATH, "//textarea").send_keys('ברונו')

# Question 5
# driver.get('https://youtube.com/')
# driver.find_element(By.NAME, 'search_query').send_keys('Guitar')
# driver.find_element(By.ID, 'search-icon-legacy').click()

# Question 6
# driver.get('https://translate.google.com/')
# driver.find_element(By.CSS_SELECTOR, "textarea[aria-autocomplete='list']").send_keys('שלום')
# driver.find_element(By.CSS_SELECTOR, "textarea[role='combobox']").send_keys('לך')
# driver.find_element(By.XPATH, "//textarea").send_keys('ברונו')
# input()

# Challenges - Question 8
# driver.delete_all_cookies()
# print(driver.get_cookies())



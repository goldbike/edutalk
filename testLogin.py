__author__ = 'dustinlee'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox()
driver = webdriver.Chrome('chromedriver')

driver.get("http://www.daehyunlee.com")
assert "이대현" in driver.title
login = driver.find_element_by_css_selector('input.button')
login.click()


username = driver.find_element_by_id('focus__this')
username.send_keys('dustinlee')

password = driver.find_element_by_name('p')
password.send_keys('sisa0822')

login = driver.find_element_by_css_selector('input.button')
login.click()

logout = driver.find_elements_by_css_selector('form.button.btn_logout')
#logout.click()

print(logout)

for e in logout:
    print(e)

driver.close()






from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://github.com/login')

elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys("example@gamil.com")

elem = driver.find_element_by_name("Password")
elem.clear()

elem = driver.find_element_by_name("commit")
elem.click()
time.sleep(5)

elem = driver.find_element_by_name("login")
elem.clear()

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("12345678")

elem = driver.find_element_by_name("commit")
elem.click()
time.sleep(5)

elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys("example@gamil.com")

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("12345678")

elem = driver.find_element_by_name("commit")
elem.click()
time.sleep(5)

assert "no result found ." not in driver.page_source

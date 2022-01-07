from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/maximus/Documents/dev_doc/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
url = "http://secure-retreat-92358.herokuapp.com"

driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("alex")
last_name.send_keys("m")
email.send_keys("tes@test.com")
submit.click()

# count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
# # count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# driver.quit()

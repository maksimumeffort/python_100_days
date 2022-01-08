from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = "/Users/maximus/Documents/dev_doc/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service=s)

EMAIL = "maksdevil@hotmail.co.uk"
PASS = "Throwaway2021@"

URL = "https://www.linkedin.com/jobs/search/?geoId=104001115&keywords=python%20developer&location=Brisbane%20City%2C%20QL"

driver.get(URL)

# login
sign_in = driver.find_element(By.CSS_SELECTOR, "div.nav__cta-container a.nav__button-secondary")
sign_in.click()

# time.sleep(5)

user = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
submit = driver.find_element(By.CLASS_NAME, "btn__primary--large")
user.send_keys(EMAIL)
password.send_keys(PASS)
submit.click()

# run through the list of job ads and find the first one that has easy apply

search_results_list = driver.find_element(By.CSS_SELECTOR, "ul.jobs-search-results__list")
search_result_items = search_results_list.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
results = []
for result in search_result_items:
    res_id = result.get_attribute("id")
    print(res_id)



# easy_apply = driver.find_element(By.XPATH, '//*[@id="ember303"]/div/div/ul/li[3]')
# print(easy_apply.text)


# print(search_result_items)



# print(len(search_result_items))

# apply_btns = driver.find_elements(By.CSS_SELECTOR, "div.jobs-apply-button--top-card")
# btns_text_list = []
# for btn in apply_btns:
#     btns_text_list.append(btn.find_element(By.CSS_SELECTOR, "span").text)
# print(btns_text_list)

driver.quit()

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

time.sleep(3)

user = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
submit = driver.find_element(By.CLASS_NAME, "btn__primary--large")

user.send_keys(EMAIL)

password.send_keys(PASS)

submit.click()

# OPTION 1: run through the list of job ads and find the first one that has easy apply

# search_results_list = driver.find_element(By.CSS_SELECTOR, "ul.jobs-search-results__list")
# search_result_items = search_results_list.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
# for result in search_result_items:
#     res_id = result.get_attribute("id")
#     print(res_id)
#     # data_job_id = driver.find_element(By.XPATH, f"//*[@id={res_id}]/div/div").get_attribute("data-job-id")
#     # print(data_job_id)



# easy_apply = driver.find_element(By.XPATH, '//*[@id="ember303"]/div/div/ul/li[3]')
# print(easy_apply.text)


# print(search_result_items)



# print(len(search_result_items))

# apply_btns = driver.find_elements(By.CSS_SELECTOR, "div.jobs-apply-button--top-card")
# btns_text_list = []
# for btn in apply_btns:
#     btns_text_list.append(btn.find_element(By.CSS_SELECTOR, "span").text)
# print(btns_text_list)

## OPTION 2: click through the list, check if text == "easy apply", if not move to next item in list
time.sleep(10)

item_list = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

text_list = []
for item in item_list:
    time.sleep(2)
    item.click()
    item_desc = driver.find_element(By.CSS_SELECTOR, "div.jobs-unified-top-card__content--two-pane")
    print("found description")
    item_title = item_desc.find_element(By.TAG_NAME, "h2").text
    text_list.append(item_title)
# apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button span")
print(text_list)
driver.quit()

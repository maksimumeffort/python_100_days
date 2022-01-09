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
PHONE = "459840931"

URL = "https://www.linkedin.com/jobs/search/?currentJobId=2866113243&geoId=104001115&keywords=python%20developer&location=Brisbane%20City%2C%20QL"

driver.get(URL)

# login
sign_in = driver.find_element(By.CSS_SELECTOR, "div.nav__cta-container a.nav__button-secondary")
sign_in.click()

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

# find_application_mode function
def find_application_mode(item):
    item.click()
    item_desc = driver.find_element(By.CSS_SELECTOR, "div.jobs-unified-top-card__content--two-pane")
    # need to sleep so that "apply" element loads
    time.sleep(1)
    # item_title = item_desc.find_element(By.TAG_NAME, "h2").text
    item_spans = item_desc.find_elements(By.TAG_NAME, 'span')
    span_text_list = []
    # go through the list of spans and pick out their Apply mode
    for span in item_spans:
        if "Apply" in span.text:
            span_text_list.append(span.text)
        # makes sure applied jobs showing up in the list to not mess up the index of apply modes
        elif f"Applied" in span.text:
            span_text_list.append("Applied")
    if len(span_text_list) != 1:
        span_text_list.pop()
    apply_modes.append(span_text_list)
    # print(f"{span_text_list} added")


time.sleep(10)

# get a list of application modes
search_results = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
apply_modes = []
for result in search_results:
    find_application_mode(result)
    # print("apply mode added")

# find index of first list item with apply_mode = "Easy Apply"
# flatten the apply_modes list
mode_list_flat = [item for sub_list in apply_modes for item in sub_list]

# # find the first value in item_list with value "Easy Apply"
easy_apply_indices = [n for n in range(len(mode_list_flat)) if mode_list_flat[n] == "Easy Apply"]
# print(easy_apply_indices)
# print(mode_list_flat.index('Applied'))
for index in easy_apply_indices:
    search_results[index].click()

    # # application process
    apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
    apply_btn.click()
    time.sleep(2)

    # find the phone input field and give phone value
    phone_input = driver.find_element(By.TAG_NAME, "input")
    phone_input.send_keys(PHONE)

    # # click submit
    # submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button")
    # submit_button.click()

    # click exit
    exit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
    exit_button.click()
    discard_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
    discard_button.click()



# needed_index = mode_list_flat.index('Easy Apply')
# first_easy_app = search_results[needed_index]
# first_easy_app.click()
# print("found first easy app")
#
#

driver.quit()


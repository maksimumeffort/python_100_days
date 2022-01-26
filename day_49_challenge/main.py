from selenium import webdriver
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = "/Users/maximus/Documents/dev_doc/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service=s)

EMAIL = os.environ["EMAIL"]
PASS = os.environ["PASS"]
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


## OPTION 2: click through the list, check if text == "easy apply", if not move to next item in list

# find_application_mode function
def find_application_mode(item):
    item.click()
    item_desc = driver.find_element(By.CSS_SELECTOR, "div.jobs-unified-top-card__content--two-pane")
    # need to sleep so that "apply" element loads
    time.sleep(3)
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
    if len(span_text_list) >= 1:
        span_text_list.pop()

    apply_modes.append(span_text_list)
    # print(f"{span_text_list} added")

# Check for Modal
def modal_check():
    modal = driver.find_element(By.CSS_SELECTOR, "div.artdeco-modal")
    print(modal)

time.sleep(10)

# get a list of application modes

applications_info_list = []

search_results = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
apply_modes = []
for result in search_results:
    find_application_mode(result)

print(apply_modes)

# find index of first list item with apply_mode = "Easy Apply"
# flatten the apply_modes list
mode_list_flat = [item for sub_list in apply_modes for item in sub_list]

# # find the first value in item_list with value "Easy Apply"
easy_apply_indices = [n for n in range(len(mode_list_flat)) if mode_list_flat[n] == "Easy Apply"]
print(easy_apply_indices)
# print(mode_list_flat.index('Applied'))

for index in easy_apply_indices[0:1]:
    search_results[index].click()
    time.sleep(5)
    title = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div")
    print(title)

# for index in easy_apply_indices:
#     search_results[index].click()
#     # # read application info
#
#     job_info = driver.find_element(By.CSS_SELECTOR, "div.jobs-unified-top-card")
#     print(job_info)
#
#     job_title = job_info.find_element(By.CSS_SELECTOR, "h2")
#     print(job_title)
#
#     # new_application = {
#     #     "job_title":
#     #     "Job location"
#     #     "Method of Contact"
#     #     "Employer Name"
#     #     "Employer Contact"
#     #     "Notes"
#     # }
#
#
#     # # application process
#     apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
#     apply_btn.click()
#     time.sleep(2)
#
#     # find the phone input field and give phone value
#     phone_input = driver.find_element(By.TAG_NAME, "input")
#     phone_input.send_keys(PHONE)
#
#     # # click submit
#     # submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button")
#     # submit_button.click()
#
#     # click exit
#     exit_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
#     exit_button.click()
#     discard_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[1]")
#     discard_button.click()



# driver.quit()


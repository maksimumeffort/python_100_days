from selenium import webdriver
import os

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from random import randint
import re

EMAIL = os.environ['EMAIL']
PASS = os.environ['PASS']
counter = 20

# FUNCTIONS

def delay():
    time.sleep(randint(3, 10))


def swipe_right(x):
        x.click()
        delay()


def log_in(driver):
    # login
    login_btn = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
    login_btn.click()
    delay()
    # choose facebook
    facebook_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
    facebook_btn.click()

    # access facebook identifier
    tinder_window = driver.window_handles[0]
    fb_window = driver.window_handles[1]
    delay()
    driver.switch_to.window(fb_window)

    # print(tinder_window)
    # print("\n\n")
    # print(fb_window)
    delay()

    # find input field and send input values
    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "pass")
    fb_login = driver.find_element(By.NAME, "login")
    username.send_keys(EMAIL)
    # delay()
    password.send_keys(PASS)
    # delay()
    fb_login.click()
    delay()
    driver.switch_to.window(tinder_window)


def dismiss_notifications(driver):
    # allow location
    delay()
    modal = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div")
    # click allow
    allow = modal.find_element(By.TAG_NAME, "button")
    allow.click()
    delay()
    # dismiss notifications
    not_int_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
    not_int_btn.click()
    delay()
    # allow cookies
    accept_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
    accept_btn.click()
    delay()


# swipe left/swipe right
def find_buttons(driver):
    try:
        btns = driver.find_elements(By.TAG_NAME, "button")
        print("found buttons")
    except InvalidSelectorException:
        print("modal detected?")
        buttons = driver.find_elements(By.CSS_SELECTOR, "[role*='dialog' button]")
        print("modal detected")
        print(buttons)
    else:
        print(len(btns))
        main_btns = [btn for btn in btns[-5:]]
        # if len(btns) == 22:
        #     return main_btns[1]
        # print(main_btns[2])
        return main_btns[2]

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')

path = "/Users/maximus/Documents/dev_doc/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service=s, options=chrome_options)
URL = "https://tinder.com/app/recs"

driver.get(url=URL)
delay()

log_in(driver)
dismiss_notifications(driver)

## TODO: 1. Create a dictionary of all matches

#get the tab_panel element
delay()
tab_panels = driver.find_elements(By.CSS_SELECTOR, "[role*=tabpanel]")

# tab_panels[0] == "Matches"
match_tabs = tab_panels[0].find_elements(By.CSS_SELECTOR, "div.D\(f\).Fxw\(w\)")

delay()
# go through list of cards counting number in each matches_tab
match_cards = [tab.find_elements(By.CSS_SELECTOR, "div.P\(8px\)") for tab in match_tabs]
match_cards_flat = [match for sublist in match_cards for match in sublist]

match_list = []

# check if first match == https://tinder.com/app/likes-you
has_potential_matches = match_cards_flat[0].find_element(By.TAG_NAME, "a").get_attribute('href') == "https://tinder.com/app/likes-you"

# if has_potential_matches:
#     match_cards_flat.pop(0)
#
# for match in match_cards_flat:
#     name = match.find_element(By.CSS_SELECTOR, "div.Ell").text.title()
#     picture_element = match.find_element(By.CSS_SELECTOR, "div.D\(b\).Pos\(r\).Expand").get_attribute("style")
#     regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#     picture_link = re.findall(regex, picture_element)[0][0]
#     dict_item = {"Name": name, "Picture": picture_link}
#     match_list.append(dict_item)

# tab_panels[1] == "Messages"

## TODO: 2. Enable to send messages to matches
message=""
match_cards_flat[1].click()
# send messages to matches
message_form = driver.find_element(By.TAG_NAME, "form")
text_area = message_form.find_element(By.TAG_NAME, "textarea")
send_button = message_form.find_element(By.TAG_NAME, "button")

text_area.send_keys(message)
send_button.click()



# while counter > 0:
#     try:
#         like_btn = find_buttons(driver)
#     except ElementNotInteractableException or ElementClickInterceptedException:
#             print("checking if matched")
#             exit_match = driver.find_element(By.CSS_SELECTOR, "[title*='Back to Tinder']")
#             exit_match.click()
#     else:
#         swipe_right(like_btn)
#         print("liked")
#         print(counter)
#         counter -= 1

# driver.quit()


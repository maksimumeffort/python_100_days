import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = '/Users/maximus/Documents/dev_doc/chromedriver'
SIMILAR_ACCOUNT = 'memeschemez'
USERNAME = os.environ['USER']
PASSWORD = os.environ['PASS']
INSTA_URL = 'https://www.instagram.com/accounts/login/'
S = Service(DRIVER_PATH)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=S)
        self.scroll_count = 10

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(3)
        # username
        user_input = self.driver.find_element(By.NAME, 'username')
        user_input.send_keys(USERNAME)
        # password
        pass_input = self.driver.find_element(By.NAME, 'password')
        pass_input.send_keys(PASSWORD)
        # click login
        time.sleep(5)
        login_btn = self.driver.find_elements(By.TAG_NAME, 'button')[1]
        login_btn.click()

    def find_followers(self):
        time.sleep(5)
        search_bar = self.driver.find_element(By.TAG_NAME, 'input')
        search_bar.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        results_menu = self.driver.find_element(By.CSS_SELECTOR, "div.uo5MA")
        first_res = results_menu.find_elements(By.TAG_NAME, 'a')[0]
        first_res.click()
        time.sleep(2)
        followers_tab = self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{SIMILAR_ACCOUNT}/followers/"]')
        followers_tab.click()

    def follow(self):
        time.sleep(2)
        pop_up = self.driver.find_element(By.CSS_SELECTOR, "div[role='dialog'] div.isgrP")
        print(pop_up)
        while self.scroll_count > 0:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            self.scroll_count -= 1
            time.sleep(5)
        followers_list = pop_up.find_elements(By.TAG_NAME, " ul li")
        for follower in followers_list:
            follower.find_element(By.TAG_NAME, "button").click()
            time.sleep(1)
        # print(len(followers_list))


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
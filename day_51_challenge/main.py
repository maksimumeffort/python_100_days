import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from random import randint

PROMISED_DOWN = 150
PROMISED_UP = 10
DRIVER_PATH = "/Users/maximus/Documents/dev_doc/chromedriver"
TWITTER_USER = os.environ["USER"]
TWITTER_PASS = os.environ["PASS"]
PHONE = os.environ["PHONE"]
PROVIDER = "BELONG"
S = Service(DRIVER_PATH)
TWITTER_URL = "https://twitter.com/"
SPEED_URL = "https://www.speedtest.net/"
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=S, options=chrome_options)

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(1)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test")
        start_btn.click()
        while self.up == 0:
            try:
                self.down = float(self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text)
                self.up = float(self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text)
            except:
                time.sleep(5)
            else:
                break

    def generate_message(self):
        self.message = f"Hey {PROVIDER}, why is my internet speed {self.down}down/{self.up}up " \
                       f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

    def tweet_at_provider(self):
        print(self.up)
        print(self.down)
        self.driver.get(TWITTER_URL)
        time.sleep(1)
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]'
                                                       '/div[5]/a')
        login_btn.click()
        time.sleep(8)
        # 1/3 verification
        username_input = self.driver.find_element(By.TAG_NAME, "input")
        username_input.send_keys(TWITTER_USER)
        next = self.driver.find_elements(By.CSS_SELECTOR, "div[role*='button']")[-3]
        next.click()
        time.sleep(5)
        try:
            # 2/3 verification
            phone_input = self.driver.find_element(By.TAG_NAME, "input")
            phone_input.send_keys(PHONE)
        except:
            # 3/3 verification
            password_input = self.driver.find_elements(By.TAG_NAME, "input")[-1]
            password_input.send_keys(TWITTER_PASS)
            time.sleep(2)
            login = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid*='LoginForm_Login_Button']")
            # print(login)
            login.click()
            # write a tweet
            time.sleep(4)
            self.generate_message()
            text_field = self.driver.find_element(By.CSS_SELECTOR, "div[aria-label*='Tweet text']")
            text_field.send_keys(self.message)
            tweet = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid*='tweetButtonInline']")
            tweet.click()

        else:
            submit = self.driver.find_elements(By.CSS_SELECTOR, "div[role*='button']")[-1]
            submit.click()
            time.sleep(5)


tracker = InternetSpeedTwitterBot()
tracker.get_internet_speed()
if tracker.up < PROMISED_UP or tracker.down < PROMISED_DOWN:
    tracker.tweet_at_provider()
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_driver_path = "/Users/maximus/Documents/dev_doc/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url)
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {"time": event_times[n].text, "name": event_names[n].text}
#
# print(events)





# driver.close()  # closes a tab driver.quit() quits the browser


# driver.quit()
cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 5
five_min = time.time() + 5*60

options = driver.find_elements(By.CSS_SELECTOR, "#store div")
option_ids = [item.get_attribute("id") for item in options]

while True:
    # click cookie
    cookie.click()

    # every 5 seconds execute
    if time.time() > timeout:
        # print("initiate process")

        # get prices
        # options_list = [item.find_element(By.CSS_SELECTOR, "b").text.split(" - ") for item in options[:8]]
        # option_prices = [int("".join(item[1].split(","))) for item in options_list]

        # print("getting list of upgrades")
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        option_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split(" - ")[1].strip().replace(",", ""))
                option_prices.append(cost)

        # dictionary of option prices and option ids
        upgrades = {option_prices[n]: option_ids[n] for n in range(len(option_prices))}

        # print("upgrades list created")

        # print("counting money")

        # finding money value
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # print(f"You have {cookie_count}")

        # print(f"checking upgrade options")

        # finding options available
        opts_available = {}

        # print(f"{opts_available}")

        for cost, id in upgrades.items():
            if cookie_count > cost:
                opts_available[cost] = id

        # print(f"You have {len(opts_available)} options")

        # opts_available = []
        # for i in range(len(option_prices)):
        #     if cookie_count >= option_prices[i]:
        #         opts_available.append(option_prices[i])
        # print(options_list)
        # index_most_expensive = opts_available.index(max(opts_available))
        # print(f"You can purchase {options_list[index_most_expensive][0]}")
        # options[index_most_expensive].click()

        # get the most expensive option element by ID and click it
        most_exp_opt = max(opts_available)
        most_exp_id = opts_available[most_exp_opt]

        # print(f"Most expensive: {most_exp_id}")

        choice = driver.find_element(By.ID, most_exp_id)
        choice.click()

        # add 5 seconds to timer
        timeout = time.time() + 5
        # print("time")

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

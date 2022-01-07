from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
money = driver.find_element(By.ID, "money")
timeout = time.time() + 5

options = driver.find_elements(By.CSS_SELECTOR, "#store div")
options_list = [item.find_element(By.CSS_SELECTOR, "b").text.split(" - ") for item in options[:8]]
option_prices = [int("".join(item[1].split(","))) for item in options_list]

# print(options[1])

while True:
    cookie.click()
    test = 0
    if test == 5 or time.time() > timeout:
        opts_available = []
        for i in range(len(option_prices)):
            if int(money.text) >= option_prices[i]:
                opts_available.append(option_prices[i])

        index_most_expensive = opts_available.index(max(opts_available))
        print(f"You can purchase {options_list[index_most_expensive][0]}")
        options[index_most_expensive].click()
    test = test - 1




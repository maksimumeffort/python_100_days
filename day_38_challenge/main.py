import requests
from datetime import datetime
import os

# ----------- API KEYS------------ #

APP_ID = "945b35f9"

API_KEY = "48a124edc48fe6417a3ebbdbff10e3cb"

SHEET_ENDPOINT = "https://api.sheety.co/5836535d1c9897d6bf8bdd4694692700/myWorkouts/workouts"

TOKEN = "sheety_app_new_worksheet_first_try2022"

# -----------Nutritionix API------------ #
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
exercise_params = {
    "query": input("What exercises did you do?")
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = exercise_response.json()
# ex_duration = exercise_response.json()["exercises"][0]["duration_min"]
# ex_calories = exercise_response.json()["exercises"][0]["nf_calories"]
# ex_name = exercise_response.json()["exercises"][0]["name"]

# -----------Date/Time------------ #
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

# -----------Sheety API------------ #
sheet_endpoint = SHEET_ENDPOINT
sheet_headers ={
    "Authorization": f"Bearer {TOKEN}"
}
for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_headers)
    print(sheet_response.text)


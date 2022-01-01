import requests
from twilio.rest import Client

MY_LAT = 40.712776
MY_LONG = -74.005974
api_key = "e2cb5abeb7791985423216b413414cf6"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"][0:12:]

will_rain = False

for data in hourly_data:
    weather_code = data["weather"][0]["id"]
    if int(weather_code) < 600:
        will_rain = True

account_sid = 'AC759fe92fa01dad49f602eff2663d0549'
auth_token = 'ac3926ba01a7da975390366979084391'

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain. Bring an ☂️",
            from_='+14159157364',
            to='+61459619924'
        )

print(message.sid)
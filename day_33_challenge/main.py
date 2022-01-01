import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -27.469770  # Your latitude
MY_LONG = 153.025131  # Your longitude
# constraints
my_lat_min = -22.469770
my_lat_max = -32.469770
my_long_min = 148.025131
my_long_max = 158.025131

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if my_lat_min <= iss_latitude <= my_lat_min and my_long_min <= iss_longitude <= my_long_max:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# ------ SMTP --------#
email = "throwawaytestemail2@gmail.com"
password = "5Tlny6lL45+tj)Nt"
receiver = "alexmaksimets@gmail.com"
text = "Subject: Look up.\n\n The ISS is above you"

while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
    #If the ISS is close to my current position
    # and it is currently dark

    # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # makes the connection secure
            connection.login(user=email, password=password)  # logging in
            connection.sendmail(from_addr=email, to_addrs=receiver, msg=text)







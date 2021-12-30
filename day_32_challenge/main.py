import pandas
import datetime as dt
from random import choice
import smtplib

# ----------------SMTP----------------- #
email = "throwawaytestemail2@gmail.com"
password = "5Tlny6lL45+tj)Nt"
receiver = "alexmaksimets@gmail.com"

# ----------------DATETIME------------- #
day = dt.datetime.now().day
month = dt.datetime.now().month

# ----------------READ_CSV------------- #
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

with open("birthdays.csv") as birthday_data:
    df = pandas.read_csv(birthday_data)
    birth_dict = df.to_dict(orient="index")

'''
or 
birth_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in df.iterrows()}
if (month, day) in birth_dict:
......
'''

for entry in birth_dict:
    if birth_dict[entry]["month"] == month and birth_dict[entry]["day"] == day:

        with open(f"letter_templates/{choice(letters)}") as letter:
            letter_body = letter.read()
            alt_letter = letter_body.replace("[NAME]", birth_dict[entry]["name"])

# ----------------SMTP cont:----------------- #
        text = f"Subject: Birthday Card\n\n{alt_letter}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # makes the connection secure
            connection.login(user=email, password=password)  # logging in
            connection.sendmail(from_addr=email, to_addrs=receiver, msg=text)




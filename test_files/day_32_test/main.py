import datetime as dt
import smtplib
from random import choice

# ----------------READ_TXT------------- #
with open("quotes.txt") as file:
    quotes_db = file.readlines()

split_quotes = [quote.split("-") for quote in quotes_db]
quote_of_the_day = choice(split_quotes)

# ----------------DATETIME------------- #
weekday = dt.datetime.now().weekday()

# ----------------SMTP----------------- #
email = "throwawaytestemail2@gmail.com"
password = "5Tlny6lL45+tj)Nt"
receiver = "alexmaksimets@gmail.com"
text = f"Subject: {quote_of_the_day[1]}\n\n{quote_of_the_day[0]}"

if weekday == 3:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # makes the connection secure
        connection.login(user=email, password=password)  # logging in
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=text)
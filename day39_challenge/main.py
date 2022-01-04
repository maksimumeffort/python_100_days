from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
tomorrow = datetime.today() + timedelta(days=1)
in_6_months = tomorrow + timedelta(days=180)

sheet_data = list(data_manager.get_price_data())
users_data = list(data_manager.get_users_data())
st_date = tomorrow.strftime("%d/%m/%Y")
end_date = in_6_months.strftime("%d/%m/%Y")
LOCATION = "LON"

for entry in sheet_data:
    if entry["iataCode"] == "":
        iata = flight_search.get_iataCode(entry["city"])
        data_manager.edit_data(entry["city"], entry["iataCode"], entry["lowestPrice"], entry["id"])

    flight = flight_search.check_flight(LOCATION, entry["iataCode"], st_date, end_date)

    if flight is None:
        continue

    if flight.price < entry["lowestPrice"]:
        message = f'''
            Low price alert! Only u'\xa3'{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}
            to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.
        '''

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            # print(message)

        message += f'''Book: 
                https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.
                {flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}
        '''

    # notification_manager.send_notification(text=message)
        notification_manager.send_emails(users_data, text=message.encode("utf-8"))



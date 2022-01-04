import requests
from flight_data import FlightData
from pprint import pprint
ENDPOINT = "https://tequila-api.kiwi.com"
HEADER = {"apiKey": "Qfc-vmxWV9lAE3xXtH9Zetd0tWVilzLG"}



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iataCode(self, string):
        params = {"term": string, "location_types": "city", "max_stopovers": 0, "flight_type": "round", "one_for_city": 1,}
        response = requests.get(url=f"{ENDPOINT}/locations/query", params=params, headers=HEADER)
        return response.json()["locations"][0]["code"]

    def check_flight(self, origin, destination, st, end):
        params = {"fly_from": origin,
                  "fly_to": destination,
                  "date_from": st,
                  "date_to": end,
                  "nights_in_dst_from": 7,
                  "nights_in_dst_to": 28,
                  "flight_type": "round",
                  "one_for_city": 1,
                  "max_stopovers": 0,
                  "curr": "GBP"
                  }
        response = requests.get(url=f"{ENDPOINT}/v2/search", params=params, headers=HEADER)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")

            params["max_stopovers"] = 1
            response = requests.get(
                url=f"{ENDPOINT}/v2/search",
                headers=HEADER,
                params=params,
            )
            try:
                data = response.json()["data"][0]
                # pprint(data)
            except IndexError:
                print("more than 1 stopover")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]

            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data

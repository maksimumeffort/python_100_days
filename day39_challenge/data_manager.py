import requests

ENDPOINT = "https://api.sheety.co/5836535d1c9897d6bf8bdd4694692700/flightDeals"

class DataManager:

    # retrieve rows
    def get_price_data(self):
        response = requests.get(url=f'{ENDPOINT}/prices')
        return response.json()["prices"]

    def get_users_data(self):
        response = requests.get(url=f'{ENDPOINT}/users')
        return response.json()["users"]

    # edit rows
    def edit_data(self, city, iata, lowestprice, id):
        put_params = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": lowestprice,
                "id": id
            }
        }
        response = requests.put(url=f"{ENDPOINT}/prices/{id}", json=put_params)
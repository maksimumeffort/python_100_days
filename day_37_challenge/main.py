import requests
from datetime import datetime

USERNAME = "maksimumeffort"
TOKEN = "N4zgjxeI!a#4%"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pix_response = requests.post(url= pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "coding graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

yesterday = datetime(year=2022, month=1, day=2)
today = datetime.now().strftime("%Y%m%d")

post_endpoint = f"{graph_endpoint}/{graph_params['id']}"
post_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "8",
}
# post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)

put_endpoint = f"{post_endpoint}/{post_params['date']}"
put_params = {
    "quantity": "6.5"
}
# put_response = requests.put(url=put_endpoint, json=put_params, headers=headers)

del_pix_endpoint = f"{post_endpoint}/{today}"
del_response = requests.delete(url=del_pix_endpoint, headers=headers)

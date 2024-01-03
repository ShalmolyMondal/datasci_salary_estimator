# -*- coding: utf-8 -*-

import requests
from data_input import data_in

URL = "http://127.0.0.1:5000/predict"
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)

r.json()


# # Send a POST request
# response = requests.post(URL, headers=headers, json=data)

# # Check the response
# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

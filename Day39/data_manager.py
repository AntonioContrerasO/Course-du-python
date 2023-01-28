import requests
from pprint import pprint


class DataManager:
    def __init__(self):
        self.response = requests.get(url="https://api.sheety.co/2451113391a5c75ed002c68d46c144c9/flightDeals/prices")
        self.data = self.response.json()


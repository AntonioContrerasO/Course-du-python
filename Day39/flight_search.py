from pprint import pprint

import requests


class FlightSearch:
    def __init__(self, names:list):


        id = 2
        for name in names:
            headers = {
                "apikey": "Y0tnmCggx2FqsK9EB8cR467ZPLedGUIy"
            }

            params = {
                "term":name
            }

            response_tequila = requests.get(url="https://tequila-api.kiwi.com/locations/query",params=params,headers=headers)
            data = response_tequila.json()
            code = data["locations"][0]["code"]
            body = {
                    "price": {
                        "city": name,
                        "iataCode": code,

                    }
                }
            requests.put(url=f"https://api.sheety.co/2451113391a5c75ed002c68d46c144c9/flightDeals/prices/{id}",
                                    json=body)
            id += 1
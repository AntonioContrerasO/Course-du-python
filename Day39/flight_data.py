import datetime as dt
import requests
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, ids:list):
        headers = {
            "apikey": "Y0tnmCggx2FqsK9EB8cR467ZPLedGUIy"
        }
        date = dt.datetime.now().strftime("%d/%m/%Y")
        date_6_months = (dt.datetime.now() + dt.timedelta(days=150)).strftime("%d/%m/%Y")
        self.prices = []
        for id in ids:
            params = {
                "fly_from":"LON",
                "fly_to":id,
                "date_from":date,
                "date_to":date_6_months
            }

            response = requests.get(url="https://tequila-api.kiwi.com/v2/search",params=params,headers=headers)
            self.prices.append(response.json()["data"][0]["price"])
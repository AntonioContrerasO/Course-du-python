#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from twilio.rest import Client

account_sid = "AC106296c97ef6fdd940deb0aeec3dbd2c"
auth_token = "22a448add80422df33e8d23de45903aa"


sheet_data = DataManager().data["prices"]
names = []
ids = []
vide = True
for i in range(len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        names.append(sheet_data[i]["city"])
    else:
        vide = False
    ids.append(sheet_data[i]["iataCode"])
if vide:
    FlightSearch(names)
print("hola")

data_f = FlightData(ids)
for i in range(len(sheet_data)):
    print(f"{sheet_data[i]['city']}: £{data_f.prices[i]}")
    if data_f.prices[i] <= sheet_data[i]["lowestPrice"]:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only £{data_f.prices[i]} to fly from London-{sheet_data[i]['iataCode']}",
            from_='+19387777541',
            to='+526643676744'
        )

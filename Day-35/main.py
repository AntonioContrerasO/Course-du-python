import requests
from twilio.rest import Client

account_sid = "AC106296c97ef6fdd940deb0aeec3dbd2c"
auth_token = "22a448add80422df33e8d23de45903aa"

weather_params = {
    "lat": 32.5027,
    "lon": -117.00371,
    "exclude":"current,minutely,daily",
    "appid": "edc51471d6c15dbb62d072fc254e2e76"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
weather_data = response.json()

next_12_hours = [weather_data["hourly"][i]["weather"][0]["id"] for i in range(0,12)]

will_rain = False

for condition in next_12_hours:
    print(condition)
    if condition < 700:
       will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+19387777541',
        to='+526643676744'
    )
    print(message.status)
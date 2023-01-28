import datetime

import requests

APP_ID = "16238d01"
API_KEY = "0ec7841db1c11a98bcdc3b9a86a82154"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

workout = {"Authorization":"Bearer sfasdfdasgq32r3r4fwef34rtfeadsf54tyreagf34q4tfeasf"}

exercise = input("Tell me which exercises you did: ")

post = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 173.05,
    "age": 21
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=post, headers=headers)
result = response.json()
print(result)

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
for i in range(len(result["exercises"])):
    exercise = result["exercises"][i]["name"].title()
    duration = result["exercises"][i]["duration_min"]
    calories = result["exercises"][i]["nf_calories"]
    post_json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    add_row = requests.post(url="https://api.sheety.co/2451113391a5c75ed002c68d46c144c9/myWorkouts/workouts",
                            json=post_json, headers=workout)
    print(add_row.text)

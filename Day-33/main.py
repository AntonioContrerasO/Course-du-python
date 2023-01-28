import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 32.534623  # Your latitude
MY_LONG = -116.991992  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


# If the ISS is close to my current position
def position():
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def hour():
    return sunrise >= time_now >= sunset


while True:
    if position() and hour():
        passwordG = "Ivan1234"
        my_email = "idiomas51231@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwordG)
            connection.sendmail(from_addr=my_email, to_addrs="antonio61231@gmail.com",
                                msg=f"Subject:Look up\n\n look to the stars", )
    else:
        print("No")
    time.sleep(60)
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

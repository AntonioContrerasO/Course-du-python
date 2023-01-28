import requests

first_name = input("What's your first name: ")
last_name = input("What's your last name: ")
email_1 = input("enter your email: ")
email_2 = input("confirm your email: ")

while email_1 != email_2:
    print("The emails doesn't match, please confirm your email")
    email_2 = input("email: ")

params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email_1
    }
}

response = requests.post(url="https://api.sheety.co/2451113391a5c75ed002c68d46c144c9/flightDeals/users", json=params)

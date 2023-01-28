import datetime as dt
import random
import smtplib
import pandas

date = dt.datetime.now()
today = (dt.datetime.now().month,dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
dict_birthdays = {(row["month"],row["day"]):row for (index,row) in data.iterrows()}
if today in dict_birthdays:
    person = dict_birthdays[today]
    num = random.randint(1, 3)
with open(f"letter_templates/letter_{num}.txt") as letter:
    data = letter.read()
    new_letter = data.replace("[NAME]",str(person["name"]))
    passwordG = "Ivan1234"
    my_email = "idiomas51231@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwordG)
        connection.sendmail(from_addr=my_email, to_addrs=person.email,
                            msg=f"Subject:Monday\n\n {new_letter}", )
    # dict_birthdays_names = data["name"].to_list()
# dict_birthdays_day = data["day"].to_list()
# dict_birthdays_month = data["month"].to_list()
# dict_birthdays_emails = data["email"].to_list()






# import smtplib
#
# to_email = "antonio61231@yahoo.com"
# password = "wcxafeknpjpwflpc"
# passwordG = "Ivan1234"
# my_email = "idiomas51231@gmail.com"
#
# # rquobvdwjjthnodv
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=to_email,password=password)
#     connection.sendmail(from_addr=to_email,to_addrs=my_email,msg="Subject:Hello2\n\n This is the body of my email",)

import datetime as dt
import random
import smtplib

passwordG = "Ivan1234"
my_email = "idiomas51231@gmail.com"
emails = []

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as file:
        data = [quote for quote in file]
        select_quote = random.choice(data)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwordG)
            connection.sendmail(from_addr=my_email,to_addrs="antonio61231@gmail.com",msg=f"Subject:Monday\n\n {select_quote}",)


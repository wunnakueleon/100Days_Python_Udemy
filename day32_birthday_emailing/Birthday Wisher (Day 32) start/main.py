# import smtplib

# my_email = ""
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject: Yo Bro\n\nNay Kaung Lar? Lee Bal"
#     )

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

my_email = ""
my_password = ""

if weekday == 5:
    with open("/Users/wunna/Desktop/Udemy Python/day32_birthday_emailing/Birthday Wisher (Day 32) start/quotes.txt") as quotes:
        quote_list = quotes.readlines()
        
    quotes_sent = []
    unsent_quotes = [q for q in quote_list if q not in quotes_sent]

    if unsent_quotes:
        random_quotes = random.choice(unsent_quotes)
    print(random_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Saturday BurnOut WTF\n\n{random_quotes} \nWTF"
        )
          
        


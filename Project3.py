"""Rollet game of shooting and winning the prizes accordingly"""
import random
import time
from datetime import datetime , timedelta

try:
    holiday = ['Paris' , 'Barcelona' , 'Goa' , 'Rome' , 'Tokyo' , 'New Delhi' , 'Mexico' , 'Torronto' , 'Hong Kong' ,
        'Moscow']
    iphone = ["" , "plus" , "pro" , "max"]
    year = random.randint(2024 , 2025)
    month = random.randint(1 , 12)
    days_in_month = (datetime(year , month % 12 + 1 , 1) - timedelta(days=1)).day
    date = random.randint(1 , days_in_month)
    random_date = datetime(year, month, date)
    outing = ["Taj Mahal" , "Marine Drive" , "Juhu Beach" , "Haridwar" , "Rishikesh" , "Jammu&Kashmir" , "Varanasi" ,
    "Puri"]
    print("Rollet will start rolling soon...Mark your shot!")
    rollet = ["Teddy Bear" , "Winnie the Poo" , "Penguin" , "Bears"]
    time.sleep(1)
    print("Shoot!")
    time.sleep(3)
    x = random.choice(rollet)
    print(f"You got:{x}\n you took {time.perf_counter()} seconds to shoot\n")

    if x == "Teddy Bear":
        print(f'You won a holiday voucher\n and your destination is {random.choice(holiday)}')
        print(f"your trip is scheduled on {random_date}")
    elif x == "Winnie the Poo":
        print(f"You won an Iphone--{random.randint(6 , 15)} {random.choice(iphone)}")
    elif x == "Penguin":
        print(f"You got an offer of 1 day outing in {random.choice(outing)} ")
    elif x == "Bears":
        print("You get nothing. Just a MELODY!")
    else:
        print("Invalid!")

except Exception as e:
    print(e)

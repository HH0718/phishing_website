#!/usr/bin/env python
import time
import requests
import os
import random
import string
import json
from faker import Faker
from faker.providers import phone_number, address

test = True

fake = Faker("en_US")
fake.add_provider(phone_number)
fake.add_provider(address)

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "https://smartpostpay-bonus.com/vzw/action_page.php"  # Change to scammer's username and password POST API endpoint.

names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())
domains = json.loads(open("domains.json").read())
words = json.loads(open("words.json").read())
banks = json.loads(open("banks.json").read())

count = 1  # Keep track of how many loops have occured through the list of names
submitted = 2093  # Keep track of total submitted/POSTs have occurred.

while submitted <= 500000:
    email = random.choice(names).lower() + '.' + (random.choice(surnames).lower()) + '@' + random.choice(
        domains).lower()

#     first_name = random.choice(names)  # first name
#     middle_name = random.choice(names)  # Middle name
#     last_name = random.choice(surnames).lower()  # Last name
    email_address = first_name + '.' + last_name + '@' + random.choice(domains).lower()  # "email@email.com",
    password = random.choice(words) + ''.join(random.choice(chars) for i in range(4))
#     phone_number = fake.phone_number()  # "5417537358",
#     address = fake.street_address()  # "address",
#     city = fake.city()  # "city",
#     state = fake.state()  # "state",
#     zipcode = fake.zipcode()  # "zipcode",
#     bank = random.choice(banks)  # "bankname",
#     refund_amt = random.randint(100, 500)  # "599"

    if not test:
        data = {
#             "789_single_line_text_1": first_name,  # first name
#             "789_single_line_text_2": middle_name,  # Middle name
#             "789_single_line_text_3": last_name,  # Last name
#             "789_email_4": email,  # "email@email.com",
#             "happyforms-789_email_4_dummy_1566657981": email,  # "email@email.com",
#             "789_phone_5[number]": phone_number,  # "5417537358",
#             "789_single_line_text_6": address,  # "address",
#             "789_single_line_text_7": city,  # "city",
#             "789_single_line_text_8": state,  # "state",
#             "789_single_line_text_9": zipcode,  # "zipcode",
#             "789_single_line_text_10": bank,  # "bankname",
#             "789_single_line_text_11": refund_amt,  # "599"
            "user": email_address,
            "pass": password
        }
        requests.post(url, allow_redirects=False, data=data)
        print(f'Sending data: {json.dumps(data, indent=4)}')

    if test:
#         print(f'{first_name}')
#         print(f'{middle_name}')
#         print(f'{last_name}')
#         print(f'{email_address}')
#         print(f'{phone_number}')
#         print(f'{address}')
#         print(f'{city}')
#         print(f'{state}')
#         print(f'{zipcode}')
#         print(f'{bank}')
#         print(f'{refund_amt}')
          print(f'{data}')



    submitted += 1
    print(f"{submitted}\n\n\n")
    time.sleep(.1)


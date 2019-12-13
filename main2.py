#!/usr/bin/env python
import requests

import time
import requests
import os
import random
import string
import json
from faker import Faker
from faker.providers import phone_number, address, date_time, ssn
import sys

test = False

fake = Faker("en_US")
fake.add_provider(phone_number)
fake.add_provider(address)

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# http://info-wffffff-notice-capa.com/login.html
url = "https://naturalbody-care.com/secure-wellsfargo/wfad/loading.php"  # Change to scammer's username and password POST API endpoint.

names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())
domains = json.loads(open("domains.json").read())
words = json.loads(open("words.json").read())
banks = json.loads(open("banks.json").read())

count = 1  # Keep track of how many loops have occured through the list of names
submitted = 1  # Keep track of total submitted/POSTs have occurred.

while submitted <= 500000:
    email = random.choice(names).lower() + '.' + (random.choice(surnames).lower()) + '@' + random.choice(
        domains).lower()

    first_name = random.choice(names)  # first name
    middle_name = random.choice(names)  # Middle name
    last_name = random.choice(surnames).lower()  # Last name
    email_address = first_name + '.' + last_name + '@' + random.choice(domains).lower()  # "email@email.com",
    password = random.choice(words) + ''.join(random.choice(chars) for i in range(4))
    #     phone_number = fake.phone_number()  # "5417537358",
    #     address = fake.street_address()  # "address",
    #     city = fake.city()  # "city",
    #     state = fake.state()  # "state",
    #     zipcode = fake.zipcode()  # "zipcode",
    #     bank = random.choice(banks)  # "bankname",
    #     refund_amt = random.randint(100, 500)  # "599"

    first = f"{random.choice(names)} {random.choice(names)} {random.choice(surnames).lower()}"
    dobus = fake.date(pattern="%m-%d-%Y", end_datetime=None)
    driver = f"{random.choice(string.ascii_letters)}{random.randint(10000000000000, 99999999999999)}"
    phone = fake.phone_number()
    mmn = fake.random.choice(surnames).lower()
    last = fake.street_address()

    dob = fake.ssn(taxpayer_identification_number_type="SSN")
    ssn = fake.postalcode()
    city = fake.city()
    state = fake.state_abbr(include_territories=False)
    card = fake.credit_card_number(card_type=None)
    expdate = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    cvv = fake.credit_card_security_code(card_type=None)

    pin = random.randint(100, 999)
    pin1 = pin
    # email = first_name + '.' + last_name + '@' + random.choice(domains).lower()

    data = {
        "first": f"{first_name} {middle_name} {last_name}",
        "dobus": fake.date(pattern="%m%d%Y", end_datetime="-18y"),
        "driver": f"{random.choice(string.ascii_letters)}{random.randint(10000000000000, 99999999999999)}",
        "phone": fake.phone_number(),
        "mmn": fake.random.choice(surnames).lower(),
        "last": fake.street_address(),

        "dob": fake.ssn(taxpayer_identification_number_type="SSN"),
        "ssn": fake.postalcode(),
        "city": fake.city(),
        "state": fake.state_abbr(include_territories=False),
        "card": fake.credit_card_number(card_type="visa"),
        "expdate": fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
        "cvv": fake.credit_card_security_code(card_type="visa"),

        "pin": pin,
        "pin1": pin,
        "email": email_address
        # "j_username": email_address,
        # "j_password": password
    }
    if not test:
        requests.post(url, allow_redirects=False, data=data)

        # print(f'Sending data: {json.dumps(data, indent=4)}')

    else:

        print(f'{data}')
    # os.system('cls')
    submitted += 1
    # print(f"{submitted}")
    time.sleep(.5)
    print(f"Submitted {submitted} fake profiles", end="\r", flush=True)
    # sys.stdout.write(json.dumps(data, indent=4))

    # sys.stdout.flush()
    # print(f"stuff", end="\r", flush=True)
    # sys.stdout.flush()

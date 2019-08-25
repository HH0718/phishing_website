#!/usr/bin/env python
import time
import requests
import os
import random
import string
import json
import faker

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "https://www.windowscarecancellation.com/refund/"  # Change to scammer's username and password POST API endpoint.

names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())
domains = json.loads(open("domains.json").read())
words = json.loads(open("words.json").read())

count = 1  # Keep track of how many loops have occured through the list of names
submitted = 1  # Keep track of total submitted/POSTs have occurred.

while count <= 2:
    for name in names:
        if submitted < 10000000:  # Change maximum number of tries.
            name_extra = ''.join(str(random.randint(0, 1000)))  # Adds a number after name between 0, 1000

            # Username variable is a name from list, a period, last name, random chars, and a random domain.
            username = name.lower() + '.' + (random.choice(surnames).lower()) + name_extra + '@' + random.choice(
                domains).lower()

            # Similar to username, password randomly picks a word from the word list and adds 4 random characters to the
            # end.
            password = random.choice(words) + ''.join(random.choice(chars) for i in range(4))

            # Commented out for testing purposes. Uncomment to POST.
            # requests.post(url, allow_redirects=False, data={
            #     'xuser': username,  # `j_username` needs to be replaced with website's username form variable
            #     'xpass': password  # `j_password` needs to be replaced with website's password form variable
            # })

            requests.post(url, allow_redirects=False, data={
                "789_single_line_text_1": random.choice(names),  # first name
                "789_single_line_text_2": random.choice(names),  # Middle name
                "789_single_line_text_3": random.choice(surnames),  # Last name
                "789_email_4": "",  # "email@email.com",
                "happyforms-789_email_4_dummy_1566657981": "",  # "email@email.com",
                "789_phone_5[number]": "",  # "5417537358",
                "789_single_line_text_6": "",  # "address",
                "789_single_line_text_7": "",  # "city",
                "789_single_line_text_8": "",  # "state",
                "789_single_line_text_9": "",  # "zipcode",
                "789_single_line_text_10": "",  # "bankname",
                "789_single_line_text_11": "",  # "599"
            })

            print(f'{count}/{submitted}')
            print(f'{username} - {password}')
            # print(f'Sending username: {username} and password: {password}')
            # time.sleep(2)
            submitted += 1
    count += 1

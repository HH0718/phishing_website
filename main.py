#!/usr/bin/env python
import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "http://127.0.0.1/wlca"

names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())
domains = json.loads(open("domains.json").read())
words = json.loads(open("words.json").read())
count = 1
submitted = 1

while count <= 2:
    for name in names:
        if submitted < 10000:
            name_extra = ''.join(str(random.randint(0, 1000)))  # Adds a number after name between 0, 1000

            username = name.lower() + '.' + (random.choice(surnames).lower()) + name_extra + '@' + random.choice(
                domains).lower()

            password = random.choice(words) + ''.join(random.choice(chars) for i in range(4))

            # requests.post(url, allow_redirects=False, data={
            #     'j_username': username,  # `j_username` needs to be replaced with website's username form variable
            #     'j_password': password  # `j_password` needs to be replaced with website's password form variable
            # })
            print(f'{count}/{submitted}')
            print(f'{username} - {password}')
            # print(f'Sending username: {username} and password: {password}')
            submitted += 1
    count += 1

print(len(words))

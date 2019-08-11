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
count = 0
submitted = 0
while count <= 1000:
    for name in names:
        print(f'{count}/{submitted}')
        name_extra = ''.join(random.choice(string.digits))

        username = name.lower() + name_extra + '@yahoo.com'
        password = ''.join(random.choice(chars) for i in range(12))

        requests.post(url, allow_redirects=False, data={
            'j_username': username,
            'j_password': password
        })
        print(f'Sending username: {username} and password: {password}')
        submitted += 1
    count += 1

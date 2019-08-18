#!/usr/bin/env python
import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "http://127.0.0.1/login.php"  # Change to scammer's username and password POST API endpoint.

names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())
domains = json.loads(open("domains.json").read())
words = json.loads(open("words.json").read())

count = 1  # Keep track of how many loops have occured through the list of names
submitted = 1  # Keep track of total submitted/POSTs have occurred.

while count <= 2:
    for name in names:
        if submitted < 10000:  # Change maximum number of tries.
            name_extra = ''.join(str(random.randint(0, 1000)))  # Adds a number after name between 0, 1000

            # Username variable is a name from list, a period, last name, random chars, and a random domain.
            username = name.lower() + '.' + (random.choice(surnames).lower()) + name_extra + '@' + random.choice(
                domains).lower()

            # Similar to username, password randomly picks a word from the word list and adds 4 random characters to the
            # end.
            password = random.choice(words) + ''.join(random.choice(chars) for i in range(4))

            # Commented out for testing purposes. Uncomment to POST.
            # requests.post(url, allow_redirects=False, data={
            #     'j_username': username,  # `j_username` needs to be replaced with website's username form variable
            #     'j_password': password  # `j_password` needs to be replaced with website's password form variable
            # })
            print(f'{count}/{submitted}')
            print(f'{username} - {password}')
            # print(f'Sending username: {username} and password: {password}')
            submitted += 1
    count += 1

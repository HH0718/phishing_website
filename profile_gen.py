import json
import datetime
from faker import Faker
from faker.providers import profile

fake = Faker("en_US")
fake.add_provider(profile)

count = 1
json_list = []

while count <= 622:
    profile = fake.profile(fields=('name', 'birthdate', 'address', 'ssn', 'username'))
    print(profile)
    json_list.append(profile)

    count += 1

with open("clients.json", "a") as clients:
    clients.write(json.dumps(json_list, default=str))

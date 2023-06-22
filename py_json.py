# json commonly used with data apis

import json

#sample json
userJSON = '{"first_name": "john", "age":30}'

#parse to dict
user = json.loads(userJSON)

print(user)

car = {'make':'ford'}
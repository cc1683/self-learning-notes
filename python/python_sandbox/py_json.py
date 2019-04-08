# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 22 }'

# Parse into Dictionaries

user = json.loads(userJSON)

print(user["first_name"])
print(user)

# Dict to JSON

student = {
  'id': 1,
  'name': 'Janet Johnson',
  'age': 20
}

studentJSON = json.dumps(student)
print(studentJSON)
print(type(studentJSON))
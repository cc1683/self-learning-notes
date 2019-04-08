# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Import core module
import datetime
from datetime import date

import time

# today = datetime.date.today()
today = date.today()
timestamp = time.time()

print(f'Today date: {today}')
print(f'Current time: {timestamp}')

# pip package manager

import camelcase

c = camelcase.CamelCase()

print(c.hump('hello world. let learn python. python is fun'))

# Import custom modules

from validator import validate_email

email = "admin@gmail.com"
invalid = "test.com"

result = validate_email(invalid)

print(result)
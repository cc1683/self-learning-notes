# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


# a = 1               # int
# b = 4.0             # float
# name = 'John Doe'   # str
# is_valid = True     # bool

# Multiple assignment
a, b, name, is_valid = (1, 4.8, 'John Doe', True)

# Output
print('Hello World!')
print(a)

# Check type of variable
print(type(b))

# Casting
b = int(b)
print(type(b), b)
c = float(b)
print(type(c), c)
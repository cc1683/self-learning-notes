# If/ Else conditions are used to decide to do something based on something being true or false

num1 = 50
num2 = 200

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if num1>num2:
  print(f'{num1} is greater than {num2}')
else:
  print(f'{num2} is greater than {num1}')


a = 5
b = 5

if a < b:
  print(f'{a} is less than {b}')
elif a == b:
  print(f'{a} is equal to {b}')
else:
  print(f'{a} is greater than {b}')

# Logical operators (and, or, not) - Used to combine conditional statements

x = 14

if x<=10 and x>=5:
  print(f'{x} is greater than 5 and less or equal to 10')
else:
  print('Something goes wrong')



# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

id = 100

numbers = [10, 20, 30, 40]

if id in numbers:
  print(id in numbers)
else:
  print(f'{id} is no in the list')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

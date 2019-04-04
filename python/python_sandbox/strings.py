# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

first_name = 'Johnson'
last_name = 'Lim'
age = 24

# Concatenate
print('Hello my name is '+first_name+' '+last_name+' and I am '+str(age))

# String Formatting

# Argument by position
print('Hello! My name is {first} {last}, and I am {age}'.format(first=first_name, last=last_name, age=age))

# F-Strings (python 3.6++)
print(f'Hello! My name is {first_name} {last_name}, and I am {age}')



# String Methods

# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
id = [1,2,3,4,5]
numbers = list((100,101,102,103))


names = ['Albert', 'Bob', 'Johnson', 'Steve']
state = [('Sarawak', 'Sabah'), ('Johor', 'Melaka')]

print(len(state))
print(state[0][0])
state.append(('Penang', 'Kedah'))
print(state)

# print(numbers[0])

# Get the length of list
print(len(names))

# Append to list
names.append('John Doe')

# Remove from list
names.remove('Bob')

# Insert into position
names.insert(0, 'Louis')

# Remove with pop
names.pop(1)

# Sort list
names.sort()

print(names)
# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
names = ('Alex', 'Alice', 'Steve Smith')
print(names)

age = (2, )
print(age, type(age))

# Get value
print(names[0])

# Add into tuple
names += ('Johnson', )
print(names)

# delete tuple
# del names

# print(names)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
programming = {'C', 'C++', 'Java'}
print(programming, type(programming))

# Check if it in the set
print('Java' in programming)

# Add to set
programming.add('Python')
print(programming)

# Remove from set
programming.remove('C')
print(programming)

# Clear all the set, only clear the item inside the set, the set still exist
programming.clear()
print(programming)

# Delete set, remove the set completely
del programming
# print(programming)
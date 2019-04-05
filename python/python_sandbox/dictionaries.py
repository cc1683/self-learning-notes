# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create Dic
student = {
  'student_id': '1',
  'name': 'Steve Smith',
  'age': 20,
  'major': 'Computer Science'
}

print(student)
name = student['name']
print(f'Hello my name is {name}')
print('My major is '+ student.get('major'))

# Add key/value pair
student['gender'] = 'Male'
print(student['gender'])

# Get all the keys
print(student.keys())

# Get all the items
print(student.items())

# Remove items
del student['gender']

print(student)
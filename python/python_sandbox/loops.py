# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

students = ['John', 'Paul', 'Daniel', 'Smith']

for student in students:
  print(student)

fruits = ['Apple', 'Orange', 'Banana']

for fruit in fruits:
  print(fruit)
  if fruit == 'Orange':
    print(f'We break the loop because of we found {fruit}')
    break

# range

for counter in range(len(students)):
  print(students[counter])

for i in range(0, 11):
  print(f'Numbers: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0

while count<10:
  print(count)
  count+=1

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class Student:
  def __init__(self, name, age, email, major): # Constructor
    self.name = name
    self.age = age
    self.email = email
    self.major = major
  
  def greeting(self):
    return f'Hello, my name is {self.name} and I am {self.age}'

# Extend Class

class Lecturer(Student):
  def __init__(self, name, age, email, major): # Constructor
    self.name = name
    self.age = age
    self.email = email
    self.major = major


steve = Student('Steve Smith', 20, 'smith@gmail.com', 'Computer Science')
janet = Lecturer('Janet', 42, 'janet@gmail.com', 'Engineering')

# print(type(steve))
# print(steve.name)
# print(steve.major)

print(steve.greeting())
print(janet.greeting()) # Access the parent class
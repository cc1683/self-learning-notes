# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def greeting(name):
  print('Hello '+name+'! ')

greeting('Louis')

# Function with return values
def addTwoNumbers(num1, num2):
  return num1+num2

print(addTwoNumbers(100, 100))
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2, num3: num1+num2+num3

print(getSum(10, 10, 10))
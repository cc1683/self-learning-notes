# Python Coding Exercises from https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/

# Write a function that returns the maximum of two numbers.

# def max(num1, num2):
#     if num1>num2:
#         return num1
#     elif num2>num1:
#         return num2

# print(max(20,11))

'''
Write a function called fizz_buzz that takes a number.
    If the number is divisible by 3, it should return “Fizz”.
    If it is divisible by 5, it should return “Buzz”.
    If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    Otherwise, it should return the same number.
'''

# def fizz_buzz(num):
#     if (num % 3 == 0 and num % 5 == 0):
#         return 'FizzBuzz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     elif num % 3 == 0:
#         return 'Fizz'
#     else:
#         return num

# print(fizz_buzz(30))

'''
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
'''

# def validateSpeed(speed):
#     demerit = 0
#     speedAbove = 0
#     if speed < 70:
#         return 'Ok'
#     else:
#         speedAbove = (speed - 70) / 5
#         demerit += int(speedAbove)
#         if(demerit > 12):
#             return 'License suspended'
#         return f'Points: {demerit}'

# print(validateSpeed(300))

'''
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
    0 EVEN
    1 ODD
    2 EVEN
    3 ODD
'''

# def showNumbers(limit):
#     for i in range(0, limit+1):
#         if i % 2 == 0:
#             print(f'{i} EVEN')
#         else:
#             print(f'{i} ODD')

# showNumbers(5)

'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''

# def showNumbers(limit):
#     numbers = []
#     for i in range(1, limit+1):
#         if (i % 3 == 0 or i % 5 == 0):
#             numbers.append(i)
#     return numbers

# print(showNumbers(20))

'''
Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
'''

# def show_stars(rows):
#     for i in range(1, rows+1):
#         for i in range(1, i+1):
#             print('*', end = '')
#         print()

# show_stars(6)

# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

#! BUGS!
#! BUGS!
#! BUGS!

def showPrime(num):
    primeList = []
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                primeList.append(i)
                break
    return primeList
print(showPrime(20))

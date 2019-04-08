# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get file info
print('File name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to the file
myFile.write('I love Python Programming! ')
myFile.close()
print('Is closed: ', myFile.closed)

# Append to the file
myFile = open('myfile.txt', 'a')
myFile.write('I love JavaScript Programming! ')
myFile.close()

# Read from the file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)





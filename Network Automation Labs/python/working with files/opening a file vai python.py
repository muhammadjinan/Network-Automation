file = open('First.txt','r') # Opening file
contents = file.read()       # Reading file
print(contents)              # Printing the file content
file.close()                 # Closing the file
#print(file.closed)           # Checking whether the file is closed or not

# OR
# +-------------------------------+
# | file = open('First.txt','r')  |  # Opening file
# | print(file.read())            |  # Reading and printing the file content
# +-------------------------------+
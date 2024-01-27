file = open('First.txt','rt')
print(file.seek(3))     
print(file.read())      # Print from the curser point mentioned in above commant
print(file.tell())      # Tell the current position of the cursur in the file

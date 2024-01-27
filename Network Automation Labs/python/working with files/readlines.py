with open('First.txt','rt')as F:
    content=F.readlines()       # '.readline' print the 1st line, if you use the commant 2 times it gives 2 lines
    print(content)              # In output, each item will have'\n' at end because 'enter' is considered
    print(type(content))

   # replace above three command with 'print(list(F))' to get the same output
   # print(list(F))
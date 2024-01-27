with open('First.txt','rt')as F:
    content=F.read().splitlines()
    print(content[4])               # 4 is index and 5th line of 'First.txt' will be printed
    
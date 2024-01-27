with open('First.txt','rt')as F:
    # content=F.read()
    # print(type(content))          # Files are basically 'string'
    content=F.read().splitlines()   # Converting the file type form 'str' to 'list'
    print(type(content))
    print(content)
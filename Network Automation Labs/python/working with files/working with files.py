with open('First.txt','r') as F:
    content = F.read()  # At present the data type is 'str', when we change 'content = F.read().splitlines()' data type becomes 'list'
    print(content)      # Once converted into list we can select & print item via index
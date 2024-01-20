Branches=('KONDOTTY','KOCHI','DOHA','JEDDA','BANGLOR','CHENNAI','MADRAS')
no=1
print('HQ:',Branches[0])    # We can print items in a tuple with index 
print(type(Branches))       # Print the type of Array
for item in Branches:           # Python collections are called "Array"
    print(no,'-',item+'.')  # '+' is used to concatenate the adjacent argument
    no+=1                       # '+' removes space between two adjacent arguments while printing

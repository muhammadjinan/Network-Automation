LIST=[12,'HSR','BTM','CSR','Madivala','LalBag']
print('\n'+''.center(50,"-"))
print(LIST)      #[12, 'HSR', 'BTM', 'CSR', 'Madivala', 'LalBag']
print(LIST[2])   #BTM
print(LIST[1:-2])#['HSR', 'BTM', 'CSR']
print(LIST[:])   #[12, 'HSR', 'BTM', 'CSR', 'Madivala', 'LalBag']
print(LIST[1:3]) #['HSR', 'BTM']
print(LIST[3:])  #['CSR', 'Madivala', 'LalBag']
print(LIST[:3])  #[12, 'HSR', 'BTM']
print(LIST[0:3]) #[12, 'HSR', 'BTM']
print("".center(50,"-"))
print('Total Number of contents in the List is:',len(LIST))
print("".center(50,"-"))
if 'BTM' in LIST:
    print('YES found BTM')
else:
    print('NO such ITEM')
print("".center(50,"-"))
## Adding items in a LIST
LIST.append(23)     # Will add value/data to the last of the list
print('After Append\n', LIST)
LIST.insert(2,24)   # Insert Data to the specified index
print('After Insert\n',LIST)
LIST.remove('Madivala') # Removes the 1st occuring data
# If there is two Madivala, then the 1st Madivala will be removed
print('After removing',LIST)
LIST.pop(-2)    #.pop(index value) | Delete data at specified index
print('After POP',LIST)
del LIST[2]     # Delete data at the specified index
# 'LIST.clear()' is similar to 'del LIST[:]'
print('After Delete',LIST)
print("".center(50,"-"))
for item in LIST:
    print('Data types are',type(LIST))
print("".center(50,"-"),'\n')
Dic={}                                
for _ in range(3):                    
    key = input('Enter the key')
    value = input('Enter the value')
    Dic[key]=value                    # We can also use 'Dic.update({key:value})'
print(Dic)

# If there is a pre-existing data then the new items will get added with the pre-existing
# If we are inputting the same key as the pre-existing one, then the value of that key will get updated

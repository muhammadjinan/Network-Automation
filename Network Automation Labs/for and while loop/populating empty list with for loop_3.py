Branch_Router=['HSR','BTM','PUNE','GOA','ASAM','KOCHI','KZKD']
List2=[]                # Created a new empty list
i=0                     # Created a variable 'i' and assigned value '0' to it
for R in Branch_Router: # Assigned 'R' as the items of the list 'Branch_Router'
    List2.append(R)     #.append() is used to populate a list
    print(f'List2 is populating with-> {i}',List2)
    i+=1                # 1 is added to 'i' with the loop

# Run and see the difference with 
#   "populating empty list with for loop_2.py"
#   "populating empty list with for loop_3.py"
    
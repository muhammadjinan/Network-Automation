Branches={'CHENNAI','JEDDA','KOCHI','DELHI','BENGALURU'}
print('BEGINNING    :',Branches)
print('Tracker of company status\n'+''.center(66,'-'))
for i in range(len(Branches)):
    ClosedBr=Branches.pop()
    print('Closed Branch:',ClosedBr)
    print('THEN         :',Branches)

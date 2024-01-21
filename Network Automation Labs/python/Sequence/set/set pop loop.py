Branches={'CHENNAI','JEDDA','KOCHI','DELHI','BENGALURU'}
print('Tracker of company status\n'+''.center(63,'-'))
print('PRESENT   :',Branches)
for i in range(len(Branches)):
    OpenBr=Branches.pop()
    print('New Branch:',OpenBr)
    print('BEGINNING :',Branches)

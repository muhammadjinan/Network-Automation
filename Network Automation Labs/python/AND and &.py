a = 14
b = 4
print(''.center(20,'*'))
print(b and a)          #"lazy evaluation" both are true and print last checked
print(b & a)            #14=1110 4=0100 so 1110 AND 0100=0100 | (0100 = 4)
print(12 & 2)           #12=1100 2=0010 so 1100 AND 0010=0000 | (0000 = 0)
print(''.center(20,'*'))

if a<b and a>b:
    print("DONE")
else:
    print("FALSE")

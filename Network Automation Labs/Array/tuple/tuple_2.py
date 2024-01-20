Branches=('HSR','GOA','PUNE')
V1=V2=V3=0
for i in range(3):
    if i==0:
        V1=Branches[i]
        continue
    if i==1:
        V2=Branches[i]
        continue
    if i==2:
        V3=Branches[i]
print(V1,V2,V3)
import json
RD={
    'Router1':['1.1.1.1','admin','ccie'],
    'Router1':['2.2.2.2','admin2','ccie2'],
    'Router3':['3.3.3.3','admin3','ccie3']
}

with open('JSONfirst.json','w')as F:
    json.dump(RD,F)

Tmp=json.dumps(RD,indent=5)
print(type(Tmp))
print(Tmp)

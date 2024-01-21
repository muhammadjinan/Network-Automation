Router={'Router_ID':'1.1.1.1','Username':['admin','tom','jerry'],'Password':'cisco','Location':'GOA'}
print(Router)
# I want to change the Location from 'GOA' to 'HSR'
Router['Location']='HSR'
print('Updated Location:',Router)
for k,v in Router.items():    
    print(f'My Key is \"{k}\" and value is \"{v}\"')
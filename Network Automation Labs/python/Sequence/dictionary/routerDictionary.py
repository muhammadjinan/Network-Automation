Router={'Router_ID':'1.1.1.1','Username':['admin','tom','jerry'],'Password':'cisco','Location':'GOA'}
print(Router)
print(Router.get('Username'))
print(type(Router))
Tmp=(Router.items())
print(type(Tmp))
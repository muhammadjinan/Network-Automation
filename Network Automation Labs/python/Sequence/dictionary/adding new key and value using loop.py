Ro_ID={
    'R_ID': '1.1.1.1',
    'username':{'admin','tom','jerry'},
    'password':'password'
}
for k in range(1):      # Inside the range minimum 1 shoul be given for the value to get updated, empty will give error and <=0 will not give updated output
    Ro_ID.update({'password':'2.0.1'})
print(Ro_ID)
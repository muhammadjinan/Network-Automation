Ro_ID={
    'R_ID': '1.1.1.1',
    'username':{'admin','tom','jerry'},
    'password':'password'
}
Ro_ID.update({'password':'cisco'})                      # Updating password
print(Ro_ID)
Ro_ID.update({'password':input('Enter new password ')}) # Updating password recieved from the user
print(Ro_ID)
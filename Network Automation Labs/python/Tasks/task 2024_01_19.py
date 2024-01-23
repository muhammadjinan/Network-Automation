# Task: Accept Devices information from user into different Data type and use SET, LIST, TUPLE & print in the same file.
# User input method for accepting IP router ID and put into list tuple seperatly and use different method and print.

R_Info=[]
for I in range(3):
	R_Info.append(input("Enter the  Router Info "))
print(R_Info)
print(f'\"{R_Info[0]}\" is trying to establish connection with the server')

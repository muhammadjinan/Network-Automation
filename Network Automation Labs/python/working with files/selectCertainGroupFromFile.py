with open(r'E:\Files\Learning\Computer Networking\Networkers Home\Network Automation\Network Automation Labs\Devices.txt','rt') as FD:
    content = FD.readlines()
    dev = list()
    for line in content[1:]:
        dev.append(line.split(':'))   
    for i in dev:
        print(f'Pinging to {i[1]}')

    
    
    
    
    
    
    
    
    
content = FD.readlines()          # Each line are converted into items
print(content)
for item in content[1:]:          # [1:] will ignore the 1st item (i.e., 1st line)
    ip = item.split(":")[1]      # Now the each lines are splitted into different items with taking ':' as reference, and here we choose to print the value at 1st(index)
    print(ip)
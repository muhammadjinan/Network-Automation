from netmiko import Netmiko
connection = Netmiko(host='192.168.229.12', port='22', username='admin', password='ccie', device_type='cisco_ios')

# Send commands to the router
output = connection.send_command('sh ip int br')
print(output)
# OR (line 4, 5) = print(connection.send_command('sh ip int br'))

# To find the current prompt
promt = connection.find_prompt()
print('Current prompt is: ', promt)

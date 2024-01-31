from netmiko import Netmiko
connection = Netmiko(host='192.168.229.12', port='22', username='admin', password='ccie', device_type='cisco_ios')

promt = connection.find_prompt()
print(promt)

# In 'Netmiko' we need to enter certain commands to enter certain modes of Router

# To enter 'User execution mode' (router#) if in 'Privileged mode' (router>)
if '>' in promt:
    connection.enable()

# To enter 'Global configuration mode' (router(config)#) if not in the mode
if not connection.check_config_mode():
    connection.config_mode()

# Print the current prompt
print(connection.find_prompt())
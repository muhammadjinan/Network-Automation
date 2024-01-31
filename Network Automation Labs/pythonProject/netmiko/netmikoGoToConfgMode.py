from netmiko import Netmiko
connection = Netmiko(host='192.168.229.12', port='22', username='admin', password='ccie', device_type='cisco_ios')

promt = connection.find_prompt()
print(promt)

# In 'Netmiko' we need to enter certain commands to enter certain modes of Router

# Checking whether in 'Privileged mode' (router>) if in then go to
if '>' in promt:
    # To enter 'User execution mode' (router#) if in 'Privileged mode' (router>)
    connection.enable()

# Checking whether not in 'Global configuration mode' (router(config)#)
if not connection.check_config_mode():
    # To enter 'Global configuration mode' (router(config)#)
    connection.config_mode()

# We can enter to certain mode even without checking, just enter the command to enter the certain mode
# | connection.config_mode() | -> To enter 'Global configuration mode'

# Print the current prompt
print(connection.find_prompt())

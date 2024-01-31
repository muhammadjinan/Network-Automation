import paramiko
import time

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Declaring a variable 'router' which include the login credentials

router = {
    'hostname': '192.168.229.12',
    'port': '22',
    'username': 'admin',
    'password': 'ccie'
}

# Establishing connection with the router

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
if ssh_client.get_transport().is_active() == True:
    print('Connection Established with: ', router['hostname'])
else:
    print('Connection Error')

# Sending commands to the router

cmd = ssh_client.invoke_shell()

cmd.send('enable\n')
cmd.send('conf t\n')
cmd.send('int loo1\n')
cmd.send('ip add 1.1.1.1 255.255.255.255\n')
cmd.send('do sh ip int br\n')

time.sleep(1)  # 1sec delay

py_console = cmd.recv(10000)
py_console = py_console.decode('utf-8')  # Converting 'py_console' int UTF-8

print(py_console)  # To view the console output in python console

import paramiko

ssh_client = paramiko.SSHClient()
# print(type(ssh_client))
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
router = {
    'hostname': '192.168.229.12',
    'port': '22',
    'username': 'admin',
    'password': 'ccie'
}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
print('Connection status: ', ssh_client.get_transport().is_active())
# if ssh_client.get_transport().is_active()==True:
#     print('Connection is established')

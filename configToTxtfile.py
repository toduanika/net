from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_xe',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'secret': 'enablepass',
    'port': 22,
}

ssh = ConnectHandler(**cisco_router)

result = ssh.send_command('show running-config')

file = open('config.txt', 'w')

file.write(result)

file.close()
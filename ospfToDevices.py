from netmiko import ConnectHandler

devices = ["192.168.100.15", "192.168.100.16", "192.168.100.17", "192.168.100.18", "192.168.100.19"]


for device in devices:
    cisco_device = {
        'device_type': 'cisco_ios_telnet',
        'host': device,
        'username': 'developer',
        'password': 'C1sco12345',
        'secret': 'cisco',
        'port': 22,
    }

    ssh = ConnectHandler(**cisco_device)

    commands = ['router ospf 1',
            'network 10.0.0.0 0.255.255.255 area 0']

    ssh.enable()                                 
    config = ssh.send_config_set(commands)

    ssh.disconnect()


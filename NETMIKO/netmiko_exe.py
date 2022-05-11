import os
from netmiko import ConnectHandler

# Read password from environment variable
password = os.getenv("CISCO_SANDBOX_PASSWORD")

###############################################################################################
# cisco1 = {
#     'host': 'sandbox-iosxe-latest-1.cisco.com',
#     'username': 'developer',
#     'device_type': 'cisco_ios',
#     'password': password,
# }

# cisco2 = {
#     'host': 'ios-xe-mgmt.cisco.com ',
#     'username': 'developer',
#     'device_type': 'cisco_ios',
#     'password': password,
# }

# devices = [cisco1, cisco2]

# for device in devices:
#     print(f"\nHostname: {device['host']} ")
#     print('----' * 15)
#     conn = ConnectHandler(**device)
#     output = conn.send_command('show ip int brief')
#     print(output)

# config_commands = ['int loop 35', 'ip address 35.35.35.35 255.255.255.0']
# output = conn.send_config_set(config_commands)
# print(output)
###############################################################################################
# Send multiple commands from a file
with open('command_file.txt') as f:
    commands_to_send = f.read().splitlines()

cisco1 = {
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'device_type': 'cisco_ios',
    'password': password,
}

devices =[cisco1]

for device in devices:
    print(f"\nHostname: {device['host']}")
    print('----' * 15)
    conn = ConnectHandler(**device)
    output = conn.send_config_set(commands_to_send)
    print(output)
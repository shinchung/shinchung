# Netmiko SCP
import os
from netmiko import ConnectHandler, file_transfer

# Read password from environment variable
password = os.getenv("CISCO_SANDBOX_PASSWORD")

cisco1 = {
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'device_type': 'cisco_ios',
    'password': password,
    # 'file_system': 'flash:',
}

cisco2 = {
    'host': 'ios-xe-mgmt.cisco.com',
    'username': 'developer',
    'device_type': 'cisco_ios',
    'password': password,
    # 'file_system': 'flash:',
}

source_file = "csr1000v-mono-universalk9.16.09.03.SPA.pkg"
dest_file = "csr1000v-mono-universalk9.16.09.03.SPA.pkg"
direction = "get"
file_system = 'flash:'

    # Create the Netmiko SSH connection
for net_device in (cisco1):
    # file_system = net_device['file_system']

    # Create the Netmiko SSH connection
    ssh_conn = ConnectHandler(**net_device)
    transfer_dict = file_transfer(
        ssh_conn,
        source_file=source_file,
        dest_file=dest_file,
        file_system=file_system,
        direction=direction,
        overwrite_file=True,
    )
    print(transfer_dict)
    pause = input("Hit enter to continue: ")
#connecthandler
from netmiko import Netmiko
from getpass import getpass
password = getpass()
cisco1 = {
    'host': "192.168.1.201",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
}
cisco2 = {
    'host': "192.168.1.202",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
}
cisco3 = {
    'host': "192.168.1.203",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_xe',
}
nxos1 = {
    'host': "192.168.1.205",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'cisco_nxos',
}
arista1 = {
    'host': "192.168.1.208",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'arista_eos',
}
arista2 = {
    'host': "192.168.1.209",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'arista_eos',
}
srx1 = {
    'host': "192.168.1.207",
    'username': 'admin',
    'password': password,
    'secret': password,
    'device_type': 'juniper_junos',
}
for device in (cisco1, cisco2, arista1, arista2, nxos1, srx1):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show ip arp")
    print(output)
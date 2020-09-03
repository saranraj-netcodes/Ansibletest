#connecthandler
from netmiko import Netmiko
from getpass import getpass
password = getpass()
cisco1 = {
    'host': "192.168.1.201",
    'username': 'admin',
    'password': 'password',
    'secret': 'password'
    'device_type':'cisco_ios'
}
net_con = Netmiko(**cisco1)

print(net_con.find_prompt())
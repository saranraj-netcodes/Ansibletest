import ipdb

class NetworkDevice:
    def __init__(self, platform, ip_address, username="admin"):
        self.platform = platform
        self.ip_address = ip_address
        self.username = username

    def print_ip(self):
        print(f"IP Addr: {self.ip_address}")
    
    def print_platform(self):
        print(f"Platfrom: {self.platform}")
    
    def print_username(self):
        print(f"user: {self.username}")


# ipdb.set_trace()
router1 = NetworkDevice("Cisco IOS", "192.168.1.201")
router2 = NetworkDevice("Cisco IOS XE", "192.168.1.202", username="root")

router1.print_ip()
router2.print_ip()
router1.print_platform()
router2.print_username()
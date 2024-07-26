import os
import subprocess
import netifaces

class InterfaceManager:
    def __init__(self, interface):
        self.interface = interface

    def get_interface_name(self):
        interface_path = self._get_interface_path()
        item = self._search_for_dir(interface_path)
        return self._cut_name(item)

    def _get_interface_path(self):
        net_path = '/sys/class/net'
        return os.path.join(net_path, self.interface)

    def _search_for_dir(self, interface_path):
        for item in os.listdir(interface_path):
            if item.startswith('lower'):
                return item
        return None

    def _cut_name(self, item):
        return item[6:]

    def change_cos(self, cos_value, verbose=False):
        subprocess.run(["sudo", "ip", "link", "set", self.interface, "type", "vlan", "egress", f"0:{cos_value}"], check=True)
        if verbose:
            print(f"COS value for {self.interface} has been changed to {cos_value}")

    def get_ip(self):
        try:
            interface_ip = netifaces.ifaddresses(self.interface)[netifaces.AF_INET][0]['addr']
            return interface_ip
        except KeyError:
            print(f"Interface {self.interface} not found")
            exit(1)
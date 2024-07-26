from utils import *

class COSTester:
    def __init__(self, interface, verbose):
        self.interface = interface
        self.verbose = verbose
        self.received_cos = []

    def change_cos_and_check(self, cos_value):
        InterfaceManager.change_cos(self.interface, cos_value, self.verbose)
        if self.verbose:
            print(f"Changed COS to {cos_value}\n")
        if not self.verbose:
            print("*" * cos_value)
        prio = NetworkUtils.check_interface_packet(InterfaceManager.get_interface_name(self.interface))
        self.received_cos.append(prio)

    def cleanup(self):
        InterfaceManager.change_cos(self.interface, 0, self.verbose)

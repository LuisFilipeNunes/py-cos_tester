from utils import *

class COSTester:
    def __init__(self, interface, verbose):
        self.interface = interface
        self.verbose = verbose
        self.received_cos = []
        self.int_manager = InterfaceManager(interface)

    def change_cos_and_check(self, cos_value):
        self.int_manager.change_cos(cos_value, self.verbose)
        if self.verbose:
            print(f"Changed COS to {cos_value}")
        if not self.verbose:
            print("*" * cos_value)
        prio = NetworkUtils.check_interface_packet(self.int_manager.get_interface_name())
        self.received_cos.append(prio)

    def cleanup(self):
       self.int_manager.change_cos(0, self.verbose)

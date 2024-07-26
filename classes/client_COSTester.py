from .COS_Tester import COSTester
import time
from utils import *

class ClientCOSTester(COSTester):
    def __init__(self, interface, server_ip, verbose):
        super().__init__(interface, verbose)
        self.server_ip = server_ip
        self.heartbeat_manager = HeartbeatManager(server_ip)
        
    def run(self):
        client_heartbeat = 1
        for cos_value in range(8):
            client_heartbeat = self.heartbeat_manager.connect_heart(client_heartbeat, self.verbose)
            self.change_cos_and_check(cos_value)
            time.sleep(3)
        
        ResultsConstructor.construct("Server", self.received_cos)
        self.cleanup()
        print("Client shutting down after all COS tests.")
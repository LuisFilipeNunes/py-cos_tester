from COSTester import COSTester
import socket
from utils import *

class ServerCOSTester(COSTester):
    def run(self):
        interface_ip = InterfaceManager.get_ip(self.interface)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((interface_ip, 5551))
        server_socket.listen(1)
        
        if self.verbose:
            print(f"Server listening on {self.interface} - {interface_ip}:5551")
        
        server_heartbeat = 0
        for cos_value in range(8):
            conn, server_heartbeat = HeartbeatManager.beat_heart(server_socket, server_heartbeat, self.verbose)
            self.change_cos_and_check(cos_value)
            conn.close()
        
        ResultsConstructor.construct("Client", self.received_cos)
        self.cleanup()
        server_socket.close()
        print("Server shutting down after all COS tests.")
from .COS_Tester import COSTester
import socket
from utils import *

class ServerCOSTester(COSTester):
    
    def __init__(self, interface, verbose):
        super().__init__(interface, verbose)
        self.interface_manager = InterfaceManager(interface)
    
    def run(self):
        interface_ip = self.interface_manager.get_ip()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((interface_ip, 5551))
        server_socket.listen(1)
        
        if self.verbose:
            print(f"Server listening on {self.interface} - {interface_ip}:5551")
        
        server_heartbeat = 0
        for cos_value in range(8):
            if not isinstance(server_socket, socket.socket):
                print(f"Error: server_socket is not a valid socket object. Type: {type(server_socket)}")
                return
            conn, server_heartbeat = HeartbeatManager.beat_heart(server_socket, server_heartbeat, self.verbose)
            self.change_cos_and_check(cos_value)
            conn.close()
        
        ResultsConstructor.construct("Client", self.received_cos)
        self.cleanup()
        server_socket.close()
        print("Server shutting down after all COS tests.")
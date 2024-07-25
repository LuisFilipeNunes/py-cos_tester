#!/usr/bin/env python3

import argparse
import time
import socket
from utils import (change_cos,check_interface_packet, get_interface_name,  
                   get_ip_from_interface, beat_heart, connect_heart, construct_results)


def run_server(interface, verbose):
    interface_ip = get_ip_from_interface(interface)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((interface_ip, 5551))
    server_socket.listen(1)
    
    if verbose : print(f"Server listening on {interface} - {interface_ip}:5551")
    
    server_heartbeat = 0
    received_cos = []
    for cos_value in range(8):
        
        conn, server_heartbeat = beat_heart(server_socket, server_heartbeat, verbose)

        change_cos(interface, cos_value, verbose)
        if verbose : print(f"Changed COS to {cos_value}\n")
        
        if not verbose : print("*" * cos_value)
        
        prio = check_interface_packet(get_interface_name(interface))
        received_cos.append(prio)
        conn.close()
        
    construct_results("Client", received_cos)
    
    #Return to the default configuration
    change_cos(interface, 0, verbose)
    server_socket.close()
    print("Server shutting down after all COS tests.")

def run_client(interface, server_ip, verbose):
    client_heartbeat = 1
    received_cos = []
    for cos_value in range(8):
        
        client_heartbeat = connect_heart(server_ip, client_heartbeat, verbose)
        
        change_cos(interface, cos_value, verbose)
        if verbose : print(f"Changed COS to {cos_value}\n")
        
        if not verbose : print("*" * cos_value)
        
        prio = check_interface_packet(get_interface_name(interface))
        received_cos.append(prio)        
        time.sleep(3)
        
    construct_results("Server", received_cos)
    
    #Return to the default configuration
    change_cos(interface, 0, verbose)
    print("Client shutting down after all COS tests.")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change COS with heartbeat")
    parser.add_argument("-i", "--interface", required=True, help="Network interface")
    parser.add_argument("-m", "--mode", choices=["server", "client"], required=True, help="Run as server or client")
    parser.add_argument("-a", "--address", help="Server address (required for client mode)")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable verbose output")
    args = parser.parse_args()

    if args.mode == "server":
        run_server(args.interface, args.verbose)
    elif args.mode == "client":
        if not args.address:
            parser.error("Server address is required for client mode")
        run_client(args.interface, args.address, args.verbose)

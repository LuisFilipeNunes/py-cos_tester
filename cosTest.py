#!/usr/bin/env python3

import argparse
from classes import *

def main():
    parser = argparse.ArgumentParser(description="Change COS with heartbeat")
    parser.add_argument("-i", "--interface", required=True, help="Network interface")
    parser.add_argument("-m", "--mode", choices=["server", "client"], required=True, help="Run as server or client")
    parser.add_argument("-a", "--address", help="Server address (required for client mode)")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable verbose output")
    args = parser.parse_args()

    if args.mode == "server":
        tester = ServerCOSTester(args.interface, args.verbose)
    elif args.mode == "client":
        if not args.address:
            parser.error("Server address is required for client mode")
        tester = ClientCOSTester(args.interface, args.address, args.verbose)
    
    tester.run()

if __name__ == "__main__":
    main()
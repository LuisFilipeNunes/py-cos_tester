# COS Checker

This project provides a tool for testing Class of Service (COS) settings on network interfaces. It includes both server and client components to facilitate COS testing across network connections.

## Features

- Server and client modes for COS testing
- Supports COS values from 0 to 7
- Heartbeat mechanism to synchronize server and client
- Verbose output option for detailed logging
- Automatic detection of interface IP addresses
- Results compilation for easy analysis

## Requirements

- Python 3.x
- Tabulate 0.9.0 at least,
- Scapy 2.5.0 at least
- Netifaces 0.11.0
- Network interface with COS support

## Usage

### Server Mode

```bash
python cosTest.py -i <interface> -m server [-v]
``` 
### Client Mode

```bash
python cosTest.py -i <interface> -m client -a <server_ip> [-v]
``` 

### Arguments
* -i, --interface: Network interface to use for testing
* -m, --mode: Run as "server" or "client"
* -a, --address: Server IP address (required for client mode)
* -v, --verbose: Enable verbose output

### How it Works

1. The server listens on the specified interface.
2. The client connects to the server.
3. Both server and client cycle through COS values 0-7.
4. For each COS value:
    * The COS is set on the interface
    * A packet is sent and its priority is checked
    * Results are recorded
5. After all tests, results are compiled and displayed.

### Output

The script provides a summary of received COS values for each test, allowing you to verify if the COS settings are being applied and recognized across the network.

### Notes

Ensure you have the necessary permissions to change network interface settings.
This script requires root/administrator privileges to modify COS values.
### Important Alert

For the correct use of the script, the user must ensure that the network interface is a vlan subtype and that the real physical interface is in the same namespace of the network interface with a vlan subtype. 
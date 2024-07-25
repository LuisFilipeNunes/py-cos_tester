import scapy.all as scapy
import sys

def check_interface_packet(interface):
    packet = scapy.sniff(iface=interface, count=1, filter="tcp and port 5551")[0]
    
    if scapy.Ether in packet:
        if scapy.Dot1Q in packet:
            prio = packet[scapy.Dot1Q].prio
        else:
            prio = "N/A"
            
        return prio 
    else:
        return -1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_vlan.py <interface>")
        sys.exit(1)
    interface = sys.argv[1]
    check_interface_packet(interface)

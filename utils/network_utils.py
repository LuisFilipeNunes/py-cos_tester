import scapy.all as scapy

class NetworkUtils:
    @staticmethod
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
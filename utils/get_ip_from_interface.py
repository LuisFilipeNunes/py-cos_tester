import netifaces

def get_ip_from_interface(interface):
    try:
        interface_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        return interface_ip
    except KeyError:
        print(f"Interface {interface} not found")
        exit(1)
    
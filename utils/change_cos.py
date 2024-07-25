import subprocess

def change_cos(interface, cos_value, verbose):
    subprocess.run(["sudo", "ip", "link", "set", interface, "type", "vlan", "egress", f"0:{cos_value}"], check=True)
    if verbose : print(f"COS value for {interface} has been changed to {cos_value}")
import os

def get_interface_name(interface_prefix):
    interface_path = get_interface_path(interface_prefix)
    item = search_for_dir(interface_path)
    item = cut_name(item)
    return item

def get_interface_path(interface_prefix):
    net_path = '/sys/class/net'
    interface_path = os.path.join(net_path, interface_prefix)
    return interface_path

def search_for_dir(interface_path):
    for item in os.listdir(interface_path):
        if item.startswith('lower'):
            return item
    return None

def cut_name(item):
    return item[6:]
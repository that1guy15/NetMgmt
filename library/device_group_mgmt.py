import os
import sys
from collections import defaultdict
import yaml
from yaml.representer import Representer

inv_dir = 'inventory/'


# Create New Device in Inventory
def device_add(device, mgmt, role, network, username, password):
    device_conf = device + '.yaml'
    print device_conf
    device_dir = inv_dir + device + '/'
    print device_dir
    directory = os.path.dirname(device_dir) + '/'
    print directory
    if not os.path.exists(directory):
        os.makedirs(directory)
    target_dict = defaultdict(dict)
    target_dict[device]['name'] = device
    target_dict[device]['mgmt_ip'] = mgmt_ip
    target_dict[device]['role'] = role
    target_dict[device]['network'] = network
    target_dict[device]['username'] = username
    target_dict[device]['password'] = password

    with open(directory + device_conf, 'w') as outfile:
        yaml.add_representer(defaultdict, Representer.represent_dict)
        yaml.dump(target_dict, outfile, default_flow_style=False)
        return device + ' config added to inventory'


device_name = 'spine1'
mgmt_ip = '1.1.1.2'
role = 'spine'
network = 'datacenter'
username = 'admin'
password = 'admin'

device_add(device_name, mgmt_ip, role, network, username, password)






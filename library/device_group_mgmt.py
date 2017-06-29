import os
import os.path
import sys
from collections import defaultdict, OrderedDict
import yaml
from yaml.representer import Representer, SafeRepresenter

inv_dir = 'inventory/'

device_name = ''
mgmt_ip = ''
role = ''
roles = []
network = ''
username = ''
password = ''


# Create New Network
def network_add(network, roles, username, password):
    network_conf = network + '.yaml'
    network_dir = inv_dir + network + '/'
    directory = os.path.dirname(network_dir) + '/'
    roles = roles.split()

    # Check if network exist
    try:
        os.path.exists([directory + network_conf])
    except:
        raise
        sys.exit(1)
        return network + ' already in inventory!'

    # Create network directory
    try:
        os.makedirs(directory)
    except OSError:
        if not os.path.isdir(directory):
            return 'Unable to add ' + network + ': OSError'
            raise

    # Build network settings structure
    target_dict = defaultdict(dict)
    target_dict[network]['network'] = network
    target_dict[network]['roles'] = roles
    target_dict[network]['username'] = username
    target_dict[network]['password'] = password

    # Build network settings file
    try:
        with open(directory + network_conf, 'w') as outfile:
            yaml.add_representer(defaultdict, Representer.represent_dict)
            yaml.add_representer(OrderedDict, Representer.represent_dict)
            yaml.add_representer(unicode, SafeRepresenter.represent_unicode)
            yaml.dump(target_dict, outfile, default_flow_style=False)
            return network + ' network added to inventory!'
    except:
        raise


# Create New Device in Inventory
def device_add(device, mgmt_ip, role, network, username, password):
    device_conf = device + '.yaml'
    device_dir = inv_dir + network + '/' + device + '/'
    directory = os.path.dirname(device_dir) + '/'

    # Check if device exist
    try:
        os.path.exists([directory + device_conf])
    except:
        raise
        sys.exit(1)
        return device + ' already in inventory!'

    # Create device directory
    try:
        os.makedirs(directory)
    except OSError:
        if not os.path.isdir(directory):
            return 'Unable to add ' + device + ': OSError'
            raise

    # Build device settings structure
    target_dict = defaultdict(dict)
    target_dict[device]['name'] = device
    target_dict[device]['mgmt_ip'] = mgmt_ip
    target_dict[device]['role'] = role
    target_dict[device]['network'] = network
    target_dict[device]['username'] = username
    target_dict[device]['password'] = password

    # Build device settings file
    try:
        with open(directory + device_conf, 'w') as outfile:
            yaml.add_representer(defaultdict, Representer.represent_dict)
            yaml.add_representer(OrderedDict, Representer.represent_dict)
            yaml.add_representer(unicode, SafeRepresenter.represent_unicode)
            yaml.dump(target_dict, outfile, default_flow_style=False)
            return device + ' config added to inventory!, success'
    except:
        raise

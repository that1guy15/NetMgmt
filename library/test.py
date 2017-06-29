device_name = 'spine2'
mgmt_ip = '1.1.1.1'
role = 'spine'
network = 'TX-DC1'
username = 'admin'
password = 'admin'


def device_add(device, mgmt_ip, role, network, username, password):
    device_conf = device + '.yaml'
    device_dir = inv_dir + network + '/' + device + '/'
    directory = os.path.dirname(device_dir)
    print '===================='
    print device_conf
    print device_dir
    print directory
    print '===================='
    try:
        os.path.exists([directory + device_conf])
    except:
        raise
        sys.exit(1)
        return device + ' already in inventory!'
    try:
        os.makedirs(directory)
    except OSError:
        if not os.path.isdir(directory):
            return 'Unable to add ' + device + ': OSError'
            raise
    target_dict = defaultdict(dict)
    target_dict[device]['name'] = device
    target_dict[device]['mgmt_ip'] = mgmt_ip
    target_dict[device]['role'] = role
    target_dict[device]['network'] = network
    target_dict[device]['username'] = username
    target_dict[device]['password'] = password
    try:
        with open(directory + device_conf, 'w') as outfile:
            yaml.add_representer(defaultdict, Representer.represent_dict)
            yaml.add_representer(OrderedDict, Representer.represent_dict)
            yaml.add_representer(unicode, SafeRepresenter.represent_unicode)
            yaml.dump(target_dict, outfile, default_flow_style=False)
            return device + ' config added to inventory!, success'
    except:
        raise


device_add(device_name, mgmt_ip, role, network, username, password)
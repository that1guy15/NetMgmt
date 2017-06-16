#!/srv/netmgmt/venv/bin/python2.7

# Based on: https://serversforhackers.com/running-ansible-2-programmatically

import os
import sys
import datetime
import argparse
from datetime import datetime
from ansible.executor import playbook_executor
from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

parser = argparse.ArgumentParser(description='Arguments passed to the script.')
parser.add_argument('device', help='all, none, Group Name, IP address or resolvable hostname. Must be in hosts file')
parser.add_argument('playbook', help='playbook to run')
args = parser.parse_args()

timestamp = datetime.now().strftime('%m/%d/%Y %I:%M:%S')
src_playbook = args.playbook
src_hosts = 'hosts'
src_limit = args.device


class Options(object):
    """
    Options class to replace Ansible OptParser
    """
    def __init__(self, **kwargs):
        props = (
            'ask_pass', 'ask_sudo_pass', 'ask_su_pass', 'ask_vault_pass',
            'become_ask_pass', 'become_method', 'become', 'become_user',
            'check', 'connection', 'diff', 'extra_vars', 'flush_cache',
            'force_handlers', 'forks', 'inventory', 'listhosts', 'listtags',
            'listtasks', 'module_path', 'module_paths',
            'new_vault_password_file', 'one_line', 'output_file',
            'poll_interval', 'private_key_file', 'python_interpreter',
            'remote_user', 'scp_extra_args', 'seconds', 'sftp_extra_args',
            'skip_tags', 'ssh_common_args', 'ssh_extra_args', 'subset', 'sudo',
            'sudo_user', 'syntax', 'tags', 'timeout', 'tree',
            'vault_password_files', 'verbosity')
            
        for property in props:
            if property in kwargs:
                setattr(self, property, kwargs[property])
            else:
                setattr(self, property, None)


class Runner(object):
    def __init__(
            self, playbook, display, hosts='hosts', limit_to=None, options={}, passwords={},
            vault_pass=None):
        
        # Set options
        self.options = Options()
        for key, value in options.iteritems():
            setattr(self.options, key, value)

        # Set global verbosity
        self.display = display
        self.display.verbosity = self.options.verbosity
        # Executor has its own verbosity setting
        playbook_executor.verbosity = self.options.verbosity

        # Gets data from YAML/JSON files
        self.loader = DataLoader()
        # Set vault password
        if vault_pass is not None:
            self.loader.set_vault_password(vault_pass)
        elif 'VAULT_PASS' in os.environ:
            self.loader.set_vault_password(os.environ['VAULT_PASS'])

        # All the variables from all the various places
        self.variable_manager = VariableManager()
        if self.options.python_interpreter is not None:
            self.variable_manager.extra_vars = {
                'ansible_python_interpreter': self.options.python_interpreter
            }
        
        # Set inventory, using most of above objects with optional limit subset
        self.limit_to = limit_to
        self.inventory = Inventory(
            loader=self.loader, variable_manager=self.variable_manager,
            host_list=hosts)
        
        if len(self.inventory.list_hosts()) == 0:
            # Empty inventory
            self.display.error("Provided hosts list is empty.")
            sys.exit(1)

        self.inventory.subset(self.options.subset)

        if len(self.inventory.list_hosts()) == 0:
            # Invalid limit
            self.display.error("Specified limit does not match any hosts.")
            sys.exit(1)

        if self.limit_to:
            # inventory.subset() is equivalent to the cli param --limit=
            self.inventory.subset(self.limit_to)
    
        self.variable_manager.set_inventory(self.inventory)
        
        # Setup playbook executor, but don't run until run() called
        self.pbex = playbook_executor.PlaybookExecutor(
            playbooks=[playbook],
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options,
            passwords=passwords)

    def run(self):
        # Run Playbook and get stats
        self.pbex.run()
        stats = self.pbex._tqm._stats

        return stats
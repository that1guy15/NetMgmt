#!/bin/bash

echo "Provisioning virtual machine..."

echo "Installing Needed stuffs"
    yum install -y git > /dev/null
    yum install -y vim > /dev/null
    yum install -y epel-release > /dev/null

echo "Installing Ansible"
	yum install -y ansible > /dev/null
	
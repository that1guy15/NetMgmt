#!/bin/bash

echo "Provisioning virtual machine..."

echo "Installing Needed stuffs"
    sudo add-apt-repository ppa:git-core/ppa  > /dev/null
    sudo apt-get update  > /dev/null
    sudo apt-get install git  > /dev/null

echo "Installing Ansible"
	sudo apt-get install ansible > /dev/null
	
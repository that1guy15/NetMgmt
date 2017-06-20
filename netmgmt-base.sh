#!/bin/bash

echo "Provisioning virtual machine..."
echo "*******************************"
echo "*******************************"
echo "INSTALL ANSIBLE"
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
	sudo apt-get install ansible > /dev/null
	
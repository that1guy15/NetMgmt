#!/bin/bash

echo "Provisioning virtual machine..."

echo "INSTALL GIT"
    sudo add-apt-repository ppa:git-core/ppa
    sudo apt-get update
    sudo apt-get install git > /dev/null

echo "INSTALL ANSIBLE"
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
	sudo apt-get install ansible > /dev/null
	
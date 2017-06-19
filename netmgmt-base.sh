#!/bin/bash

echo "Provisioning virtual machine..."

echo "INSTALL GIT"
    sudo add-apt-repository ppa:git-core/ppa > /dev/null
    sudo apt-get update > /dev/null
    sudo apt-get install git > /dev/null

echo "INSTALL ANSIBLE"
    sudo apt-add-repository ppa:ansible/ansible > /dev/null
    sudo apt-get update > /dev/null
	sudo apt-get install ansible > /dev/null
	
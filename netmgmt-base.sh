#!/bin/bash

echo "Provisioning virtual machine..."

echo "INSTALL GIT"
    sudo su -
    sudo add-apt-repository ppa:git-core/ppa  > /dev/null
    sudo apt-get update  > /dev/null
    sudo apt-get install git  > /dev/null

echo "INSTALL ANSIBLE"
    sudo echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list
	sudo apt-get install ansible > /dev/null
	
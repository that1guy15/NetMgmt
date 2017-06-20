#!/bin/bash

echo "Provisioning virtual machine..."
echo "*******************************"
echo "*******************************"

echo "ADD APT-GET REPOS"
    sudo su -
    sudo add-apt-repository ppa:git-core/ppa -y > /dev/null
    sudo apt-add-repository ppa:ansible/ansible -y > /dev/null
    sudo apt-get update

echo "INSTALL GIT"
    sudo apt-get install git > /dev/null

echo "INSTALL ANSIBLE"
	sudo apt-get install ansible > /dev/null

echo "CLONE GITHUB PROJECT REPO"
	cd /srv
	git clone https://github.com/that1guy15/netmgmt.git > /dev/null
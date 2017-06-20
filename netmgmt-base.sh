#!/bin/bash

echo "Provisioning virtual machine..."
echo "*******************************"
echo "*******************************"

echo "ADD APT-GET REPOS"
    sudo add-apt-repository ppa:git-core/ppa
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update

echo "INSTALL GIT"
    sudo apt-get install git > /dev/null

echo "INSTALL ANSIBLE"
	sudo apt-get install ansible > /dev/null
	
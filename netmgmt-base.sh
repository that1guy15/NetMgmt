#!/bin/bash

echo "Provisioning virtual machine..."
echo "*******************************"
echo "*******************************"

echo "ADD APT-GET REPOS"
    sudo su -
    sudo add-apt-repository ppa:git-core/ppa -y > /dev/null
    sudo apt-add-repository ppa:ansible/ansible -y > /dev/null
    sudo apt-get update -y

echo "INSTALL GIT"
    sudo apt-get install git -y > /dev/null

echo "INSTALL ANSIBLE"
	sudo apt-get install ansible -y > /dev/null

echo "CLONE GITHUB PROJECT REPO"
	cd /srv
	sudo git clone https://github.com/that1guy15/netmgmt.git > /dev/null
	sudo chown -R vagrant.vagrant netmgmt

echo "GIT PUSH TO DEPLOY"
    cd /srv/netmgmt/.git/hooks/
    git config receive.denyCurrentBranch updateInstead
    cat >> push-to-checkout << EOF
    /bin/sh
    echo >&2 updating from $(git rev-parse HEAD)
    echo >&2 updating to "$1"

    git update-index -q --refresh && git read-tree -u -m HEAD "$1" || {
        status=$?
        echo >&2 read-tree failed
        exit $status
    }
    EOF
# NetMgmt
Network automation and config management tool

# Vagrant servers  
Deployment server: CentOS/7 w/ Ansible 2.3.0  
Target server: ubuntu/trusty64  
  
#Setup Steps:  
  
Clone repo to deployment server  
```git clone https://github.com/that1guy15/NetMgmt.git```   
  
```cd NetMgmt```  
```ansible-playbook deploy/setup-server.yml --ask-sudo-pass```  
```ansible-playbook devops/deploy.yml --ask-sudo-pass```  
  
From web-browser got http://127.0.0.1:8080

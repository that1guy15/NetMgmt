# NetMgmt
Network automation and config management tool  
  
Main goals of this project will be:
1) build and push full config of Leaf/spine fabric
2) build, validate and push changes
2) build repository for all configs 
3) diff tool to show changes
  
and maybe other stuff as I move along.

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

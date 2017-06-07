# ansible-flask-demo
Demo used to deploy a Flask website from scratch 

# Vagrant servers  
Deployment server: CentOS/7 w/ Ansible 2.2.0  
Target server: ubuntu/trusty64  
  
#Setup Steps:  
  
Clone repo to deployment server  
```git clone https://github.com/that1guy15/ansible-flask-demo.git```   
  
```cd ansible-flask-demo```  
```ansible-playbook devops/setup-server.yml```  
```ansible-playbook devops/deploy.yml```  
  
From web-browser got http://127.0.0.1:8080

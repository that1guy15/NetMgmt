Vagrant.configure("2") do |config|
  config.vm.define "ansible1" do |ansible1|
    ansible1.vm.box = "centos/7"
    ansible1.vm.hostname = "ansible1"

    ansible1.vm.network "private_network", ip: "192.168.100.100",
      virtualbox__intnet: "internal"
  
    ansible1.vm.provider "virtualbox" do |vb|
       vb.memory = "512"
    end

    ansible1.vm.provision "shell",
      path: "ansible1.sh" 
  
  end
  
  config.vm.define "webSrv1" do |webSrv1|
    webSrv1.vm.box = "ubuntu/trusty64"
    webSrv1.vm.hostname = "webSrv1"
    webSrv1.vm.network "forwarded_port", guest: 80, host: 8080

    webSrv1.vm.network "private_network", ip: "192.168.100.101",
      virtualbox__intnet: "internal"
  
    webSrv1.vm.provider "virtualbox" do |vb|
       vb.memory = "512"
    end
  end
end
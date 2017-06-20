Vagrant.configure("2") do |config|
  config.vm.define "netmgmt1" do |netmgmt1|
    netmgmt1.vm.box = "ubuntu/trusty64"
    netmgmt1.vm.hostname = "NetMgmt"
    netmgmt1.vm.network "forwarded_port", guest: 80, host: 8080

    netmgmt1.vm.network "private_network", ip: "192.168.100.100",
      virtualbox__intnet: "internal"

    netmgmt1.vm.provider "virtualbox" do |vb|
       vb.memory = "512"
    end

    netmgmt1.vm.provision "shell",
      path: "netmgmt-base.sh"
  end
end
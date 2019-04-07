# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.hostname = "docker-test"
  config.vm.network "private_network", ip: "10.10.10.10"
  config.vm.provider "virtualbox" do |v|
    v.cpus = 2
    v.memory = 2048
  end
  config.vm.provision "shell", inline: "
  sudo yum -y install vim docker docker-client
  sudo usermod -aG dockerroot vagrant
  sudo systemctl enable docker
  sudo systemctl start docker
  sudo docker swarm init --advertise-addr 10.10.10.10
  cd /vagrant/docker/flask-from
  sudo docker build -t jjh/flask:from .
  sudo docker stack deploy -c docker-compose.yml con-test
  "
end

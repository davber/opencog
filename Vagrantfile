# -*- mode: ruby -*-
# # vi: set ft=ruby :

# QuickStart
# 1. vagrant up
# 2. vagrant ssh
# Optional
# 1. Change Ubuntu archive mirror to a local mirror
# 2. Change vb.customize memory and cpus values
# 3. On Linux hosts, use provider vagrant-lxc
# More
# http://wiki.opencog.org/w/Setup_OpenCog_development_environment_VM_using_Vagrant
# http://wiki.opencog.org/w/Building_OpenCog

Vagrant.configure("2") do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "http://files.vagrantup.com/trusty64.box"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Our environment currently consists of only one box
  config.vm.define 'cogbox2' do |machine|
    machine.vm.hostname = "cogbox2"

    # Port forwarding for AtomSpace Visualizer.
    # Set IP_ADDRESS = '0.0.0.0' in /opencog/python/web/api/restapi.py and
    # run the Visualizer on host.
    machine.vm.network "forwarded_port", guest: 5000, host: 5001

    # Set --host to 192.168.50.2 when running opencog-server.sh in RelEx,
    # to pass RelEx's OpenCog scheme output to cogbox.
    machine.vm.network "private_network", ip: "192.168.50.2"

    machine.vm.provider :virtualbox do |vb|
        vb.name = "cogbox2"
        vb.customize [
                     "modifyvm", :id,
                     "--memory", "1536",
                     "--name", "opencog-dev-vm-2",
                     "--cpus", "1"
                     ]
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/ansible/opencog.yml"
    ansible.groups = {
      "opencogs" => ["cogbox2"]
    }
    ansible.sudo = true
    ansible.tags = ENV['TAGS'] unless !ENV['TAGS'] || ENV['TAGS'].empty?
    ansible.verbose = ENV['VERBOSE'] unless !ENV['VERBOSE'] || ENV['VERBOSE'].empty?
    ansible.extra_vars = {
      # Nothing for now, but please add when needed
    }
  end
end

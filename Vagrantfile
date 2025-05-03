Vagrant.configure("2") do |config|
    (1..1).each do |i|
      config.vm.define "aws-#{i}" do |k8s|
        k8s.vm.box = "ubuntu/bionic64"
        k8s.vm.hostname = "aws-#{i}"
        # k8s.vm.network "private_network", ip: "172.89.1.1#{i}"
        k8s.vm.provider "virtualbox" do |vb|
          vb.gui = true
          vb.cpus = 2
          vb.memory = "2048"
        end
  
        # Instalar Docker, Kind e Kubectl
        k8s.vm.provision "shell", inline: <<-SHELL
          # Atualizar pacotes e instalar dependências
          apt-get update
          apt-get install -y ca-certificates curl apt-transport-https software-properties-common gnupg
  
          # Adicionar repositório do Docker
          install -m 0755 -d /etc/apt/keyrings
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | tee /etc/apt/keyrings/docker.asc
          echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list
          
          apt-get update
          apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  
          # Testar Docker
          docker run hello-world || echo "Docker instalado com sucesso."
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          apt-get install unzip
        #unzip awscliv2.zip
        #sudo ./aws/install
         
        SHELL
  
        # Copiar arquivo config.yaml
        #k8s.vm.provision "file", source: "./config.yaml", destination: "/home/vagrant/config.yaml"
      end
    end
  end
  
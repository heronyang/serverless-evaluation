# Install docker
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
apt-cache policy docker-engine
sudo apt install -y docker-engine
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart

# Install languages
sudo apt -y install golang-go
sudo apt -y install python-dev
sudo apt -y install python3-dev

# Install
sudo apt update
sudo apt -y upgrade
sudo apt install -y make
sudo apt install -y build-essential
git clone https://github.com/open-lambda/open-lambda.git
cd open-lambda
make

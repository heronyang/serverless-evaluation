sudo apt update

# Clone openwhisk
git clone --depth=1 https://github.com/openwhisk/openwhisk.git

# Dependencies
sudo apt install python-dev
sudo apt install -y python-pip
sudo pip install --upgrade pip
sudo apt install -y build-essential libssl-dev libffi-dev
sudo pip install ansible==2.1.2.0

# Change current directory to openwhisk
cd openwhisk

# Install all required software
(cd tools/ubuntu-setup && ./all.sh)

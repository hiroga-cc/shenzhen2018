sudo apt-get install -q python-pip
sudo apt-get install -q python-pygame

sudo apt install -y npm
sudo npm install n -g
sudo n stable
sudo ln -sf /usr/local/bin/node /usr/bin/node
sudo ln -s /usr/local/bin/npm /usr/bin/npm
sudo apt purge -y nodejs npm

pip install -r requirements.txt
npm install -g blockchain-wallet-service --unsafe-perm

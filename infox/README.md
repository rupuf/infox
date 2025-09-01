pkg update && pkg upgrade -y
pkg install git python -y
pip install requests phonenumbers

# Clone repository
git clone https://github.com/rupuf/infox.git

# Go to directory
cd infox

# Run installer
bash install.sh

#!/bin/bash
#
# Install RetroFlag SafeShutdown for Retropie on Tinkerboard (ROTT 1.0.7)
# 

SCRIPT=$(readlink -f $0);
dir_base=`dirname $SCRIPT`;

#Step 1) Check if root--------------------------------------
#if [[ $EUID -ne 0 ]]; then
#   echo "Please execute script as root o sudo." 
#   exit 1
#fi
#-----------------------------------------------------------

#Step 2) Update repository----------------------------------
#sudo apt-get update -y
#-----------------------------------------------------------

#Step 3) Install gpio python----------------------------
sudo apt-get install python-dev git
cd $HOME
git clone http://github.com/TinkerBoard/gpio_lib_python --depth 1 GPIO_API_for_Python
cd GPIO_API_for_Python/
sudo python setup.py install
#-----------------------------------------------------------

#Step 4) Copy Python script-----------------------------
sudo mkdir -p /opt/RetroFlag
script=SafeShutdownTinker.py

if [ -e /opt/RetroFlag/$script ];
	then
		echo "Script SafeShutdownTinker.py already exists. Overwriting file now!"
		echo "Copying ..."
	else
		echo "Script will be installed now! Copying ..."
fi

cd $dir_base

sudo cp SafeShutdownTinker.py /opt/RetroFlag
sudo cp ShutdownTinker.py /opt/RetroFlag
sudo cp multi_switch.sh /opt/RetroFlag

cd /opt/RetroFlag
sudo chmod +x SafeShutdownTinker.py
sudo chmod +x ShutdownTinker.py
sudo chmod +x multi_switch.sh
#-----------------------------------------------------------

#Step 5) Enable Python script to run on start up------------
cd /etc/
RC=rc.local

if grep -q "sudo python \/opt\/RetroFlag\/SafeShutdownTinker.py \&" "$RC";
	then
		echo "File /etc/rc.local already configured. Doing nothing."
	else
		sed -i -e "s/^exit 0/sudo python \/opt\/RetroFlag\/SafeShutdownTinker.py \&\n&/g" "$RC"
		echo "File /etc/rc.local configured."
fi
#-----------------------------------------------------------

#Step 6) Reboot to apply changes----------------------------
echo "RetroFlag Pi Case installation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------
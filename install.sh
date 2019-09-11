#!/bin/bash
if [ "$(id -u)" != "0" ]; then
	echo "Please re-run as sudo."
	exit 1
fi

echo "Automated Installer Program For I2C LCD Screens"
echo ""
echo "Installer by Ryanteck LTD. Cloned and tweaked by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube tutorial"
echo "Further tweaked by pfidr34 for pihole stats"
echo ""
echo "Updating APT & Installing python-smbus and python-requests, if password is asked by sudo please enter it"
echo ""
apt-get update
apt-get install python-smbus python-requests -y
echo "Should now be installed, now checking revision"
echo ""
revision=`python -c "import RPi.GPIO as GPIO; print GPIO.RPI_REVISION"`

if [ $revision = "1" ]
then
echo "I2C Pins detected as 0"
echo ""
cp installConfigs/i2c_lib_0.py ./i2c_lib.py
else
echo "I2C Pins detected as 1"
echo ""
cp installConfigs/i2c_lib_1.py ./i2c_lib.py
fi
echo "I2C Library setup for this revision of Raspberry Pi, if you change revision a modification will be required to i2c_lib.py"
echo ""
echo "Now overwriting modules & blacklist. This will enable I2C pins"
echo ""
cp installConfigs/modules /etc/
cp installConfigs/raspi-blacklist.conf /etc/modprobe.d/
printf "dtparam=i2c_arm=1\n" >> /boot/config.txt

echo "Install is complete. Please press any key to now reboot."
echo ""
echo ""
echo ""

read -n1 -s
sudo reboot

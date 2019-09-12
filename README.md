# LCD for Pihole Stats

The following has been tested on a Raspberry Pi 3B+ running Raspian Buster Lite

Screen used: https://www.amazon.com/gp/product/B07CXHC32T
Dupont wire used: https://www.amazon.com/gp/product/B01EV70C78

## Setup the Pi

1.) Change to the opt directory ```cd /opt``` <br>
2.) Clone the needed files into the direcotry ```sudo git clone https://github.com/pfidr34/lcd.git``` <br>
3.) Change to the opt directory ```cd /opt/lcd``` <br>
4.) Run the installation script ```sudo bash install.sh``` <br>

![GPIO](https://github.com/pfidr34/lcd/blob/master/images/piGPIO.jpg?raw=true)

## Wire the LCD

1.) Unplug the Pi
2.) GND on the LCD to pin 6 on the Pi GPIO
3.) VCC on the LCD to pin 2 on the Pi GPIO
4.) SDA on the LCD to pin 3 on the Pi GPIO
5.) SCL on the LCD to pin 5 on the Pi GPIO

## Install as a service

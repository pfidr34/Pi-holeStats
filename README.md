# Pihole Stats

The following has been tested on a Raspberry Pi 3B+ running Raspian Buster Lite

Screen used: https://www.amazon.com/gp/product/B07CXHC32T <br>
Dupont wire used: https://www.amazon.com/gp/product/B01EV70C78

## Setup the Pi

1.) Change to the opt directory ```cd /opt``` <br>
2.) Clone the needed files into the direcotry ```sudo git clone https://github.com/pfidr34/Pi-holeStats.git``` <br>
3.) Change to the opt directory ```cd /opt/Pi-holeStats``` <br>
4.) Run the installation script ```sudo bash install.sh``` <br>

![LCD](https://github.com/pfidr34/Pi-holeStats/blob/master/images/i2cLCD.jpg?raw=true)
![GPIO](https://github.com/pfidr34/Pi-holeStats/blob/master/images/pi3b+GPIO.jpg?raw=true)

## Wire the LCD

1.) Unplug the Pi <br>
2.) GND on the LCD to pin 6 on the Pi GPIO <br>
3.) VCC on the LCD to pin 2 on the Pi GPIO <br>
4.) SDA on the LCD to pin 3 on the Pi GPIO <br>
5.) SCL on the LCD to pin 5 on the Pi GPIO <br>

## Install as a service
1.) Change to the systemd directory ```cd /lib/systemd/system/``` <br>
2.) Start a new file for the service ```sudo nano pistat.service``` <br>
3.) Paste the following into nano <br>
```
[Unit]
Description=Pi Stats LCD
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /opt/Pi-holeStats/pistat.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
``` 
4.) Set permissions on the script ```sudo chmod 644 /lib/systemd/system/pistat.service``` <br>
5.) Make the script executable ```chmod +x /opt/Pi-holeStats/pistat.py``` <br>
6.) Reload daemon so our service is seen ```sudo systemctl daemon-reload``` <br>
7.) Enable the service to run on boot ```sudo systemctl enable pistat.service``` <br>
8.) Set permissions on the script ```sudo systemctl start pistat.service``` <br>
<br>
<br>
<br>
Project based off of: <br>
https://github.com/the-raspberry-pi-guy/lcd <br>
and <br>
https://www.reddit.com/r/pihole/comments/d1ilob/my_cheap_pihole_monitor_on_16x2_lcd_1/

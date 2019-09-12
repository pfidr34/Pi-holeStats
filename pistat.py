# Original script by: www.reddit.com/u/SakamotoDesu
# Modified sript by: www.github.com/pfidr34

# Import modules
import os
import lcddriver
import time
import socket
import requests

# Define page display time
waitTime = 5

# Set LCD display varaible
display = lcddriver.lcd()

# Get local pi IP address
# (Requires internet connection)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]

# Function to get uptime
def uptime():

     # Add try/catch block
     try:
         # Get uptime
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     # Handle exceptions
     except:
        return "NaN"

     # Get seconds from uptime
     total_seconds = float(contents[0])

     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24

     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )

     # Build the string
     string = ""
     if days > 0:
         string += str(days) +  "D "
     if len(string) > 0 or hours > 0:
         string += str(hours) + "H "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + "M"

     # Return the uptime
     return string;

# Add try/catch block
try:
        # Loop forever
        while True:

                # Get Pihole data
                pihole = requests.get("http://127.0.0.1/admin/api.php?summaryRaw").json()

                # PAGE 1
                display.lcd_display_string("Pihole " + str(pihole['status']).upper(),1)
                if len(localIP) >= 14:
                        display.lcd_display_string(localIP,2)
                else:
                        display.lcd_display_string("IP " + localIP,2)
                time.sleep(waitTime)

                # PAGE 2
                display.lcd_display_string("Blocked " + str(pihole['ads_blocked_today']),1)
                display.lcd_display_string("Blocked " + str(pihole['ads_percentage_today'])[:4] + "%",2)
                time.sleep(waitTime)

                # PAGE 3
                display.lcd_display_string("List " + str(pihole['domains_being_blocked']),1)
                display.lcd_display_string("Queries " + str(pihole['dns_queries_today']),2)
                time.sleep(waitTime)

                # PAGE 4
                if len(str(pihole['gravity_last_updated']['relative']['days'])) < 4:
                        display.lcd_display_string("Gravity " + str(pihole['gravity_last_updated']['relative']['days']) + "D " + str(pihole['gravity_last_updated']['relative']['hours']) + "H",1)
                else:
                        display.lcd_display_string("Gravity " + str(pihole['gravity_last_updated']['relative']['days']) + "D",1)
                display.lcd_display_string("Up " + uptime(),2)
                time.sleep(waitTime)

# Handle exceptions
except Exception, e:
        print("Error : " + str(e))
        display.lcd_clear()

import os
import json
import time

# check network...
if '192' not in os.popen('ifconfig | grep 192').read():
  os.system('sudo /etc/init.d/networking restart')
  time.sleep(30)
# otherwise first run will fail to open file.
file = open("/home/pi/ip.txt",'a')
file.close()

# get the public ip from chinaz.
os.system("wget ip.chinaz.com/getip.aspx -O ip.txt.temp")
file = open("/home/pi/ip.txt.temp",'r')
ip = file.read().split("'")[1]
file.close()
file = open("/home/pi/ip.txt",'r')

# check if IP changed.
# if changed, do nothing.
if  ip==file.read():
  print  "equal"
  file.close()
else:
# else, save IP and send E-mail.
  file.close()
  file = open("/home/pi/ip.txt",'w')
  file.write(ip)
  file.close()
  os.system("cat mail.txt ip.txt | msmtp -a default foo@example.com")



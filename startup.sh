#!/bin/sh
sleep 10
sudo modprobe w1-gpio
sudo modprobe w1-therm
# sudo /home/pi/optimized-SMS-pi/adb forward tcp:50001 tcp:50001
sleep 3
logger "one to client"
sudo python /home/pi/optimized-SMS-pi/client.py &
sleep 1
logger "one to temp server"
sudo python /home/pi/optimized-SMS-pi/optimized-SMS-pi.py -p54320 &


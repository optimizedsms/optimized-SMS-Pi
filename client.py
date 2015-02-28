# client.py
#  Setups the client required to connect the Pi to the SMS gateway on 
#  android.  Uses sockets or sockets and adb.
#  
#  Copyright (C) 2015, Chaski Telecommunications.  
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#

import time
import errno
import os
import sys
import socket
import getremote

TCP_IP = '127.0.0.1'
REMOTE_IP = '127.0.0.1'
TCP_PORT = 50001
COAP_PORT = 54320
BUFFER_SIZE = 1024

data=bytearray(BUFFER_SIZE)
data2=bytearray(BUFFER_SIZE)

def init():
  print "preconnect"
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.connect((TCP_IP, TCP_PORT))
  except:
    REMOTE_IP = getremote.getRemoteIp()
    try:
          print "Trying to connect to:",REMOTE_IP
          s.connect((REMOTE_IP, TCP_PORT))
    except:
          print "No connection"
          print "Trying to launch adb"
          os.system("/home/pi/optimized-SMS-Pi/adb forward tcp:50001 tcp:50001")
          REMOTE_IP = '127.0.0.1'
          print "Trying to connect via adb:", REMOTE_IP
          try:
             s.connect((REMOTE_IP, TCP_PORT))
          except:
             print "NO ADB Connection"
    
  print "Connect 1 done"

  s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  addr = ("localhost", COAP_PORT)
  print "Connect 2 done"

  s2.setblocking(0)
  s.setblocking(0)
  return s, s2 ,addr


total=len(sys.argv)
cmdargs = str(sys.argv)

if total == 2:
   TCP_IP=sys.argv[1]
print "starting client.py version 0.1"
print "connecting target to ", TCP_IP

# data = s.recv(BUFFER_SIZE)
# s.close()
count = 310 
# start with a full count
while True:
    if count >= 310: 
       s,s2,addr=init()
       print "Attempting connection reset"
       count = 0 

    #do some serial sending here
    time.sleep(0.1)
    count=count+1

    try:
      retval = s.recv_into(data,0)
    except socket.error, e:
      retval = 0;
      # print "socket2 error", os.strerror(e.errno)
      # s.close()
      # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # s.connect((TCP_IP, TCP_PORT))
      # s.setblocking(0)
    # print "size ",retval
    if retval > 0:
       count=0
       print "retval size",retval
       data3=bytearray(retval)
       data3 = data[0:retval]
       s2.sendto(data3,addr);
       print "received data 1:", data

    data=bytearray(BUFFER_SIZE)

    try:
      retval = s2.recv_into(data2,0)
    except socket.error, e:
      retval = 0;
      # print "socket2 error", os.strerror(e.errno)

    if retval > 0:
       print "a-retval size",retval
       data3=bytearray(retval)
       data3 = data2[0:retval]
       s.sendto(data3,addr);
       print "received data 2:", data3

    data2=bytearray(BUFFER_SIZE)


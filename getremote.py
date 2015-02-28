# header.py
#
#  Scans for connected android device.
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

import socket


def getRemoteIp():
 BROADCAST_PORT = 50004
 RX_PORT = 50005
 MESSAGE = "Hello, World!"

 print "UDP broadcast target port:",BROADCAST_PORT 
 print "message:", MESSAGE

 try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  sock.bind(('', 0))
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  sock.sendto(MESSAGE, ('<broadcast>', BROADCAST_PORT))
 except:
   return "127.0.0.1" 
  

 try:
    sock2 = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
 except:
    return "127.0.0.1" 

 # sock2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
 sock2.bind(('', RX_PORT))
 sock2.settimeout(10)

 print "getremote.py version 0.1"

 while True:
    try:
     data, addr = sock2.recvfrom(1024) # buffer size is 1024 bytes
     print "received message:", data
     print "received addr:", addr
     return data
     
    except:
     sock2.close()
     sock.close()
     return "127.0.0.1"

ip = getRemoteIp() 
print ip


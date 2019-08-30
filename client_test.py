import socket
from constant_client import *
import thread
import time

def recv_data(client):
    while 1:
        data, addr = client.recvfrom(10*1024)
        print "%s: %s" % (addr, data)
        if DEBUG:
            client.sendto("ACK"+data, addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# host = socket.gethostname() # hostname or IP addr

s.bind((host, port))

# start recv data
thread.start_new_thread(recv_data, (s,))

try:
    while 1:
        msg = raw_input()
        s.sendto(str(msg), (dest_host, dest_port))
        
except:
    pass

s.close()

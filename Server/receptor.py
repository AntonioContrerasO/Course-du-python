#Atzel Herrera
import time
from socket import socket,AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
while(True):
    s.sendto(b"receptor:1", ("189.223.71.122", 443))
    print(s.recv(8192))
    time.sleep(0.5)









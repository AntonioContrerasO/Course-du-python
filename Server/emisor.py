#Steven Cole
from socket import socket,AF_INET, SOCK_DGRAM

s = socket(AF_INET,SOCK_DGRAM) # crea el socket

s.connect(("172.16.13.224",3000));

import time 
import socket
import sys
import os

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((port))
s.listen()
conn, addr = s.accept()
print (addr, "Has connected to the server")
command = input(str("Please enter a command: "))
conn.send(command.encode())
print("Command has been sent successfully")
data = conn.recv(1024)
if data:
    print("command received and executed successfully")

import socket
import sys

s = socket.socket()
host = input(str("Host adini daxil et : "))
port = 8080
s.connect((host,port))
name = input(str("Nickini yaz : "))
print(" Chata qosuldu")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print(s_name, "chata qosuldu ")

while 1:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":" ,message)
    print("")
    message = input(str("Mesajini daxil et: "))
    message = message.encode()
    s.send(message)
    print("Gonderildi")
    print("")

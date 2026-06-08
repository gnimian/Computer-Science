#server-receive tcp
import socket

#a sda cocket is a pipe that connects to a port
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Address Family_ Internet TCP
host = 'localhost' #or 0.0.0.0
port = 3339
s.bind((host, port))
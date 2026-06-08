from fltk import *
import socket
import sys

class Network:
    def __init__(self, user, host, port):
        self.conn = 0
        self.addr = None
    
        self.user = user
        self.host = host
        self.port = port

        self.opponent_finished = False
        self.opponent_ships = None
        self.opponent_attack = None

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #If server, bind and listen
        if self.user == "server":
            self.s.bind((host, port))
            self.s.listen()
            Fl.add_fd(self.s.fileno(), self.acceptconn)
    
        #If client, connect to server
        elif self.user == "client":
            try:
                self.s.connect( (self.host,self.port) ) #client connects to server
                Fl.add_fd(self.s.fileno(), self.receive_finish)
            except:
                print("Server needs to start first")
                self.s.close()
                sys.exit(1)
    
#-----------------------------------------------------------------------------------------
    
    def acceptconn(self, wid):
        if self.conn == 0: #only allow one client to connect
            self.conn, self.addr = self.s.accept()
            Fl.add_fd(self.conn.fileno(), self.receive_finish)

#-----------------------------------------------------------------------------------------
    def receive_finish(self, wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                Fl.remove_fd(self.conn.fileno())
                return
        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                Fl.remove_fd(self.s.fileno())
                return
            
        if data.decode() == "finished":
            #switch now to waiting for opponent to send ships
            if self.user == "server":
                Fl.remove_fd(self.conn.fileno())
                Fl.add_fd(self.conn.fileno(), self.receive_ships)
            elif self.user == "client":
                Fl.remove_fd(self.s.fileno())
                Fl.add_fd(self.s.fileno(), self.receive_ships)
            self.opponent_finished = True
#-----------------------------------------------------------------------------------------
    def send_finish(self):
        text = 'finished'
        if self.user == "server":
            try:
                self.conn.sendall(text.encode())
            except:
                print("Client has not yet connected, or has disconnected")
        elif self.user == "client":
            try:
                self.s.sendall(text.encode())
            except:
                print('Server may have disconnected')
                self.s.close()
#-----------------------------------------------------------------------------------------
    def receive_ships(self, wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                Fl.remove_fd(self.conn.fileno())
                return

        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                Fl.remove_fd(self.s.fileno())
                return
        
        #Turns string of ships back into list of tuples
        ships = data.decode().split(';')

        if self.user == "server":
            ship_list = []
            for i in ships:
                coords = i.split(',')
                if len(coords) == 2:
                    ship_list.append((int(coords[0]), int(coords[1])))
            self.opponent_ships = ship_list
            Fl.remove_fd(self.conn.fileno())
            Fl.add_fd(self.conn.fileno(), self.receive_attack)
        
        if self.user == "client":
            ship_list = []
            for i in ships:
                coords = i.split(',')
                if len(coords) == 2:
                    ship_list.append((int(coords[0]), int(coords[1]))) 
            self.opponent_ships = ship_list
            Fl.remove_fd(self.s.fileno())
            Fl.add_fd(self.s.fileno(), self.receive_attack)

#-----------------------------------------------------------------------------------------
    def send_ships(self, ships):
        #get ship placement from get_placement in BattleShip class in a string and send to other player
        if self.user == "server":
            try:
                self.conn.sendall(ships.encode())
            except:
                print("Client has not yet connected, or has disconnected")
        elif self.user == "client":
            try:
                self.s.sendall(ships.encode())
            except:
                print('Server may have disconnected')
                self.s.close()
#-----------------------------------------------------------------------------------------
    
    def close(self):
        if self.user== "server" and self.conn != 0:
            self.conn.close()
        self.s.close() #close socket s for both client and server

#-----------------------------------------------------------------------------------------
    
    def send_attack(self, status, x , y):
        # h for hit, m for miss
        sends = f'{status},{x},{y}'
        if self.user == "server":
            try:
                self.conn.sendall(sends.encode())
            except:
                print("Client has not yet connected, or has disconnected")
        elif self.user == "client":
            try:
                self.s.sendall(sends.encode())
            except:
                print('Server may have disconnected')
                self.s.close()

#-----------------------------------------------------------------------------------------
    
    def receive_attack(self,wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                Fl.remove_fd(self.conn.fileno())
                return

        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                Fl.remove_fd(self.s.fileno())
                return
        
        #Turns string of ships back into list of tuples
        self.opponent_attack = data.decode()

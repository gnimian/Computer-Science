#Started on May 19, 2026
#Finished on June 3, 2026
#DEBUGGING
#Battleship game server and client
#python3 battleShip.py server localhost 4444
#python3 battleShip.py client localhost 4444
#OOP version

from fltk import *
import socket
import sys
import os
from PIL import Image
import io

#=========================================================================================
#                                     BATTLESHIP CLASS                                 
#=========================================================================================
class BattleShip(Fl_Window):
    def __init__(self, w = 1150, h = 650):
        Fl_Window.__init__(self, w, h,sys.argv[1])

        #CHECKS VALIDITY
        try:
            self.user = sys.argv[1]
            self.host = sys.argv[2]
            self.port = int(sys.argv[3])
        except:
            print("python3 battleShip.py [server/client] [host] [port]")
            sys.exit(1)
        if self.user != "server" and self.user != "client":
            print("python3 battleShip.py [server/client] [host] [port]")
            sys.exit(1)
        #If there is no sudo privileges in Linux, port range should be from 1024 to 65535
        if self.port < 1024 or self.port > 65535:
            print("python3 battleShip.py [server/client] [host] [port]")
            sys.exit(1)
        #checks if length of argument is correct
        if len(sys.argv) != 4:
            print("python3 battleShip.py [server/client] [host] [port]")
            sys.exit(1)

        #VARIABLE DECLARATIONS
        self.net = Network(self.user, self.host, self.port ) #create a network object
        self.my_ships = [] #store ship coor as list of tuples in (x,y) format
        self.enemy_ships = [] #store ship coor as list of tuples in (x,y) format
        self.shots_taken = [] #stores coor of shots taken formatted (x,y)
        self.me_finished = False 
        self.countShip = 1
        self.hit_count = 0 
        self.damage_count = 0
        self.game_over = False
        self.dis_count_start = False
        self.dis_count = 5 #5 seconds to wait before closing


        if self.user == "server":
            self.my_turn = True
        else:
            self.my_turn = False

        self.begin()

        self.ship_i = self.image_resize("ship.png", 100)
        self.blank_i = self.image_resize("blank.png",100)
        self.hit_i = self.image_resize("hit.png",100)
        self.miss_i = self.image_resize("miss.png",100)


        #LEFT GRID
        self.left_but = []
        for i in range(5):
            temp_left = []
            for j in range(5):
                but_l = Fl_Button(50 + i*100, 100 + j*100, 100, 100)
                but_l.image(self.blank_i)
                but_l.callback(self.left_but_cb, (i, j))
                temp_left.append(but_l)
            self.left_but.append(temp_left)
        self.right_but = []
    
        #RIGHT GRID
        for i in range(5):
            temp_right = []
            for j in range(5):
                but_r = Fl_Button(600 + i*100, 100 + j*100, 100, 100)
                but_r.image(self.blank_i)
                but_r.callback(self.right_but_cb, (i,j))
                temp_right.append(but_r)
            self.right_but.append(temp_right)
        
        Fl.visible_focus(0)

        #Text box to show message for connection, turn, hit or miss, win or lose 
        self.text = Fl_Box(50, 20, 1100, 50, "Welcome to Battleship! Please wait until both players are connected")
        self.text.labelcolor(FL_WHITE)
        self.text.labelsize(30)
        self.text.labelfont(FL_HELVETICA_BOLD)
        self.color(FL_BLACK)

        if self.net.connected:
            #tell user to start placing ships
            self.text.label("Place your ships by clicking on the left grid. You can place up to 5 ships.")
        else:
            Fl.add_timeout(0.1, self.check_connection)

        #Make error box on the bottom in smaller text
        self.error_box = Fl_Box(50, 600, 1100, 50, "")
        self.error_box.labelcolor(FL_WHITE)
        self.error_box.labelsize(20)
        self.error_box.labelfont(FL_HELVETICA_BOLD)   

        self.end()
        self.callback(self.close)

#===================================CHECK CONNECTION=========================================
    def check_connection(self):
        if self.net.disconnected and not self.dis_count_start:
            self.dis_count_start = True
            self.game_over = True
            Fl.remove_timeout(self.clear_error)
            Fl.add_timeout(0, self.dis_countdown)
        else:
            Fl.repeat_timeout(0.1, self.check_connection)

#===================================CLOSE WINDOW AFTER DIS========================================
    def dis_countdown(self):
        if self.dis_count > 0:
            self.dis_count -= 1
            self.error_box.label(f"Opponent has disconnected. Closing in {self.dis_count} seconds...")
            Fl.add_timeout(1, self.dis_countdown)
        else:
            self.close()
#===================================IMAGE RESIZE========================================= 
    def image_resize(self,fname,width):
        '''resizes any image type using high quality PIL library'''
        img = Image.open(fname) #opens all image formats supported by PIL
        w,h = img.size
        height = int(width*h/w)  #correct aspect ratio
        img = img.resize((width, height), Image.BICUBIC) #high quality resizing
        mem = io.BytesIO()  #byte stream memory object
        img.save(mem, format="PNG") #converts image type to PNG byte stream
        siz = mem.tell() #gets size of image in bytes without reading again
        return Fl_PNG_Image(None, mem.getbuffer(), siz)
#====================================ERROR MESSAGES=======================================
    def clear_error(self):
        self.error_box.label("")

    def show_error(self, message):
        Fl.remove_timeout(self.clear_error)
        self.error_box.label(message)
        Fl.add_timeout(2, self.clear_error)

#===================================LEFT_BUT_CB===========================================
    def left_but_cb(self,wid,data):
        if not self.net.connected:
            self.show_error("Not connected to opponent yet")
            return
            

        if self.countShip <= 5:
            i, j = data
            if (i, j) in self.my_ships:
                self.show_error("Already placed a ship here")
                return
            self.my_ships.append((i, j))
            wid.image(self.ship_i)
            if self.countShip == 5:
                self.text.label("Waiting for opponent to finish placing ships...")
                self.me_finished = True
                self.net.send_finish()
                Fl.add_timeout(0.1, self.verify_finish)
            self.countShip += 1
        else:
            self.show_error("Already placed 5 ships")
#===================================RIGHT_BUT_CB==========================================
    def right_but_cb(self,wid,data):
        if self.game_over:
            self.show_error("Game Over")
            return
        
        if self.enemy_ships == []:
            #wait for opponent to send ships, error label shows you you have to wait
            self.show_error("Waiting for opponent to finish placing ships")
            return

        if self.my_turn:
            i, j = data
            self.my_turn = False
            if (i, j) in self.shots_taken:
                self.show_error("Already attacked here, choose again")
                self.my_turn = True
                return
            else:
                self.shots_taken.append((i, j))
            if (i, j) in self.enemy_ships:
                self.text.label("Hit! It's now your opponent's turn")
                wid.image(self.hit_i)
                self.net.send_attack("h",i,j)
                self.hit_count += 1
                if self.hit_count == 5:
                    #you win message
                    self.text.label("All opponent's ships have been sunk.")
                    fl_message("You win!")
                    self.game_over = True
                    return

            else:
                self.text.label("Miss! It's now your opponent's turn")
                wid.image(self.miss_i)
                self.net.send_attack("m",i,j)

            if self.net.opponent_attack is None:
                Fl.add_timeout(0.1, self.verify_attack)
        else:
            self.show_error("It's not your turn")
#=====================================VERIFY_ATTACK=======================================
    def verify_attack(self):
        if self.game_over:
            self.my_turn = False
            return
        if self.net.opponent_attack is not None:
            att = self.net.opponent_attack.split(',')
            if att[0] == 'h':
                self.text.label("You got hit! It's now your turn")
                #add to damage count
                self.damage_count += 1
                self.left_but[int(att[1])][int(att[2])].image(self.hit_i)
                self.left_but[int(att[1])][int(att[2])].redraw()
            else:
                self.text.label("Your opponent missed! It's now your turn")
                self.left_but[int(att[1])][int(att[2])].image(self.miss_i)
                self.left_but[int(att[1])][int(att[2])].redraw()
            self.my_turn = True
            self.net.opponent_attack = None

            if self.damage_count == 5:
                self.game_over = True
                self.text.label("All your ships have been sunk.")
                fl_message("You lost!")
                return
        else:
            Fl.repeat_timeout(0.1, self.verify_attack)
#==============================VERIFY_FINISH==============================================
    def verify_finish(self):
        #determine if server and client are both finished with placing ships
        if self.net.opponent_finished:
            self.text.label("Both finished placing. Server starts attacking")
            self.net.send_ships(self.get_placement())
            Fl.add_timeout(0.1, self.verify_ships)
        else:
            Fl.repeat_timeout(0.1, self.verify_finish)
#====================================VERIFY SHIPS=========================================
    def verify_ships(self):
        if self.net.opponent_ships is not None:
            self.enemy_ships = self.net.opponent_ships
            if self.my_turn:
                self.text.label("Game started. Your turn.")
            else:
                self.text.label("Game started. Waiting for opponent's attack.")
                Fl.add_timeout(0.1, self.verify_attack)

        else:
            Fl.repeat_timeout(0.1, self.verify_ships)
#===================================GET_PLACEMENT=========================================
    #for Server and Client class to get placement of ships
    def get_placement(self):
        temp = ''
        for ship in self.my_ships:
            #turns coordinates into string to send to client
            asdf = f"{ship[0]},{ship[1]};"
            temp += asdf
        return temp
#==================================CLOSE==================================================
    def close(self, wid):
        self.net.close()
        self.hide()

#=========================================================================================
#                                     NETWORK CLASS                                 
#=========================================================================================
class Network:
#=====================================INITIALIZER=========================================
    def __init__(self, user, host, port):
        self.conn = 0
        self.addr = None
    
        self.user = user
        self.host = host
        self.port = port

        self.connected = False
        #checks if opponent has disconnected 
        self.disconnected = False

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
                self.connected = True
                Fl.add_fd(self.s.fileno(), self.receive_finish)
            except:
                print("Server needs to start first")
                self.s.close()
                sys.exit(1)
#==================================CLOSE AFTER DISCONNECT=====================================
    def close_disconnect(self):
        if self.disconnected:
            return
        self.disconnected = True
        self.connected = False
        try:
            if self.user == "server" and self.conn != 0:
                Fl.remove_fd(self.conn.fileno())
            elif self.user == "client":
                Fl.remove_fd(self.s.fileno())
        except:
            pass
        
#==================================ACCEPT CONNECTION=====================================
    def acceptconn(self, wid):
        if self.conn == 0: #only allow one client to connect
            self.conn, self.addr = self.s.accept()
            self.connected = True
            Fl.add_fd(self.conn.fileno(), self.receive_finish)

#===================================FINISH SEND & RECV====================================
    def receive_finish(self, wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                print("Opponent has disconnected")
                self.close_disconnect()
                return
        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                print("Opponent has disconnected")
                self.close_disconnect()
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

    def send_finish(self):
        text = 'finished'
        if self.user == "server":
            try:
                self.conn.sendall(text.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()


        elif self.user == "client":
            try:
                self.s.sendall(text.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()
    
#==================================SHIPS SEND & RECV======================================
    def receive_ships(self, wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                print("Opponent has disconnected")
                self.close_disconnect()
                return

        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                print("Opponent has disconnected")
                self.close_disconnect()
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

    def send_ships(self, ships):
        #get ship placement from get_placement in BattleShip class in a string and send to other player
        if self.user == "server":
            try:
                self.conn.sendall(ships.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()
        elif self.user == "client":
            try:
                self.s.sendall(ships.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()

#=====================================ATTACK SEND & RECV==================================
    def send_attack(self, status, x , y):
        # h for hit, m for miss
        sends = f'{status},{x},{y}'
        if self.user == "server":
            try:
                self.conn.sendall(sends.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()
        elif self.user == "client":
            try:
                self.s.sendall(sends.encode())
            except:
                print("Opponent disconnected")
                self.mark_disconnected()
                self.s.close()

    def receive_attack(self,wid):
        if self.user == "server":
            data=self.conn.recv(1024) #server communicates through socket conn
            #data is null byte b'' when socket is closed
            if data == b'':
                print("Opponent has disconnected")
                self.close_disconnect()
                return

        elif self.user == "client":
            data=self.s.recv(1024)    #client communicates through socket s
            if not data: #same as if data == b''
                print("Opponent has disconnected")
                self.close_disconnect()
                return
        
        #Turns string of ships back into list of tuples
        self.opponent_attack = data.decode()

#===============================CLOSE CONNECTIONS & SOCKETS===============================
    def close(self):
        if self.user== "server" and self.conn != 0:
            self.conn.close()
        self.s.close() #close socket s for both client and server

#=========================================================================================
#                                        MAIN FUNCTION
#=========================================================================================
if __name__ == '__main__':
    Fl.visible_focus(0)
    app = BattleShip()
    app.show()
    Fl.run()
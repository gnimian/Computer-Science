#project completion date: november 1, 2024
#3rd project in cs2? i think? this is meant to be a project? it took me like 2 hours in total tho
#make sure to have the sound effects "yellow.mp3", "red.mp3", "blue.mp3", "green.mp3" and "error.mp3" in the same folder as the code
#the above audio can be found in the "files" folder in this repository under "simon_says"
#this is basically the 4 colour memory game thing

from fltk import *
import random
import subprocess as sp

class simonsays(Fl_Window):
	L = [] #list of buttons that are flashing
	L_clicked = [] #list of buttons that the user clicked this turn
	def __init__(self, x=300,y=200,w=400,h=450,title="Simon Says"):
		Fl_Window.__init__(self, x,y,w,h,title)
		self.yellowb = Fl_Button(0, 50, 200, 200)
		self.redb = Fl_Button(200, 50, 200, 200)
		self.blueb = Fl_Button(0, 250, 200, 200)
		self.greenb = Fl_Button(200, 250, 200, 200)
		self.button = Fl_Button(0, 0, 400, 50, "Start")
		self.buttons = [self.yellowb, self.redb, self.blueb, self.greenb]
		self.yellowb.color(fl_rgb_color(252, 255, 134), FL_WHITE)
		self.redb.color(fl_rgb_color(255, 134, 152), FL_WHITE)
		self.blueb.color(fl_rgb_color(134, 189, 225), FL_WHITE)
		self.greenb.color(fl_rgb_color(157, 255, 138), FL_WHITE)
		self.button.color(FL_WHITE, FL_WHITE)
		self.button.labelsize(18)
		self.button.labelfont(FL_TIMES_BOLD)
		for x in self.buttons: #deactivate the 4 colour buttons at the beginning
			x.deactivate()
		self.button.callback(self.level)
		self.yellowb.callback(self.play, "yellow")
		self.redb.callback(self.play, "red")
		self.blueb.callback(self.play, "blue")
		self.greenb.callback(self.play, "green")
	
	def anticheating(self): #makes buttons only handle events if nothing is currently flashing
		for x in self.buttons:
			x.when(FL_WHEN_RELEASE)
		self.button.label("LEVEL " + str(len(self.L)) + ". YOUR TURN!") 
	
	def level(self, wid):
		#print(self.L) <-- if you uncomment this you can print the colours. this is useful for testing.
		self.button.when(0) #disable top button for remainder of game without graying it out
		for x in self.buttons:
			x.activate()
			x.when(0) #disables buttons until nothing is flashing anymore
		self.L.append(random.randrange(0, 4))
		if len(self.L)%10 == 0 and len(self.L) != 0: #milestone celebration every 10 levels! 
			self.button.label("YOU MADE IT TO LEVEL " + str(len(self.L)) + "! CONGRATS!")
		else:
			self.button.label("LEVEL " + str(len(self.L)))
		Fl.add_timeout(len(self.L)+0.5, self.anticheating)
		for x in range(len(self.L)):
			Fl.add_timeout(x+1, self.flashing, self.L[x])
	
	def flashing(self, x):
		if self.buttons[x].color() != FL_WHITE:
			self.buttons[x].color(FL_WHITE)
			if x == 0:
				sp.Popen(['mpv', '-no-terminal',"yellow.mp3"]) #sound effects. make sure to have these files in the same folder
			elif x == 1:
				sp.Popen(['mpv', '-no-terminal',"red.mp3"])
			elif x == 2:
				sp.Popen(['mpv', '-no-terminal',"blue.mp3"])
			elif x == 3:
				sp.Popen(['mpv', '-no-terminal',"green.mp3"])
			self.redraw()
			Fl.add_timeout(0.5, self.flashing, x)
		else:
			if x == 0:
				self.buttons[x].color(fl_rgb_color(252, 255, 134))
			elif x == 1:
				self.buttons[x].color(fl_rgb_color(255, 134, 152))
			elif x == 2:
				self.buttons[x].color(fl_rgb_color(134, 189, 225))
			elif x == 3:
				self.buttons[x].color(fl_rgb_color(157, 255, 138))
			self.redraw()
			return
	def play(self, wid, colour):
		if colour == "yellow":
			self.L_clicked.append(0) #yellow is assigned number 0, red is assigned 1, and so on
		elif colour == "red":
			self.L_clicked.append(1)
		elif colour == "blue":
			self.L_clicked.append(2)
		elif colour == "green":
			self.L_clicked.append(3)
		length = len(self.L_clicked)
		if self.L_clicked[length-1] != self.L[length-1]: #check last item in the clicked list. if not the same, you failed.
			sp.Popen(['mpv', '-no-terminal',"error.mp3"])
			fl_message("You lost. Close this message to play again.")
			self.button.label("DIED AT LEVEL " + str(len(self.L)) + ". CLICK TO RESTART.")
			self.L_clicked = []
			self.L = []
			self.button.when(FL_WHEN_RELEASE) #makes top button active so user can play again
			for x in self.buttons:
				x.deactivate()
		if len(self.L) != 0:
			sp.Popen(['mpv', '-no-terminal', colour+".mp3"]) 
		if len(self.L) != 0 and self.L == self.L_clicked: #if true, move on to next level
			self.L_clicked = []
			self.level(wid)

win = simonsays(300, 200, 400, 450, "simon says dupe")

win.show()
Fl.run()


#below is the same code with an unnecessary variable (current_level). in case i ever need this version here it is.
'''from fltk import *
import random
import subprocess as sp

class simonsays(Fl_Window):
	L = [] #list of buttons that are flashing
	L_clicked = [] #list of buttons that the user clicked this turn
	current_level = 0
	def __init__(self, x=300,y=200,w=400,h=450,title="Simon Says"):
		Fl_Window.__init__(self, x,y,w,h,title)
		self.yellowb = Fl_Button(0, 50, 200, 200)
		self.redb = Fl_Button(200, 50, 200, 200)
		self.blueb = Fl_Button(0, 250, 200, 200)
		self.greenb = Fl_Button(200, 250, 200, 200)
		self.button = Fl_Button(0, 0, 400, 50, "Start")
		self.buttons = [self.yellowb, self.redb, self.blueb, self.greenb]
		self.yellowb.color(fl_rgb_color(252, 255, 134), FL_WHITE)
		self.redb.color(fl_rgb_color(255, 134, 152), FL_WHITE)
		self.blueb.color(fl_rgb_color(134, 189, 225), FL_WHITE)
		self.greenb.color(fl_rgb_color(157, 255, 138), FL_WHITE)
		self.button.color(FL_WHITE, FL_WHITE)
		self.button.labelsize(18)
		self.button.labelfont(FL_TIMES_BOLD)
		for x in self.buttons: #deactivate the 4 colour buttons at the beginning
			x.deactivate()
		self.button.callback(self.level)
		self.yellowb.callback(self.play, "yellow")
		self.redb.callback(self.play, "red")
		self.blueb.callback(self.play, "blue")
		self.greenb.callback(self.play, "green")
	
	def anticheating(self): #makes buttons only handle events if nothing is currently flashing
		for x in self.buttons:
			x.when(FL_WHEN_RELEASE)
		self.button.label("LEVEL " + str(self.current_level) + ". YOUR TURN!") 
	
	def level(self, wid):
		#print(self.L) <-- if you uncomment this you can cheat. this is useful for testing.
		self.button.when(0) #disable top button for remainder of game without graying it out
		for x in self.buttons:
			x.activate()
			x.when(0) #disables buttons until nothing is flashing anymore
		self.current_level += 1
		if self.current_level%10 == 0: #milestone celebration every 10 levels! 
			self.button.label("YOU MADE IT TO LEVEL " + str(self.current_level) + "! CONGRATS!")
		else:
			self.button.label("LEVEL " + str(self.current_level))
		self.L.append(random.randrange(0, 4))
		Fl.add_timeout(len(self.L)+0.5, self.anticheating)
		for x in range(len(self.L)):
			Fl.add_timeout(x+1, self.flashing, self.L[x])
	
	def flashing(self, x):
		if self.buttons[x].color() != FL_WHITE:
			self.buttons[x].color(FL_WHITE)
			if x == 0:
				sp.Popen(['mpv', '-no-terminal',"yellow.mp3"]) #sound effects. make sure to have these files in the same folder
			elif x == 1:
				sp.Popen(['mpv', '-no-terminal',"red.mp3"])
			elif x == 2:
				sp.Popen(['mpv', '-no-terminal',"blue.mp3"])
			elif x == 3:
				sp.Popen(['mpv', '-no-terminal',"green.mp3"])
			self.redraw()
			Fl.add_timeout(0.5, self.flashing, x)
		else:
			if x == 0:
				self.buttons[x].color(fl_rgb_color(252, 255, 134))
			elif x == 1:
				self.buttons[x].color(fl_rgb_color(255, 134, 152))
			elif x == 2:
				self.buttons[x].color(fl_rgb_color(134, 189, 225))
			elif x == 3:
				self.buttons[x].color(fl_rgb_color(157, 255, 138))
			self.redraw()
			return
	def play(self, wid, colour):
		if colour == "yellow":
			self.L_clicked.append(0) #yellow is assigned number 0, red is assigned 1, and so on
		elif colour == "red":
			self.L_clicked.append(1)
		elif colour == "blue":
			self.L_clicked.append(2)
		elif colour == "green":
			self.L_clicked.append(3)
		length = len(self.L_clicked)
		if self.L_clicked[length-1] != self.L[length-1]: #check last item in the clicked list. if not the same, you failed.
			sp.Popen(['mpv', '-no-terminal',"error.mp3"])
			self.L_clicked = []
			self.L = []
			self.button.label("DIED AT LEVEL " + str(self.current_level) + ". CLICK TO RESTART.")
			self.current_level = 0
			self.button.when(FL_WHEN_RELEASE) #makes top button active so user can play again
			for x in self.buttons:
				x.deactivate()
		sp.Popen(['mpv', '-no-terminal', colour+".mp3"]) 
		if len(self.L) != 0 and self.L == self.L_clicked: #if true, move on to next level
			self.L_clicked = []
			self.level(wid)

win = simonsays(300, 200, 400, 450, "simon says dupe")

win.show()
Fl.run()'''

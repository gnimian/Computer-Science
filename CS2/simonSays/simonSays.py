#started around 4/6/2026
from fltk import *
import os
import subprocess as sp
import random

#need this class to override the handle method
class simonButton(Fl_Button):
    def __init__(self, x, y, w, h, main):
        Fl_Button.__init__(self ,x , y, w, h)
        self.main = main
    def handle(self, event):
        retval = super().handle(event)
        #resets timer when button is pressed and counts down from 5 seconds
        if event == FL_PUSH:
            Fl.remove_timeout(self.main.time_count)
            self.main.time = 0
            self.main.time_count()
            return 1 #indicates that the event was handled 
        
        #resets timer when button is released and counts down from 5 seconds
        if event == FL_RELEASE:
            Fl.remove_timeout(self.main.time_count)
            self.main.time = 0
            self.main.time_count()
            return 1 
        else:
            return retval #handles other events normally
        
class simonSays(Fl_Window):
    def __init__(self, x = 0, y = 0, w = 500, h =700):
        Fl_Window.__init__(self, x, y, w, h,'Simon Says Game')
        self.begin()

        #declaring variable I need to use 
        self.currentLevel = 1
        self.isPress = False
        self.time = 0
        Fl.remove_timeout(self.time_count)
        self.time = 0
        self.canPress = False
        self.keepCount = []
        self.playerCount = 0
        self.pid = None
        self.highScore = 0

        #dictionaries for the colors and sounds
        self.button_dict = {}
        self.sound_dict = {1: 'green.mp3', 2: 'red.mp3', 3: 'blue.mp3', 4: 'yellow.mp3'}
        self.lightCol_dict = {1: 10, 2: 9, 3: 12, 4: 11}
        self.darkCol_dict = {1: FL_GREEN, 2: FL_RED, 3: FL_BLUE, 4: FL_YELLOW}

        #4 buttons for simon says + start button/reset button
        self.group1 = Fl_Group(0,100,500,500)
        
        current = 1
        for row in range(2):
            for col in range(2):
                #shorter way to make buttons
                btn = simonButton(col*250,row*250+100,250,250,self)
                btn.color(self.lightCol_dict[current])
                btn.selection_color(self.darkCol_dict[current])
                btn.deactivate()
                btn.callback(self.studentPress, current)
                #append button to dictionary
                self.button_dict[current] = btn
                current += 1

        self.group1.end() #end group so I can click the start buttion
        
        #start button config
        self.text_b = Fl_Button(0,0,500,100,"Start")
        self.text_b.color(FL_BLACK)
        self.text_b.labelcolor(FL_WHITE)
        self.text_b.labelfont(FL_HELVETICA_BOLD)
        self.text_b.labelsize(30)
        self.text_b.callback(self.but_cb)

        self.score = Fl_Box(0, 600, 500, 100, "")
        self.score.labelfont(FL_HELVETICA_BOLD)
        self.score.labelsize(24)
        self.score.labelcolor(FL_BLACK)

        self.end()
        self.resizable(self.group1)
    
    def time_count(self):
        if not self.canPress:
            return
        if self.time >= 5:
            sp.Popen(['mpv', '--really-quiet', 'error.mp3']) 
            self.isPress = False
            self.canPress = False
            for i in range(1,5):
                self.button_dict[i].deactivate()
            self.score.label(f'Score: {self.currentLevel-1}')
            self.score.redraw()
            if self.currentLevel - 1 > self.highScore:
                self.highScore = self.currentLevel - 1
            Fl.add_timeout(1,self.high_Score)
            return
        Fl.add_timeout(1,self.time_count)
        self.time += 1
    
    def high_Score(self):
        self.score.label(f'High Score: {self.highScore}')
        self.score.redraw()

    def but_cb(self,wid):
        #kills sound if something is playing
        if self.pid != None:
            self.pid.send_signal(sp.signal.SIGTERM)
        
        #removing all timeouts and starting fresh for new game
        timeouts = [self.but_off, self.but_on, self.backStart, self.time_count]
        for i in range(4):
            Fl.remove_timeout(timeouts[i])

        self.time = 0
        self.currentLevel = 1
        self.canPress = False
        self.keepCount = []
        self.playerCount = 0
        self.getLevel()

        for i in range(1,5):
            self.button_dict[i].activate()
            self.button_dict[i].color(self.lightCol_dict[i])
            self.button_dict[i].value(0)
            self.button_dict[i].redraw()
        
        self.redraw()

    #gets user level
    def getLevel(self):
        self.canPress = False
        self.score.label(f'Current Level: {self.currentLevel}')
        self.score.redraw()
        Fl.add_timeout(1.0,self.backStart)
        
    #turns the button's label back to "start" and also starts sequence
    def backStart(self):
        self.score.label("")
        self.score.redraw()
        self.sequence()

    def sequence(self):
        #showing the player the sequence
        self.keepCount.append(random.randint(1,4))
        
        for i in range (len(self.keepCount)):
            Fl.add_timeout(0.75 * i,self.but_on,self.keepCount[i])
            Fl.add_timeout(i * 0.75 + 0.5,self.but_off,(self.keepCount[i],i))
        
    #when player presses a button
    def studentPress(self,wid,coll):
        #check if they can press or not and play sound if they can
        if self.canPress:
            self.callSound(coll)

        #checks if they pressed the right button
        if self.canPress and coll == self.keepCount[self.playerCount]:
                self.playerCount += 1
            
        elif self.canPress:
                sp.Popen(['mpv', '--really-quiet', 'error.mp3']) 
                self.canPress = False
                for i in range(1,5):
                    self.button_dict[i].deactivate()
                self.score.label(f'Score: {self.currentLevel-1}')
                self.score.redraw()
                return
            
        if self.canPress and self.playerCount == len(self.keepCount):
                self.playerCount = 0
                self.currentLevel += 1
                self.getLevel()

    def callSound(self,colls):
        if colls == 1:
            self.pid = sp.Popen(['mpv', '--really-quiet', 'green.mp3'])
        elif colls == 2:
            self.pid = sp.Popen(['mpv', '--really-quiet', 'red.mp3'])
        elif colls == 3:
            self.pid = sp.Popen(['mpv', '--really-quiet', 'blue.mp3']) 
        else:
            self.pid = sp.Popen(['mpv', '--really-quiet', 'yellow.mp3']) 
            
    def but_off(self,col):
        self.button_dict[col[0]].color(self.lightCol_dict[col[0]])
        self.button_dict[col[0]].redraw()
        
        if col[1] == len(self.keepCount)-1:
            self.time = 0
            self.canPress = True
            self.time_count()


    def but_on(self,col):
        self.callSound(col)
        self.button_dict[col].color(self.darkCol_dict[col])
        self.button_dict[col].redraw()
    

if __name__=='__main__':
    Fl.visible_focus(0)
    app=simonSays()
    app.show()
    Fl.run()
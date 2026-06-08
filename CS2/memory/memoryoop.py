#Converted to OOP
#Memory Game. Enjoy!!!!

from fltk import *
from PIL import Image
import io
import random
#import os

class MemoryGame(Fl_Window):
    def __init__(self,w,h,name):
        Fl_Window.__init__(self,w,h,name)
        
        self.begin()

        self.nameCompare = []
        self.butCompare=[]
        self.count=0
        self.tries = 0
        self.back_image = self.img_resize("marvel.png",200)

        self.fn = ["dococ.png","electro.png","goblin.png","hulk.png","ironman.png","lizard.png","mysterio.png","rhino2.png","sandman.png","spiderman.png","venom.png","wolverine.png"]
        self.fn = self.fn + self.fn
        random.shuffle(self.fn)

        I=[self.img_resize(f, 200) for f in self.fn]

        self.image2D=[]
        for i in range(4):
            self.row = []
            for j in range(6):
                self.row.append(I[i*6+j])
            self.image2D.append(self.row)

        self.name2D=[]
        for i in range(4):
            self.temp = []
            for j in range(6):
                self.temp.append(self.fn[i*6+j])
            self.name2D.append(self.temp)

        self.butMaker=[]
        for row in range(4):
            for column in range(6):
                self.but = Fl_Button(column*200, row*200, 200, 200)
                self.but.image(self.back_image)
                self.butMaker.append(self.but)
                self.butMaker[-1].callback(self.but_cb,(row,column))
        self.end()
        self.show()

    def img_resize(self,fname,height):
        img = Image.open(fname)
        img = img.resize((height, height), Image.BICUBIC)
        mem = io.BytesIO()
        img.save(mem, format="PNG")
        siz = mem.tell()
        return Fl_PNG_Image(None, mem.getbuffer(), siz)

    def but_cb(self,wid,data):
        #global count,nameCompare,butCompare,tries
        self.r,self.c = data
        if len(self.nameCompare) == 2 and self.nameCompare[0] != self.nameCompare[1]:
            if wid == self.butCompare[0] or wid == self.butCompare[1]:
                return
            self.butCompare[0].image(self.back_image)
            self.butCompare[1].image(self.back_image)
            self.butCompare[0].redraw() #MUST NEED
            self.butCompare[1].redraw()
            self.butCompare.clear()
            self.nameCompare.clear()

        if len(self.butCompare)==1 and self.butCompare[0] == wid:
            return

        wid.image(self.image2D[self.r][self.c])
        wid.redraw()
        self.butCompare.append(wid)
        self.nameCompare.append(self.name2D[self.r][self.c])

        #deactivate buttons if match and check if win
        if len(self.nameCompare)==2:
            self.tries+=1
            if self.nameCompare[0]==self.nameCompare[1]:
                self.butCompare[0].deactivate()
                self.butCompare[0].image().inactive()
                wid.deactivate()
                wid.image().inactive()
                self.butCompare.clear()
                self.nameCompare.clear()
                self.count+=1
            if self.count == 12:
                fl_message(f'You win! You got it in {self.tries} tries!')
                self.hide()


if __name__=='__main__':
    game = MemoryGame(1200,800,"Memory Game")
    Fl.run()
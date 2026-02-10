#Project Started 2/9/26
#Memory Game. Enjoy!!!!
from fltk import *
from PIL import Image
import io
import random
#deactive images widget.deactivate()

def img_resize(fname,height):
    img = Image.open(fname)
    w,h = img.size
    width = int(height*w/h)
    img = img.resize((height, width), Image.BICUBIC)
    mem = io.BytesIO()
    img.save(mem, format="PNG")
    siz = mem.tell()
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def but_cb(wid):
    

#resize picture
Images=["dococ.png","electro.png","goblin.png","hulk.png","ironman.png","lizard.png","mysterio.png","rhino2.png","sandman.png","spiderman.png","venom.png","wolverine.png"]
win = Fl_Window(1200,800)
win.begin()
pic = None
#make buttons into grid
LB=[]
row=[]
col=[]
coun=[]
#making a grid with 2D lists
for i in range(4):
    for j in range(6):
        while True:
                a = random.choice(Images)
                pic = img_resize(a, 200)
                if coun.count(a) < 2:
                    coun.append(a)
                    break

for r in range(4):
    for c in range(6): 
        pic = img_resize("marvel.png",200)
        but = Fl_Button(c*200, r*200, 200, 200)
        but.image(pic)
        LB.append(but)
        LB[-1].callback(but_cb)

win.end()

#box.image(pic)
win.resizable(win)

win.show()
Fl.run()


#Project Started 2/9/26
#Memory Game. Enjoy!!!!
from fltk import *
from PIL import Image
import io
import random
import os
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
    print("button callback")

#resize picture
win = Fl_Window(1200,800)
win.begin()
#make buttons into grid
LB=[]
twod=[]
coun=[]

#making list of pictures
fn=os.listdir('marvel_pics')
fn = fn + fn
random.shuffle(fn)
#making a grid with 2D lists
for i in range(4):
    row = []
    for j in range(6):
        row.append(fn[i*6+j])
    twod.append(row)
print(twod)

for r in range(4):
    for c in range(6): 
        pic = img_resize("marvel_pics/marvel.png",200)
        but = Fl_Button(c*200, r*200, 200, 200)
        but.image(pic)
        LB.append(but)
        LB[-1].callback(but_cb)

win.end()

#box.image(pic)
win.resizable(win)

win.show()
Fl.run()


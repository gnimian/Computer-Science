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
storage = []
def but_cb(wid,data):
    count=0
    r,c=data
    if count <2:
        wid.image(twod[r][c])
        storage.append(name[r][c])
        print(storage)
    

win = Fl_Window(1200,800)
win.begin()

LB=[]
twod=[]
coun=[]
name = []
#making list of pictures
#fn=os.listdir('marvel_pics')
fn = ["dococ.png","electro.png","goblin.png","hulk.png","ironman.png","lizard.png","mysterio.png","rhino2.png","sandman.png","spiderman.png","venom.png","wolverine.png"]
fn = fn + fn
random.shuffle(fn)
I=[Fl_PNG_Image(f).copy(200,200)for f in fn]
print(I)
#making a grid with 2D lists
for i in range(4):
    row = []
    for j in range(6):
        row.append(I[i*6+j])
    twod.append(row)

for i in range(4):
    twooo = []
    for j in range(6):
        twooo.append(fn[i*6+j])
    name.append(twooo)

for r in range(4):
    for c in range(6): 
        pic = img_resize("marvel.png",200)
        but = Fl_Button(c*200, r*200, 200, 200)
        but.image(pic)
        LB.append(but)
        LB[-1].callback(but_cb,(r,c))

win.end()

#box.image(pic)
win.resizable(win)

win.show()
Fl.run()


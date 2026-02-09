#Project Started 2/9/26
#Memory Game. Enjoy!!!!
from fltk import *
from PIL import Image
import io
#deactive images widget.deactivate()

def img_resize(fname,width):
    img = Image.open(fname)
    w,h = img.size
    height = int(width*h/w)
    img = img.resize((width, height), Image.BICUBIC)
    mem = io.BytesIO()
    img.save(mem, format="PNG")
    siz = mem.tell()
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def but_cb(wid):
    wid.color(FL_GREEN)

#resize picture
Images=["dococ.png","electro.png","goblin.png","hulk.png","ironman.png","lizard.png","mysterio.png","rhino2.png","sandman.png","spiderman.png","venom.png","wolverine.png"]

pic = img_resize('dococ.png', 300)
win = Fl_Window(pic.w(), pic.h(), 'PIL resizing')
win.begin()
box = Fl_Box(0, 0, pic.w(), pic.h())
#make buttons into grid
LB=[]
win = Fl_Window(600,400)
win.begin()
for row in range(4):
    for col in range(6):
        but = col*100, row*100, 100, 100
        but.image(pic)
        LB.append( Fl_Button())
        LB[-1].callback(but_cb)


win.end()

#box.image(pic)
win.resizable(win)

win.show()
Fl.run()


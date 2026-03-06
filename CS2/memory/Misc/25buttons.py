from fltk import *
import random
win=Fl_Window(1000,1000)
win.begin()
buttons=[]
for i in range(25):
    a=random.randrange(100,900)
    b=random.randrange(0,900)
    b=Fl_Button(a,b,100,100)
    buttons.append(b)
win.end()
win.show()
Fl.run()
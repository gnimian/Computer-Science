from fltk import *
def but_cb(wid):
    wid.deactivate()
    wid.image().inactive() #prevets receiving future events
pic=Fl_PNG_Image('hulk.png')
win=Fl_Window(400,400)
win.begin()
but=Fl_Button(20,20)

'''
import random
import os
fn=os.listdir('marvel_pics')
fn = fn + fn
random.shuffle(fn)
'''

#.index() tracks which item you click

#.     0           1                16
F=['Hulk.png','Spidy.png',"...","Spidy.png"]
I = ["images","images"]
B = ["buttons","buttons"]
Fl_PNG_Image('__')
def but_cb(wid):
    i = B.index(wid)
    F[16]==F[1]
#   'spiderman' == 'spiderman'
but.callback(but.cb)

'''
#1D list
def but_cb(wid):
    print(B.index(wid))
win = Fl_Window(500,500)
B=[]
win.begin()
for r in range(4):
    for c in range(5):
        but = Fl_Button(50*c,50*r,50,50)
        B.append(but)
        B[-1].callback(but_cb)
win.end()
win.show()
Fl.run

#2D list
def but_cb(wid, loc):
    print(loc)
win = Fl_Window(500,500)
B=[]
win.begin()
for r in range(4):
    b=[]
    for c in range(5):
        but = Fl_Button(50*c,50*r,50,50)
        b.append(but)
        b[-1].callback(but_cb,(r,c))
    B.append(b)
win.end()
win.show()
Fl.run
'''

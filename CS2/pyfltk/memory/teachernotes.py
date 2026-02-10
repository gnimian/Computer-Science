from fltk import *
def but_cb(wid):
    wid.deactivate()
    wid.image().inactive() #prevets receiving future events
pic=Fl_PNG_Image('hulk.png')
win=Fl_Window(400,400)
win.begin()
but=FlButton(20,20)

'''
import random
import os
fn=os.listdir('marvel_pics')
print(fn)
fn = fn + fn
random.shuffle(fn)
'''

#.index() tracks which item you click

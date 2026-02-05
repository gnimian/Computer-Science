from fltk import *
import random
def but_cb(wid): 
    a=random.choices(range(len(choices)),k=3)
    pic1=Fl_PNG_Image(choices[a[0]]).copy(300,400)
    pic2=Fl_PNG_Image(choices[a[1]]).copy(300,400)
    pic3=Fl_PNG_Image(choices[a[2]]).copy(300,400)
    box1.image(pic1)
    #box1.box(FL_DOWN_BOX)
    box2.image(pic2)
    #box2.box(FL_DOWN_BOX)
    box3.image(pic3)
    #box3.box(FL_DOWN_BOX)
    win.redraw()
    print(a, end=' ')
    if a[0]==a[1]==a[2]:
        fl_message('you win')
        print('1000')
        win.hide()
    elif a[0]!=a[1]!=a[2]:
        print('3')
    else:
        print('2')

choices=['bell.png','cherry.png','grapes.png','lemon.png','seven.png','watermelon.png']

win=Fl_Window(900,500)
win.label("slot machine")
win.show()
win.begin() 

#background
bg1=Fl_Box(0,0,300,400)
bg1.color(FL_BLUE)
bg1.box(FL_FLAT_BOX)
bg2=Fl_Box(300,0,300,400)
bg2.color(FL_RED)
bg2.box(FL_FLAT_BOX)
bg3=Fl_Box(600,0,300,400)
bg3.color(FL_BLUE)
bg3.box(FL_FLAT_BOX)

#different boxes
box1 = Fl_Box(0,0,300,400)
box2 = Fl_Box(300,0,300,400)
box3 = Fl_Box(600,0,300,400)
box1.box(FL_NO_BOX)
box2.box(FL_NO_BOX)
box3.box(FL_NO_BOX)

#button
but = Fl_Button(0,400,900,100)
but.callback(but_cb)
but.label("pull")

win.end()
win.show()
Fl.run() 



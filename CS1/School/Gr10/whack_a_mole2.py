from fltk import *
import random

def foo(wid):
    #v = str(int(o.value()) + 1) 
    v= o.value()
    v = int(v) + 1
    o.value(str(v))

def timer():
    w = t.value()
    w = int(w) + 1
    t.value(str(w))
    Fl.repeat_timeout(1,timer)
    
def make_button():
    x=random.randrange(400)
    y=random.randrange(400)
    col = random.randrange(255)
    w.begin() 
    but = Fl_Button(x, y, 100, 100, 'Click me')
    but.color(col)
    but.box(FL_OVAL_BOX)
    but.callback(foo)
    w.redraw()
    Fl.add_timeout(1, remove_button)

def remove_button():
    w.remove(2)
    w.redraw()
    make_button()


w = Fl_Window(500,500)
w.begin()
#output bar
o = Fl_Output(20,20,70,30)
o.value('0')

#timer
t=Fl_Output(400,20,70,30)
t.value('0')
Fl.add_timeout(0,timer)
make_button()

w.show()
Fl.run()
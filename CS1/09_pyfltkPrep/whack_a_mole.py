from fltk import *
import random

def make_button():
    a=random.randrange(800)
    b=random.randrange(800)
    col = random.randrange(255)
    w.begin() 
    but = Fl_Button(a, b, 100, 100, 'Click me')
    but.color(col)
    but.box(FL_OVAL_BOX)
    w.redraw()
    Fl.add_timeout(0.0001, remove_button)

def remove_button():
    w.remove(0)
    w.redraw()
    make_button()

w = Fl_Window(900, 900, "Whack a Mole")
make_button()
w.show()
Fl.run()
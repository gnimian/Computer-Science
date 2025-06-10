from fltk import *

def foo(wid):
    print('you clicked me, ouch')

w1 = Fl_Window(400, 300, 'this is my first window')
but = Fl_Button(0, 0, 100, 30, 'click me')
but.callback(foo)
w1.show()

Fl.run()

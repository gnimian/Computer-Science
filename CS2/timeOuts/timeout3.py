from fltk import *

def tofunc():
        but.do_callback()
        Fl.repeat_timeout(1.0, tofunc)

def but_cb(w):
        if but.image()!=None:
                print("remove image")
                but.image(None)
                but.redraw()
        else:
                print("put image")
                but.image(pic)
                but.redraw()

def but2_cb(w):
        Fl.remove_timeout(tofunc)

win = Fl_Window(500,100,300,400,"my gui")
win.begin()
but = Fl_Button(100,90, 100, 110)
but2= Fl_Button(100,250,70,30,"Stop")
win.end()

but.callback(but_cb)
but2.callback(but2_cb)
pic=(Fl_JPEG_Image("spaceman.jpeg")).copy(but.w(),but.h())
Fl.add_timeout(1.0, tofunc)

win.show()
Fl.run()
from fltk import *

def foo(wid):
    print('you clicked me, ouch')
    wid.color(FL_GREEN)
    #but.color()

pic=Fl_JPEG_Image("1.jpeg")
pic = pic.copy(300,300)

w1=Fl_Window(400, 300, 'this is my first window')
#but = Fl_Button(0, 0, 100, 30, 'Click me')
but2 = Fl_Button(0, 100, 100, 30, 'me too')
but2.image(pic)
#but.callback(foo)
#but2.callback(foo)
w1.show()

Fl.run()



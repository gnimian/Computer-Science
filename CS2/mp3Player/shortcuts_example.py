from fltk import *

def but_cb(wid):
    print('event')

win = Fl_Window(0,0,400, 400, "shortcuts")
win.begin()
but = Fl_Button(10,10, 170, 50,'OK')
but.clear_visible_focus()
#but2 = Fl_Button(10,100, 170, 50,'aaaaaaa')
#win.focus(but2)
win.end()
#but.shortcut(FL_CTRL | ord('a')) #Ctrl-a
but.shortcut(FL_CTRL | ord(' ')) #ctrl spacebar
# or any of the shortcuts below
#but.shortcut(FL_META | ord('a')) #windows-a
#but.shortcut(FL_Left) #left arrow
#but.shortcut(FL_ALT|FL_F+6) #Alt-F6
#but.shortcut(ord('6')) #6

but.callback(but_cb)

win.show()
Fl.run()

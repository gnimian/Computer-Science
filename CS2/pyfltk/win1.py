from fltk import *
#win=Fl_Window(400,400,"my program")
win=Fl_Window(400,400)
win.label("my special program")
win.show()
win.begin() #any new widgets(object you can place in a window) will belong to win
#anything in fltk is a widget

#               X, Y, width, height
#but = Fl_Button(100,200,70,30,"Okay")
but = Fl_Button(100,200,70,30) #constructs or creates the button

win.end()

but.label("OK")
print(but.label())
#but.color(93)#main page -> drawing things -> colors

#Files -> functions -> R
c = fl_rgb_color(148, 225, 179)
but.color(c)

win.show()
Fl.run() #start event loop

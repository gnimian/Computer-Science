from fltk import *
#Apparantely Fl_Pack to resize button is completely broken in 1.4, so we are going to switch to Fl_Group 
#each group can only have one resizable widget
#A window is also a group
#Groups are:    g      g2      win
#Resizable:   bl[0]    b1       g

def but_cb(wid):
    if wid.color() == FL_RED:
        wid.color(FL_GREEN)
    else:
        wid.color(FL_RED)

win = Fl_Window(0,0,400, 400, "Fl_Group")
win.begin()
g=Fl_Group(0,0, 400, 300)
g.begin()

bl=[]
width = g.w()//3
for x in range(3):
    bl.append(Fl_Button(width*x, 0, width, 300, str(x)))
    bl[-1].callback(but_cb)

g.end()
#bl[0] is the first button 
g.resizable(g) #set resizable arg as either 1)widget 2)Group itself 3)None
#g.resizable(None)
#g.resizable(bl[0])

#color resizeable widget 
#bl[0].color(FL_RED)

g2= Fl_Group(0, 300, 400, 100)
g2.begin()

b1=Fl_Button(0,300, 400, 100//2,'b1')
b2=Fl_Button(0,350, 400, 100//2,'b2')
b1.callback(but_cb)
b2.callback(but_cb)

g2.end()
g2.resizable(g2)
#b1.color(FL_RED)

win.end() 
win.resizable(g)
win.show()
Fl.run()


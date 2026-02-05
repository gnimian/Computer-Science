from fltk import *
import random
times=1
def foo():
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
    global times
    x=random.randrange(400)
    y=random.randrange(400)
    col = random.randrange(255)
    w.begin() 
    but = Fl_Button(x, y, 100, 100)
    but.box(FL_NO_BOX)
    pic=Fl_PNG_Image("button.png")
    pic = pic.copy(100,100)
    but.image(pic)
    but.callback(foo)
    w.end()
    w.redraw()
    times-=0.01
    Fl.add_timeout(times, remove_button)

def remove_button():
    if w.children() > 2:
        w.remove(w.children() - 1) 
    w.redraw()
    make_button()


w = Fl_Window(500,500)
w.begin()

bg_box = Fl_Box(0, 0, 500, 500)
bg_image = Fl_JPEG_Image('image.jpeg')
bg_box.image(bg_image)

o = Fl_Output(20,20,70,30)
o.value('0')

t = Fl_Output(400,20,70,30)
t.value('0')

w.end()

w.begin()
#output bar
o = Fl_Output(20,20,70,30)
o.value('0')

#timer
t=Fl_Output(400,20,70,30)
t.value('0')
w.end()
Fl.add_timeout(0,timer)
make_button()

w.show()
Fl.run()
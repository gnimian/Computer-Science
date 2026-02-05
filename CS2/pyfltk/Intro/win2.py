from fltk import *

def but_cb(wid): #def but_cb(): not going to work, need to pass in a parameter
    print('click')
    if wid.label() == 'OK':
        wid.label('done')
        wid.color(FL_GREEN)
    else:
        wid.label('OK')
        wid.color(FL_RED)

pic=Fl_JPEG_Image("1.jpg") #.copy(300,300)
width = pic.w()
height = pic.h()
print("image size:", width, height)


win=Fl_Window(700,700)
win.label("my special program")
win.show()
win.begin() 


but = Fl_Button(100,200,90,50)
but2 = Fl_Button(100,300,90,50)
but3 = Fl_Button(250,200,width,height)
win.end()

but3.image(pic)

but.callback(but_cb)
but2.callback(but_cb)
but.label("OK")
print(but.label())
but.color(FL_RED)

win.show()
Fl.run() 
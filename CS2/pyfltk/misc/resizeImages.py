from fltk import *
def resize(NW, I):
    CW = I.w() #original width
    CH = I.h() # original height
    ratio = CW/CH
    NH = NW/ratio  
    I.resize(NW,NH)
    return I

Face = Fl_PNG_Image('Face.png')
resize(600,Face)
Face = resize(600,Face)


#This way is more simple
from PIL import Image
import io

def img_resize(fname,width):
    '''resizes any image type using high quality PIL library'''
    img = Image.open(fname) #opens all image formats supported by PIL
    w,h = img.size
    height = int(width*h/w)  #correct aspect ratio
    img = img.resize((width, height), Image.BICUBIC) #high quality resizing
    mem = io.BytesIO()  #byte stream memory object
    img.save(mem, format="PNG") #converts image type to PNG byte stream
    siz = mem.tell() #gets size of image in bytes without reading again
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

pic = img_resize('cat.jpg', 300) #resizes to 300 pixels width
win = Fl_Window(pic.w(), pic.h(), 'PIL resizing')
win.begin()
box = Fl_Box(0, 0, pic.w(), pic.h())
win.end()

box.image(pic)

win.show()
Fl.run()

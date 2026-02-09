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
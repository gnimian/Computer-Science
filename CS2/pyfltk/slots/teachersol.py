from fltk import *
import random

def pull_cb(wid):
    shown=[] #ints of image indices
    for x in range(3):
        i=random.randrange(len(I)) #random int 0-5
        B[x].image(I[i])
        #B[x].image().inactive()
        shown.append(i)
        B[x].redraw()
    #win.redraw()
    print(shown,len(shown))
    '''
    if shown[0]==shown[1] and shown[1]==shown[2]:
        fl_message('You Win!')
    '''
    if len(set(shown))==1:
        fl_message('You win!')
        
#create images
fnames=['bell.png','cherry.png','grapes.png','lemon.png','seven.png','watermelon.png']
I = [] #list of 6 images
for name in fnames:
    I.append(Fl_PNG_Image(name).copy(200,300))
win=Fl_Window(600,350)
B=[]
win.begin()

for x in range(3):
    b=Fl_Box(x*200,0,200,300)
    b.box(FL_SHADOW_BOX) #msut set since default box type is FL_NO_BOX
    b.color(207)
    B.append(b)
pull = Fl_Button(0,300,650,50,'pull')
pull.tooltip('Hit enter to play again')
pull.callback(pull_cb)
pull.labelsize(24)
#pull.deactivate()
win.end()
win.show()
Fl.run()
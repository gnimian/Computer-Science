#Project Started 2/9/26
#Project Finished 2/18/26 (still refining)
#Memory Game. Enjoy!!!!

from fltk import *
from PIL import Image
import io
import random
#import os

#resizes images, copy and paseted from Mr.Ark's website
def img_resize(fname,height):
    img = Image.open(fname)
    #w,h = img.size
    #width = int(height*w/h) 
    # #this can be used to resize the image while keeping the aspect ratio, but I just want to make them all square for simplicity
    img = img.resize((height, height), Image.BICUBIC)
    mem = io.BytesIO()
    img.save(mem, format="PNG")
    siz = mem.tell()
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

nameCompare = []
butRepeat = []
butCompare=[]
count=0
tries = 0
back_image = img_resize("marvel.png",200)

def but_cb(wid,data):
    global count,nameCompare,butCompare,butRepeat,tries
    r,c = data
    #make button back to marvel if not match
    if len(nameCompare) == 2 and nameCompare[0] != nameCompare[1]:
            butCompare[0].image(back_image)
            butCompare[1].image(back_image)
            butCompare[0].redraw() #MUST NEED
            butCompare[1].redraw()
            butCompare.clear()
            nameCompare.clear()

    if len(butRepeat)==1 and butRepeat[0] == wid:
        return
    
    wid.image(image2D[r][c])
    wid.redraw()
    butCompare.append(wid)
    butRepeat.append(wid)
    nameCompare.append(name2D[r][c])

    #deactivate buttons if match and check if win
    if len(nameCompare)==2:
        tries+=1
        if nameCompare[0]==nameCompare[1]:
            butCompare[0].deactivate()
            butCompare[0].image().inactive()
            wid.deactivate()
            wid.image().inactive()
            butCompare.clear()
            nameCompare.clear()
            count+=1
        if count == 12:
            fl_message(f'you win! You got all matches in {tries} tries!')
            win.hide()
        butRepeat.clear()


win = Fl_Window(1200,800)
win.begin()

#fn=os.listdir('marvel_pics'): this can be used to import all the images in the folder, but I just list then out for simplicity.
#importing images and making into images for fltk
fn = ["dococ.png","electro.png","goblin.png","hulk.png","ironman.png","lizard.png","mysterio.png","rhino2.png","sandman.png","spiderman.png","venom.png","wolverine.png"]
fn = fn + fn
random.shuffle(fn)
#I=[Fl_PNG_Image(f).copy(200,200)for f in fn]
I=[img_resize(f, 200) for f in fn]

#making a grid of images with 2D lists. Subsituting images for marvel.png when calling function
image2D=[]
for i in range(4):
    row = []
    for j in range(6):
        row.append(I[i*6+j])
    image2D.append(row)


#making a grid of names with 2D lists. Comparing 2 images when calling function
name2D=[]
for i in range(4):
    temp = []
    for j in range(6):
        temp.append(fn[i*6+j])
    name2D.append(temp)


#making buttons 
butMaker=[]    
for row in range(4):
    for column in range(6): 
        marvelPic = img_resize("marvel.png",200)
        but = Fl_Button(column*200, row*200, 200, 200)
        but.image(marvelPic)
        butMaker.append(but)
        butMaker[-1].callback(but_cb,(row,column))

win.end()
win.resizable(win) #makes window resizable 
win.show()
Fl.run()
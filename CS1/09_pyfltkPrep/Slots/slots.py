from fltk import *
import random
w = Fl_Window(1500,900)
w.begin()

bg_box1 = Fl_Box(15,10,480,750)
bg_box1.box(FL_FLAT_BOX)
bg_box1.color(FL_WHITE)
bg_box2 = Fl_Box(510,10,480,750)
bg_box2.box(FL_FLAT_BOX)
bg_box2.color(FL_WHITE)
bg_box3 = Fl_Box(1005,10,480,750)
bg_box3.box(FL_FLAT_BOX)
bg_box3.color(FL_WHITE)

bg_1 = Fl_Box(15,10,480,700)
bg_1.box(FL_NO_BOX)
bg_2 = Fl_Box(510,10,480,700)
bg_2.box(FL_NO_BOX)
bg_3 = Fl_Box(1005,0,480,700)
bg_3.box(FL_NO_BOX)
bg_image1 = None
bg_image2 = None
bg_image3 = None
points=0
def icon():
    pngs = ['bell.png', 'cherries.png', 'clover.png', 'heart.png', 'lemon.png', 'rainbow.png', 'melon.png']
    return random.choices(pngs, k=3)

def choose_icon(widget=None):
    remove_icon()
    global bg_image1, bg_image2, bg_image3, points
    icons = icon()
    
    bg_image1 = Fl_PNG_Image(icons[0])
    bg_image1 = bg_image1.copy(400,400)
    bg_1.image(bg_image1)
    bg_1.redraw()

    bg_image2 = Fl_PNG_Image(icons[1])
    bg_image2 = bg_image2.copy(400,400)
    bg_2.image(bg_image2)
    bg_2.redraw()

    bg_image3 = Fl_PNG_Image(icons[2])
    bg_image3 = bg_image3.copy(400,400)
    bg_3.image(bg_image3)
    bg_3.redraw()

    if icons[0] == icons[1] == icons[2]:
        points += 1000
        print('You gained 1000 points!')
        print(f'Total points: {points}')
    elif icons[0] == icons[1] or icons[1] == icons[2] or icons[0] == icons[2]:
        points += 100
        print('You gained 100 points!')
        print(f'Total points: {points}')
    else:
        points -= 100
        print('You lost 100 points!')
        print(f'Total points: {points}')
    w.redraw()
        
    make_button()

def make_button():
    button = Fl_Button(15, 775, 1470, 115, 'Click to spin')
    button.color(FL_WHITE)
    button.callback(choose_icon)

def remove_icon():
    global bg_image1, bg_image2, bg_image3
    if bg_image1:
        bg_1.image(None)
        bg_image1 = None
    if bg_image2:
        bg_2.image(None)
        bg_image2 = None
    if bg_image3:
        bg_3.image(None)
        bg_image3 = None
    w.redraw()



make_button()
w.end()
w.show()
Fl.run()
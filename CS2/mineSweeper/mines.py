from fltk import *
import random
from PIL import Image
import io

buttons = []
bombs = []
bombnum = 10
bombfound = 0
revealed = []
flagged = []
colour = [fl_rgb_color(189, 189, 189), fl_rgb_color(170, 170, 170), fl_rgb_color(224, 224, 224), fl_rgb_color(210, 210, 210)]
secs = -1

def img_resize(fname, width):
    img = Image.open(fname)
    w, h = img.size
    height = int(width*h/w)
    img = img.resize((width, height), Image.BICUBIC)
    mem = io.BytesIO()
    img.save(mem, format="PNG")
    siz = mem.tell()
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def around(index):
    L = []
    for a in range(index[0]-1, index[0]+2):
        for b in range(index[1]-1, index[1]+2):
            if a == index[0] and b == index[1]:
                continue
            if a >= 0 and b >= 0 and a <= 9 and b <= 9:
                if buttons[index[0]][index[1]] not in buttons:
                    L.append([a, b])
    return L

def time_cb():
    global secs
    secs += 1
    if secs%60 < 10:
        timer.label(f"{secs//60}:0{secs%60}")
    else:
        timer.label(f"{secs//60}:{secs%60}")
    Fl.repeat_timeout(1, time_cb)

def start(but, index):
    global bombs
    templist = []
    if len(bombs) >= bombnum:
        return
    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    for i in around(index):
        templist.append(buttons[i[0]][i[1]])
    if (buttons[num1][num2] not in bombs) and (buttons[num1][num2] not in templist):
        if buttons[num1][num2] != but:
            bombs.append(buttons[num1][num2])
    if len(bombs) < bombnum:
        start(but, index)

def lclick(but, index):
    global bombfound, secs
    bombcount = 0
    if len(bombs) == 0:
        time_cb()
        start(but, index)
    if but in bombs:
        Fl.remove_timeout(time_cb)
        top.label("YOU LOST. CLICK HERE TO RESTART")
        top.when(FL_WHEN_RELEASE)
        for bomb in bombs:
            bomb.image(img_resize("mines.png", 50))
            win.redraw()
        for flag in flagged:
            if flag not in bombs:
                flag.image(None)
                flag.color(FL_RED)
        for row in buttons:
            for b in row:
                b.when(0)
        fl_message(f"Game over.\nclick the top button to play again.")
        return

    for i in around(index):
        if buttons[i[0]][i[1]] in bombs:
            bombcount += 1
    if but not in revealed:
        revealed.append(but)
    if index[0]%2 == 0 and index[1]%2 == 0 or index[0]%2 == 1 and index[1]%2 == 1:
        but.color(colour[2], colour[2])
    else:
        but.color(colour[3], colour[3])
    if bombcount == 0:
        win.redraw()
        for j in around(index):
            if buttons[j[0]][j[1]] not in revealed:
                lclick(buttons[j[0]][j[1]], j)
    else:
        if bombcount == 1:
            but.labelcolor(fl_rgb_color(25, 118, 210))
        elif bombcount == 2:
            but.labelcolor(fl_rgb_color(56, 142, 60))
        elif bombcount == 3:
            but.labelcolor(fl_rgb_color(211, 47, 47))
        elif bombcount == 4:
            but.labelcolor(fl_rgb_color(141, 59, 161))
        elif bombcount >= 5:
            but.labelcolor(fl_rgb_color(209, 92, 0))
        but.labelsize(30)
        but.labelfont(FL_HELVETICA_BOLD)
        but.label(str(bombcount))

    if len(revealed) + bombnum == 100:
        counter.label(f"MINES: {bombnum}/{bombnum}")
        top.label("YOU WON! CLICK HERE TO RESTART")
        for bomb in bombs:
            bomb.image(img_resize("flag.png", 50))
            win.redraw()
        for row in buttons:
            for b in row:
                b.when(0)
        Fl.remove_timeout(time_cb)
        fl_message(f"you won! it took you {secs//60} minute(s) and {secs%60} second(s). click the top button to play again.")

def rclick(but):
    global bombfound
    if but in flagged:
        but.image(None)
        win.redraw()
        flagged.remove(but)
        bombfound -= 1
        counter.label(f"MINES: {bombfound}/{bombnum}")
        return
    if but not in revealed:
        but.image(img_resize("flag.png", 50))
        but.redraw()
        bombfound += 1
        counter.label(f"MINES: {bombfound}/{bombnum}")
        flagged.append(but)

def play(but, index):
    top.label("CLICK HERE TO RESTART")
    if Fl.event_button() == FL_LEFT_MOUSE:
        if but not in flagged:
            lclick(but, index)
    elif Fl.event_button() == FL_RIGHT_MOUSE:
        if len(bombs) != 0:
            rclick(but)
        else:
            top.label("CLICK ANY BUTTON TO PLAY")

def restart(wid):
    global bombs, revealed, flagged, secs, bombfound
    top.label("CLICK ANY BUTTON TO PLAY")
    bombs = []
    revealed = []
    flagged = []
    secs = -1
    bombfound = 0
    counter.label(f"MINES: {bombfound}/{bombnum}")
    Fl.remove_timeout(time_cb)
    timer.label("0:00")
    for i in range(10):
        for j in range(10):
            buttons[i][j].when(FL_WHEN_RELEASE)
            buttons[i][j].label(None)
            buttons[i][j].image(None)
            if i%2 == 0 and j%2 == 0 or i%2 == 1 and j%2 == 1:
                buttons[i][j].color(colour[0], colour[1])
            else:
                buttons[i][j].color(colour[1], colour[0])


win = Fl_Window(500, 540, "Minesweeper")
win.resizable(win)
win.color(fl_rgb_color(128, 128, 128))

for row in range(10):
    b = []
    for col in range(10):
        b.append(Fl_Button(col*50, row*50+40, 50, 50))
        b[-1].box(FL_FLAT_BOX)
        b[-1].clear_visible_focus()
        if row%2 == 0 and col%2 == 0 or row%2 == 1 and col%2 == 1:
            b[-1].color(colour[0], colour[1])
        else:
            b[-1].color(colour[1], colour[0])
    buttons.append(b)

top = Fl_Button(100, 0, 300, 40)
counter = Fl_Box(0, 0, 100, 40)
timer = Fl_Box(400, 0, 100, 40)

top.box(FL_FLAT_BOX)
top.color(fl_rgb_color(50, 50, 50))

counter.box(FL_FLAT_BOX)
counter.color(fl_rgb_color(40, 40, 40))

timer.box(FL_FLAT_BOX)
timer.color(fl_rgb_color(40, 40, 40))

top.clear_visible_focus()
counter.clear_visible_focus()
timer.clear_visible_focus()

top.labelcolor(FL_WHITE)
counter.labelcolor(FL_WHITE)
timer.labelcolor(FL_WHITE)

top.label("CLICK ANY BUTTON TO PLAY")
counter.label(f"MINES: {bombfound}/{bombnum}")
timer.label("0:00")

top.labelfont(FL_HELVETICA_BOLD)
counter.labelfont(FL_HELVETICA_BOLD)
timer.labelfont(FL_HELVETICA_BOLD)

for row in range(10):
    for col in range(10):
        buttons[row][col].callback(play, (row, col))

top.callback(restart)

win.end()
win.show()
Fl.run()

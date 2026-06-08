#MP3 Player
#Started on 1/3/2026
from fltk import *
import os
import subprocess as sp
pid = None
mp3names={}
currentPlay = False
number = []
ppp = 0
def start_vlc(song_path):
    return sp.Popen(['vlc', '--intf', 'dummy', song_path])

store = []
def opendir_cb(wid):
    global mp3names,browser, number, store
    d=fl_dir_chooser('Pick a directory to view mp3','')
    if d==None: # Cancel clicked
        return []
    fnames=os.listdir(d)
    for name in fnames:
        if name[-4:] in ('.mp3','.MP3'):
            stt = name[:-4]
            mp3names[stt]= os.path.join(d,name)
            store.append(stt)
            number.append(stt)
    store.sort(key = str.lower)
    for i in range(len(number)):
        browser.add(store[i])
         

def play_cb(wid):
    global pid,currentPlay, message,store,number, ppp
    if len(number) == 0 or browser.value() == 0:
            return
    if currentPlay:
        pid.send_signal(sp.signal.SIGTERM)
    pos = browser.value()
    ppp = pos
    hover = browser.text(pos)
    pid = start_vlc(mp3names[hover])
    currentPlay=True
    message.label(hover)
    
def previous_cb(wid):
    global pid,currentPlay,message, number, ppp
    if len(number) == 0 or browser.value() == 0:
            return
    
    if not currentPlay:
        if browser.value()==1:
            browser.value(len(number))
            hover1 = browser.text(len(number))
        else:
            pos1 = browser.value()
            browser.value(pos1-1)
        return
    
    if pid and currentPlay:
        pid.send_signal(sp.signal.SIGTERM)
        currentPlay = False

    if browser.value()==1:
        browser.value(len(number))
        hover1 = browser.text(len(number))
        pid = start_vlc(mp3names[hover1])
        ppp = browser.value()
        currentPlay=True
        message.label(hover1)
    else:
        pos1 = browser.value()
        browser.value(pos1-1)
        pos2 = browser.value()
        hover1 = browser.text(pos2)
        pid = start_vlc(mp3names[hover1])
        ppp = browser.value()
        currentPlay=True
        message.label(hover1)

def next_cb(wid):
    global pid,currentPlay,message, number, ppp
    if len(number) == 0 or browser.value() == 0:
            return
    
    if not currentPlay:
        if browser.value()==len(number):
            browser.value(1)
            hover1 = browser.text(1) 
        else:
            pos1 = browser.value()
            browser.value(pos1+1)
        return
    
    if pid and currentPlay:
        pid.send_signal(sp.signal.SIGTERM)
        currentPlay = False
    
    
    if browser.value()==len(number):
        browser.value(1)
        hover1 = browser.text(1)
        pid = start_vlc(mp3names[hover1])
        ppp = browser.value()
        currentPlay=True
        message.label(hover1)

    else:
        pos1 = browser.value()
        browser.value(pos1+1)
        pos2 = browser.value()
        hover1 = browser.text(pos2)
        pid = start_vlc(mp3names[hover1])
        ppp = browser.value()
        currentPlay=True
        message.label(hover1)

def stop_cb(wid):
    global pid,currentPlay,message
    if len(number) == 0 or browser.value() == 0:
            return
    if pid and currentPlay:
        pid.send_signal(sp.signal.SIGTERM)
        currentPlay=False
        pid = None
        message.label('')

def deletes_cb(wid):
    global pid,currentPlay,message, number,store, ppp
    if len(number) == 0 or browser.value() == 0:
            return
    
    current = browser.value()
    
    if browser.text(browser.value()) == message.label():
        pid.send_signal(sp.signal.SIGTERM)
        currentPlay = False
        message.label('')
    del mp3names[browser.text(current)]
    number.remove(browser.text(current))
    browser.remove(current)
    if current > len(number):
         current = len(number)
    browser.value(current) #set to next song after deletion
    

def playing_cb(wid):
    global pid,currentPlay,message,number,store,ppp
    if len(number) > 0:
        browser.value(ppp)
def first_cb(wid):
    browser.value(1)

def last_cb(wid):
    global number
    if len(number) == 0:
         return
    browser.value(len(number))

def clear_cb(wid):
    global pid,currentPlay,message,mp3names,number
    if pid and currentPlay:
        pid.send_signal(sp.signal.SIGTERM)
    currentPlay = False
    message.label('')
    browser.clear()
    mp3names.clear()
    number.clear()
    

win=Fl_Window(500,400,'pyFltk MP3 Player')
win.begin()
#making a menu bar with items
menu=Fl_Menu_Bar(0,0,500,25)
menu.add("Add/Directory",ord('d'),opendir_cb)
menu.add("Go/Playing",ord('p'),playing_cb)
menu.add("Go/First",ord('f'),first_cb)
menu.add("Go/Last",ord('l'),last_cb)
menu.add("Clear/All",FL_SHIFT | ord('a'),clear_cb)


#making browser
group = Fl_Group(0,50,500,250)
browser=Fl_Hold_Browser(0,50,500,250)
#browser.clear_visible_focus()
group.resizable(browser)
group.end()

#making menu message
message = Fl_Box(0,25,500,25)
message.box(FL_FLAT_BOX)
message.color(FL_YELLOW)
message.labelcolor(FL_RED)
message.labelfont(FL_BOLD)
message.align(FL_ALIGN_LEFT | FL_ALIGN_INSIDE)

#playback buttons
g2 = Fl_Group(0,300,500,100)

play = Fl_Button(100,300,100,100,'@>')
previous = Fl_Button(0,300,100,100,'@|<')
next = Fl_Button(200,300,100,100,'@>|')
stop = Fl_Button(300,300,100,100,'@square')
deletes = Fl_Button(400,300,100,100,'@undo')

play.callback(play_cb)
previous.callback(previous_cb)
next.callback(next_cb)
stop.callback(stop_cb)
deletes.callback(deletes_cb)
g2.resizable(None)

deletes.clear_visible_focus()
play.clear_visible_focus()
previous.clear_visible_focus()
next.clear_visible_focus()
stop.clear_visible_focus()


play.shortcut(FL_Enter)
previous.shortcut(FL_ALT | FL_Left)
next.shortcut(FL_ALT | FL_Right)
stop.shortcut(ord(' '))
deletes.shortcut(FL_BackSpace)

play.tooltip('Play (Enter)')
previous.tooltip('Previous (Alt <-)')
next.tooltip('Next (Alt ->)')
stop.tooltip('Stop (Space)')
deletes.tooltip('Remove (Del)')
win.resizable(group)
win.end()
win.show()
Fl.run()
if pid:
    pid.kill()
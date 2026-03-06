from fltk import *
import random
money=int(input("Enter the amount of money you want to bet: "))
def but_cb(wid): 
    global money 
    a=random.choices(range(len(choices)),k=3)
    pic1=Fl_PNG_Image(choices[a[0]]).copy(300,300)
    pic2=Fl_PNG_Image(choices[a[1]]).copy(300,300)
    pic3=Fl_PNG_Image(choices[a[2]]).copy(300,300)
    box1.image(pic1)
    box2.image(pic2)
    box3.image(pic3)
    win.redraw()
    print(a, end=' ')
    if a[0]==a[1]==a[2]:
        #fl_message('you win!')
        print('you won 100 dollars!')
        money+=100
        print(f'Your total money is {money} dollars')
    elif a[0]!=a[1]!=a[2]:
        print('you lost 10 dollars')
        money-=10
        print(f'Your total money is {money} dollars')
    else:
        print('you lost 5 dollars')
        money-=5
        print(f'Your total money is {money} dollars')
    if money<=0:
        fl_message('You have no more money to bet. Game over!')
        win.hide()


choices=['bell.png','cherry.png','grapes.png','lemon.png','seven.png','watermelon.png']

win=Fl_Window(900,400)
win.label("slot machine")
win.show()
win.begin() 


#different boxes
box1 = Fl_Box(0,0,300,300)
box2 = Fl_Box(300,0,300,300)
box3 = Fl_Box(600,0,300,300)
box1.box(FL_SHADOW_BOX)
box2.box(FL_SHADOW_BOX)
box3.box(FL_SHADOW_BOX)
box1.color(FL_BLUE)
box2.color(FL_RED)
box3.color(FL_BLUE)

#button
but = Fl_Button(0,300,900,100)
but.callback(but_cb)
but.label("pull")

win.end()
win.show()
Fl.run() 



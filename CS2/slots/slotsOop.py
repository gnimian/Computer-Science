from fltk import *
import random

class slotsMachine(Fl_Window):
    def __init__(self, width, height, name):
        Fl_Window.__init__(self, width, height, name)
        self.begin()
        self.money=int(input("Enter the amount of money you want to bet: "))
        self.choices=['bell.png','cherry.png','grapes.png','lemon.png','seven.png','watermelon.png']
        #different boxes
        self.box1 = Fl_Box(0,0,300,300)
        self.box2 = Fl_Box(300,0,300,300)
        self.box3 = Fl_Box(600,0,300,300)
        self.box1.box(FL_SHADOW_BOX)
        self.box2.box(FL_SHADOW_BOX)
        self.box3.box(FL_SHADOW_BOX)
        self.box1.color(FL_BLUE)
        self.box2.color(FL_RED)
        self.box3.color(FL_BLUE)
        self.but = Fl_Button(0,300,900,100)
        self.but.callback(self.but_cb)
        self.but.label("pull")
        self.show()
        self.end()
    
    def but_cb(self,wid):  
        a=random.choices(range(len(self.choices)),k=3)
        self.pic1=Fl_PNG_Image(self.choices[a[0]]).copy(300,300)
        self.pic2=Fl_PNG_Image(self.choices[a[1]]).copy(300,300)
        self.pic3=Fl_PNG_Image(self.choices[a[2]]).copy(300,300)
        self.box1.image(self.pic1)
        self.box2.image(self.pic2)
        self.box3.image(self.pic3)
        self.redraw()
        print(a, end=' ')
        if a[0]==a[1]==a[2]:
            #fl_message('you win!')
            print('you won 100 dollars!')
            self.money+=100
            print(f'Your total money is {self.money} dollars')
        elif a[0]!=a[1]!=a[2]:
            print('you lost 10 dollars')
            self.money-=10
            print(f'Your total money is {self.money} dollars')
        else:
            print('you lost 5 dollars')
            self.money-=5
            print(f'Your total money is {self.money} dollars')
        if self.money<=0:
            fl_message('You have no more money to bet. Game over!')
            self.hide()

if __name__=='__main__':
    slots = slotsMachine(900,400,'slot machine')
    Fl.run() 



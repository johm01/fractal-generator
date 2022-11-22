from tkinter import * 
from turtle import * 
import random
import fractals

class App:
    def __init__(self,title) -> None:
        # Main app 
       
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("500x75")
        self.root.resizable(width=False,height=False)

        self.size = IntVar()
        self.level = IntVar()
        self.angel = IntVar()

        # Fractal attributes 
        self.e1 = Entry(self.root,textvariable=self.size)
        self.e1.place(x=100,y=0)
        self.e2 = Entry(self.root,textvariable=self.level)
        self.e2.place(x=200,y=0)
        self.e3 = Entry(self.root,textvariable=self.angel)
        self.e3.place(x=300,y=0)

        self.type = 'Tree'

        #values = [int(self.e1.get()),self.e2.get(),self.e3.get()]
        # Button
        self.button = Button(self.root,text='Fractal Tree',command=lambda: self.tree(self.size.get(),self.level.get(),self.angel.get()))
        self.button.place(x=0,y=0)
        self.button_2 = Button(self.root,text='Serpinski Triangle',command=lambda: self.serpinski(self.size.get(),self.level.get(),self.angel.get()))
        self.button_2.place(x=0,y=35)
        self.button_3 = Button(self.root,text='Koch Kurve',command=lambda: self.koch_curve(self.size.get(),self.level.get(),self.angel.get()))
        self.button_3.place(x=0,y=70)


        self.root.mainloop()
    
    def triangle(self,size,angle):
        setheading(180)
        for i in range(3):
            right(angle)
            forward(size)

        # Serpinski Triangle
    def serpinski(self,n,size,angle):
        if n == 1:
            self.triangle(size,angle)
        else:
            self.serpinski(n - 1,size,angle)
            right(angle)
            forward(size * 2** (n-2))
            self.serpinski(n - 1,size,angle)
            left(angle)
            forward(size * 2** (n-2))
            self.serpinski(n - 1,size,angle)
            forward(size * 2** (n-2))

        ## Fractal Tree
    def tree(self,size,levels,angle):
        if levels ==0:
            color('Green')
            dot(size)
            color('Blue')
            return

        # Right side 
        forward(size)
        right(angle)

        self.tree(self,size * 0.8,levels - 1, angle)

            # Left side 
        left(angle *2)

        self.tree(size * 0.8,levels-1,angle)

            # Back to the start 
        right(angle)
        backward(size)

    # Koch Curve 
    def koch_curve(self,n,length,shorten_factor,angle):

        # Drawing at the start 
        if n == 0:
            forward(length)
        else:
            n -= 1
        
            self.koch_curve(n ,length,shorten_factor,angle)
            left(angle)
            self.koch_curve(n ,length,shorten_factor,angle)
            right(angle * 2)
            self.koch_curve(n ,length,shorten_factor,angle)
            left(angle)
            self.koch_curve(n ,length,shorten_factor,angle)

    # Custom fractal 
    def shape(self,n,size):
        if n == 0:
            dot('red')
            return
        forward(size) 
        left(90)
        shape(n-1,size)
        right(90)
        shape(n-1,size)
        left(90)
        shape(n-1,size)
       


if __name__ == '__main__':
    app = App('Fratcal Tree Maker!')

from tkinter import * 
from turtle import * 
import random

class App:
    def __init__(self,title) -> None:
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("500x500")
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

    
        #values = [int(self.e1.get()),self.e2.get(),self.e3.get()]
        # Button
        self.button = Button(self.root,text='Click me!',command=lambda: tree(self.size.get(),self.level.get(),self.angel.get()))
        
        self.button.place(x=0,y=0)

        self.root.mainloop()
    
def tree(size,levels,angle):
    if levels ==0:
        color('Green')
        dot(size)
        color('Blue')
        return
    forward(size)
    right(angle)

    tree(size * 0.8,levels - 1, angle)

    left(angle *2)

    tree(size * 0.8,levels-1,angle)

    right(angle)
    backward(size)
       
    
if __name__ == '__main__':
    app = App('Fratcal Tree Maker!')
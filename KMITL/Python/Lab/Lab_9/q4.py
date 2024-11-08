import tkinter as tk
import random 
import tkinter.messagebox as ttk

class Rectangle:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(bg ='white',width = 400 , height = 250)
        self.canvas.pack()
        self.canvas.bind("<Button-1>",self.oval)
        self.square()
        self.canvas.mainloop()
    def square(self):
        self.canvas.create_rectangle(20,20,370,220)
    def oval(self,event):
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
        rng = random.randint(0,6)
        if event.x < 370 and event.y < 220 and event.x > 20 and event.y > 20:
            self.canvas.create_oval(event.x-5,event.y+5,event.x+5,event.y-5,fill = colors[rng])
        else:
            error = ttk.showwarning("Warning","Mouse pointer is not in the rectangle")
        
Rectangle()

import tkinter as tk

class Mouse:
    def __init__(self):
        self.radius = 5
        root = tk.Tk()
        root.title("A simple paint program")
        self.canvas = tk.Canvas(root,bg = 'White',width = 750 , height = 500)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>",self.oval)
        clean = tk.Button(root,text = 'Clear',command = self.clear).pack(side ='bottom')
        drag = tk.Label(root,text="Drag the mouse to draw").pack(side ='bottom')
        root.mainloop()
    def oval(self,event):
        self.canvas.create_oval(event.x-5,event.y+5,event.x+5,event.y-5,fill = 'black',tags='x')
    def clear(self):
        self.canvas.delete("x")
Mouse()
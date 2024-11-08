import tkinter as tk

class Rectangle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("xd")
        self.canvas = tk.Canvas(bg='white', width=800, height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.oval) 
        self.canvas.bind("<Button-3>", self.oval_delete) 
        self.canvas.mainloop()
        
    def oval(self, event):
        self.canvas.create_oval(event.x-20, event.y+20, event.x+20, event.y-20, tag="oval")
        
    def oval_delete(self, event):
        items = self.canvas.find_withtag("oval")
        for item in items:
            x1, y1, x2, y2 = self.canvas.coords(item) 
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.canvas.delete(item)  
        
Rectangle()

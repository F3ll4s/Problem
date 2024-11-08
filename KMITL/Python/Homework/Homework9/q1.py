
import tkinter as tk
from tkinter import messagebox

class Phone:
    def __init__(self):
        root = tk.Tk()
        root.title("KMITL Phone")
        self.screen_var = tk.StringVar()
        self.screen = tk.Label(root, textvariable=self.screen_var, bg="white")
        self.screen.grid(row=0, column=0, columnspan=3)

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('*', 4, 0), ('0', 4, 1), ('#', 4, 2)
        ]
        
        for (text, row, column) in buttons:
            tk.Button(root, text=text, command=lambda t=text: self.update_screen(t)).grid(row=row, column=column)

        tk.Button(root, text="Talk", command=self.talk).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="<", command=self.clear).grid(row=5, column=2)

        root.mainloop()
    
    def update_screen(self, text):
        current = self.screen_var.get()
        self.screen_var.set(current + text)
    
    def clear(self):
        current = self.screen_var.get()
        if current:
            self.screen_var.set(current[:-1])
    
    def talk(self):
        number = self.screen_var.get()
        if number:
            messagebox.showinfo("Dialing", f"Dialing {number}")
        

Phone()

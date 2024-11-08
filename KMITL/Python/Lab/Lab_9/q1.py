import tkinter as tk


# class Button:
#     def __init__(self):
#         self.x = 0
#         root = tk.Tk()
#         root.geometry("100x100")    
#         self.count = tk.Label(root,text = self.x).pack(side = 'left')
#         plus = tk.Button(root,text = "+" ,command= self.increase).pack()
#         minus = tk.Button(root,text = "-" ,command= self.decrease).pack()
#         resets = tk.Button(root,text = "Reset" ,command= self.reset).pack()
#         root.mainloop()


# Button()

root = tk.Tk()
root.geometry("100x100") 
x = 0   
def increase():
    global x
    x += 1
def decrease():
    global x
    x -= 1
def reset():
    global x
    x = 0
count = tk.Label(root,text = x).pack(side = 'left')
plus = tk.Button(root,text = "+" ,command= increase).pack()
minus = tk.Button(root,text = "-" ,command= decrease).pack()
resets = tk.Button(root,text = "Reset" ,command= reset).pack()

root.mainloop()
import tkinter as tk
import tkinter.messagebox as ttk
root = tk.Tk()
def ustoth():
    thb = 0
    x = float(i.get())
    thb += x*30
    ttk.showinfo("USD -> THB",f"{format(x,".2f")} USD = {format(thb,".2f")} THB")
def thtous():
    usd = 0
    x = float(i.get())
    usd += x / 30
    ttk.showinfo("THB -> USD",f"{format(x,".2f")} THB = {format(usd,".2f")} USD")

i = tk.StringVar()
display = tk.Entry(root,textvariable=i).pack()
usdtothb = tk.Button(root, text = "USD -> THB",command = ustoth).pack()
thbtousd = tk.Button(root, text = "THB -> USD",command = thtous).pack()




root.mainloop()
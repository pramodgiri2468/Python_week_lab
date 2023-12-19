import tkinter as tk

def add():
    total.set(total.get() + float(entry.get()))
    entry.delete(0, tk.END)

def subtract():
    total.set(total.get() - float(entry.get()))
    entry.delete(0, tk.END)

def reset():
    total.set(0)
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Calculator")

total = tk.DoubleVar()
total.set(0)
label_total = tk.Label(text="Total:" , textvariable=total, width=10)
label_total.pack()

entry = tk.Entry(width=10)
entry.pack()

button_add = tk.Button(text="+", command=add, width=5)
button_add.pack(side=tk.LEFT)

button_subtract = tk.Button(text="-", command=subtract, width=5)
button_subtract.pack(side=tk.LEFT)

button_reset = tk.Button(text="Reset", command=reset)
button_reset.pack(side=tk.LEFT)

window.mainloop()
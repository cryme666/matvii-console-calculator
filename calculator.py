import tkinter as tk

clicks = 0
def click():
    global clicks
    clicks += 1
    print(clicks)

root = tk.Tk()

label = tk.Label(root,text="Hello world")
label1 = tk.Label(root,text="Hello world")
label2 = tk.Label(root,text="Hello world")
label.grid(row=0,column=0)
label1.grid(row=0,column=1)
label2.grid(row=1,column=1)

button = tk.Button(root,text='Click me',command=click)
button.grid(row=1,column=0)

root.mainloop()
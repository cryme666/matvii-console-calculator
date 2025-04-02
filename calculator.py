import tkinter as tk

window = tk.Tk()
window.title('Calculator')

entry = tk.Entry(window,width=50, borderwidth = 10)
entry.grid(row=0,column=0,columnspan=4)

operations = '+-*/'

buttons = [
    '1','2','3','+',
    '4','5','6','-',
    '7','8','9','*',
    '0','/','=','C'
]

def click_buttons(number):
        current = entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,current + str(number))


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))

    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(0,f"Error: {e}")
 

row,column = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(window,text=button,padx=40,pady=20,command=calculate).grid(row=row,column=column)
    elif button == 'C':
        tk.Button(window,text=button,padx=40,pady=20,command=lambda: entry.delete(0,tk.END)).grid(row=row,column=column)
    else:
        tk.Button(window,text=button,padx=40,pady=20,command= lambda num = button: click_buttons(num)).grid(row=row,column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1

tk.mainloop()

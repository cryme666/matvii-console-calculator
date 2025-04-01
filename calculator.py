import tkinter as tk

window = tk.Tk()
window.title('Calculator')

entry = tk.Entry(window,width=50, borderwidth = 10)
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    '1','2','3','+',
    '4','5','6','-',
    '7','8','9','*',
    '0','/','=','C'
]
row,column = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(window,text=button,padx=40,pady=20,command='').grid(row=row,column=column)
    elif button == 'C':
        tk.Button(window,text=button,padx=40,pady=20,command='').grid(row=row,column=column)
    else:
        tk.Button(window,text=button,padx=40,pady=20,command='').grid(row=row,column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1



tk.mainloop()
from tkinter import*
from time import*

vtn=Tk()
vtn.title("Reloj")
vtn.geometry ('250x50')
vtn.configure(background='OliveDrab1')

def clock():
    label = strftime('%H:%M:%S')
    lbl.configure(text=label)
    lbl.after(1000,clock)

lbl = Label(vtn,font=('Times', 30, 'bold'), bg='OliveDrab1', fg='black')
lbl.pack(anchor = 'cen')
clock()
vtn.mainloop()



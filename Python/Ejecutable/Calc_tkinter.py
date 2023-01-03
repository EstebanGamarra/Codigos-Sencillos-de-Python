from tkinter import*

vtn = Tk()
vtn.title("Calculadora Tkinter")
vtn.geometry ('250x200')
vtn.configure(background='black')

label_1= Label(vtn,text="N°1", bg='black', fg='white')
label_1.grid(row=1,column=1)
text_1= Entry(vtn)
text_1.grid(row=1,column=2)
label_2= Label(vtn,text="N°2", bg='black', fg='white')
label_2.grid(row=2,column=1)
text_2= Entry(vtn)
text_2.grid(row=2,column=2)

resultado=StringVar()
def suma():
    suma = int(text_1.get()) + int(text_2.get())
    return resultado.set(suma)
def resta():
    resta = int(text_1.get()) - int(text_2.get())
    return resultado.set(resta)
def multiplicacion():
    multi = int(text_1.get()) * int(text_2.get())
    return resultado.set(multi)
def division():
    divi = int(text_1.get()) / int(text_2.get())
    return resultado.set(divi)
def exit():
    vtn.destroy()

btn_suma = Button(vtn, text="+", bg='chartreuse2', fg='black', width = 11, command = suma)
btn_suma.grid(row=3,column=1)
btn_resta = Button(vtn, text="-", bg='chartreuse2', fg='black', width = 11, command = resta)
btn_resta.grid(row=3,column=2)
btn_mult = Button(vtn, text="*", bg='chartreuse2', fg='black', width = 11, command = multiplicacion)
btn_mult.grid(row=4,column=1)
btn_div = Button(vtn, text="/", bg='chartreuse2', fg='black', width = 11, command = division)
btn_div.grid(row=4,column=2)

btn_exit = Button(vtn, text="Salir", bg='maroon1', fg='black', width=30, command=exit)
btn_exit.grid(row=7,column=1, columnspan=2)

label_resultado = Label(vtn, bg="khaki1", fg='black',width='15', height='2',textvar=resultado)
label_resultado.grid(row=5, column=1,  columnspan=2)

vtn.mainloop()


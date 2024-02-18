from tkinter import *
ventana = Tk()
ventana.title("INGRESO DE DATOS PERSONALES")
ventana.geometry("600x300")

lbl1 =Label(ventana, text = "APELLIDOS")
lbl1.place(x=30, y=10, width = 100, height = 25)
lbl2 =Label(ventana, text = "NOMBRES")
lbl2.place(x=30, y= 40, width= 100, height = 25)
lbl3 =Label(ventana, text = "DIRECCION")
lbl3.place(x=30 , y= 70, width= 100, height= 25)
lbl4 =Label(ventana, text = "TELFONO")
lbl4.place(x = 30, y = 100, width = 100, height = 25)

texto1 = Text(ventana, bg = "white")
texto1.place(x= 120, y = 10, width = 200, height= 25)
texto2 = Text(ventana, bg ="white")
texto2.place(x = 120, y = 40, width = 200, height= 25)
texto3 = Text(ventana, bg = "white")
texto3.place(x = 120, y = 70, width = 200, height = 25)
texto4 = Text(ventana, bg = "white")
texto4.place(x = 120, y = 100, width = 200, height = 25)


btn1 = Button(ventana, text = "GUARDAR")
btn1.place(x = 400, y = 10, width = 120)
btn2 = Button(ventana, text = "ELIMINAR")
btn2.place(x = 400, y = 40, width = 120, height= 25)
btn3 = Button(ventana, text = "NUEVO REGISTRO")
btn3.place(x = 400, y = 70, width = 120, height= 25)
btn4 = Button(ventana, text = "SALIR")
btn4.place(x = 400, y = 100, width = 120, height= 25)



ventana.mainloop()


# CREANDO VENTANAS DE ESCRITORIO EN PYTHON
from tkinter import Tk, Label, Button
def mensaje():
    print ("mensaje del boton")

ventana = Tk()
ventana.geometry("400x280")
ventana.title("mi primera ventana")
lbl = Label(ventana, text = "este es un [label] Tkinter")
lbl.pack()
btn = Button(ventana, text = "presiona este [boton] para mensaje", command=mensaje)
btn.pack()
ventana.mainloop()
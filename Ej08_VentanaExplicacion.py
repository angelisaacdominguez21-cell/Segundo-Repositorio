#angel isaac dominguez espinoza
#3B de programacion
#cbtis 89
from tkinter import *

# Crear la ventana principal
ventana = Tk()
ventana.title("Hola mundo")
ventana.geometry("300x200")

# Crear una etiqueta (label)
etiqueta = Label(ventana, text="¡Hola mundo!")
etiqueta.pack(pady=20)

# Crear un botón para salir
boton = Button(ventana, text="Salir", command=ventana.quit)
boton.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


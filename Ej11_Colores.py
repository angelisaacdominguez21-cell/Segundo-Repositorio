#angel isaac dominguez espinoza 
#3B de programacion 
import tkinter as tk 
from tkinter import ttk

ventana = tk.Tk()
ventana.title("lista desplegablen ComboBox")
ventana.geometry("300x200")

etiqueta =tk.Label(ventana,text="Elige una opcion:")
etiqueta.pack(pady=10)

opciones = ("rojo","verde","azul","amarillo","morado")
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly" )
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion =  ComboColores.get()
    etiqueta.config(text=f"seleccionaste: {seleccion}")

ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta =tk.Label(ventana,text="aun no has seleccionado nada")
etiqueta.pack(pady=20)

ventana.mainloop()
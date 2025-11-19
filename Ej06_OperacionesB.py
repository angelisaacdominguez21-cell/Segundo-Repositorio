#angel isaac dominguez espinoza 
import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

def restar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {n1 - n2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

def multiplicar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {n1 * n2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

def dividir():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        if n2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        else:
            resultado.config(text=f"Resultado: {n1 / n2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("350x280")

# Etiquetas y entradas
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

# Botones de operaciones
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Button(ventana, text="Restar", command=restar).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=5)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=5)

# Etiqueta del resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

# 3ªB Programacion Matutino 
# Autor: Angel Isaac Dominguez Espinoza 
# Objetivo: saludar al usuario y mostrar su edad el proximo año 

nombre = input ("¿Como te llamas? ") # Pedir un dato (string)
edad = input("¿Cuantos años tienes? ")

#imput siempre devuelve texto; si necesito operar con numeros con edad 
edad = int (edad)

print() # Linea en blanco 
print("Encantado de conocherte,", nombre)
print("El año que viene tendra", edad + 1, "años.")
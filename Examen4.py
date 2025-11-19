# tabla de multiplicar 

tabla = int(input("Ingresa el número de la tabla: "))
intervalo = int(input("Ingresa el número de intervalos: "))
inicio = int(input("Ingresa el número de inicio: "))
tope = int(input("Ingresa el tope: "))

print("\nTabla de multiplicar en forma ASCENDENTE:")
for i in range(inicio, tope + 1, intervalo):
    print(f"{tabla} x {i} = {tabla * i}")

print("\nTabla de multiplicar en forma DESCENDENTE:")
for i in range(tope, inicio - 1, -intervalo):
    print(f"{tabla} x {i} = {tabla * i}")
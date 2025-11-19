


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(f"\nHola {nombre}!")

if edad >= 18:
    print("Eres mayor de edad.")
    print(f"Números que anteceden a {edad} en forma descendente:")
    for i in range(edad - 1, 0, -1):
        print(i, end=" ")
else:
    print("Eres menor de edad.")
    suma = 0
    for i in range(1, edad):
        suma += i
    print(f"La suma de los números que anteceden a {edad} es: {suma}")
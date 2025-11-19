nombre=input("Escribe tu nombre ")
edad=int(input("¿Que edad tienes? "))

if edad>=18:
    print(f"Eres mayor de edad")
    print(f"{nombre}, eres mayor de edad ({edad} años).")
    print("Números que anteceden a tu edad en orden descendente:")
    for i in range(edad,0,-1):
        print(i)

else:
    print(f"{nombre}, eres menor de edad ({edad} años).")
    suma = 0
    for i in range(edad):
        suma += i
    print(f"La suma de los números que anteceden a {edad} es: {suma}")
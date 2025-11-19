#


num=0
par=0
impar=0
nulos=0
suma=0

for i in range(0,5,1):
    num=int(input("inrese el numero; "))
    if num ==0:
        print(num,"Nulo")
        suma+=1
    elif num % 2 == 0:
        print(num," Es par")
        suma += num
        par+=1
    else:
        print(num," Es impar")
        suma += num
        impar+=1
print("La nsuma de los numeros es: ",suma)
print("Total de numos: ",nulos)
print("Total de impares: ",impar)
print("Total de pares: ",par)
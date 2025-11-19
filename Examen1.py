#por medio de un ciclo imprime la serie del 1000 al 6000 en intervalos de 500 y al sumar de todos ellos posteriormente 
# que se imprima los mismos numeros, peros en forma inversa 


inicio=1000
fin=6000
suma=0
resultado=fin
inicio1=6000
fin1=1000
suma1=0
resultado1=fin
for numero in range (inicio,fin+1,500):
    print(numero)
    suma+=numero
print("la suma total es",suma)

print("Inverso")

for numero1 in range (inicio1,fin1-1,-500):
    print(numero1)
    suma1+=numero1
print("la suma total es",suma1)
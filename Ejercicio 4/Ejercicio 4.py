#Ejercicio 1
#x=0
#while x<101:
#    print(x)
#    x+=1

#Ejercicio 2
#numeros=int(input("Ingrese el numero: "))
#numeros_1=str(abs(numeros))
#numeros_2=len(numeros_1)
#print("El numero tiene ", numeros_2 ," digitos")

#Ejercicio 3
#valor=int(input("Ingrese su primer valor: "))
#valor_2=int(input("Ingrese su segundo valor: "))
#y=0
#if valor > valor_2:
#    valor_2+=1
#    while valor > valor_2:
#        y=valor_2+y
#        valor_2+=1
#elif valor_2 > valor:
#    valor+=1
#    while valor_2 > valor:
#        y=valor+y
#        valor+=1
#
#print(y)

#Ejercicio 4
#Controlador=1
#y=0
#while Controlador==1:
#    numero=int(input("Ingrese que numero quiere sumar: "))
#    y=y+numero
#    Controlador=int(input("Numero registrado, si desea seguir sumando numeros ingrese un 1. De caso contrario ingrese un 0: "))
#print("El total de la suma es ", y)

#Ejercicio 5
#import random
#numero=random.randint(0,9)
#usuario=-1
#x=0
#while numero != usuario:
#    usuario=int(input("Intente adivinar el numero entre 0 y 9: "))
#    x=x+1
#print("Adivino en numero! Le tomo ",x," intentos adivinarlo")

#Ejercicio 6
#for x in range(100,-2,-2):
#    print(x)

#Ejercicio 7
#usuario=int(input("Ingrese un numero: "))
#x=0
#for y in range(usuario+1):
#    x+=y
#print("El total de la suma es: ", x)

#Ejercicio 8
#contador=0
#par=0
#impar=0
#positivo=0
#negativo=0
#while contador!=100:
#    numero=int(input("Ingrese un numero: "))
#    if numero % 2==0:
#        par+=1
#    else:
#        impar+=1
#    if numero >= 0:
#        positivo+=1
#    else:
#        negativo+=1
#    contador+=1
#print(f"De los ",contador," numeros ingresados,",par," son pares,",impar," son impares,",positivo," son positivos y ",negativo," son negativos.")

#Ejercicio 9
#contador=0
#x=0
#while contador!=100:
#    numero=int(input("Ingrese un numero: "))
#    x=x+numero
#    contador+=1
#    print(f"Ingreso ",contador," numeros")
#total=x/contador
#print(f"El promedio de los ",contador," es ",total, ".")

#Ejercicio 10
#numero=int(input("Ingrese un numero: "))
#numero=str(numero)
#numero_1=numero[::-1]
#print(f"El numero invertido es ",numero_1,".")
#ejercicio 1
#edad=float(input("Ingrese su edad"))
#if edad > 18:
#    print("Es mayor de edad")
#else:
#    print("Es menor de edad")

#ejercicio 2
#nota=float(input("Ingrese su nota"))
#if nota >= 6:
#    print("Aprobado")
#else:
#    print("Desaprobado")

#ejercicio 3
#numero=float(input("Ingrese su numero"))
#if numero % 2 == 0:
#    print("Ha ingresado un numero par")
#else:
#    print("Ha ingresado un numero impar")

#ejercicio 4
#edad=float(input("Ingrese su edad: "))
#print("usted pertenece a la categoria: ")
#if edad<=12:
#    print("niño")
#elif edad>12 and edad<=18:
#    print("Adolecente")
#elif edad>18 and edad<=30:
#    print("Adulto joven")
#else:
#    print("Adulto")

#ejercicio 5
#Contra=input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
#total=len(Contra)
#if total>=8 and total<=14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6
#from statistics import mode,median,mean
#import random
#numeros_aleatorios = [random.randint(1,100) for i in range (50)]
#print(f"Media: {mean(numeros_aleatorios)}")
#print(f"Mediana: {median(numeros_aleatorios)}")
#print(f"Moda: {mode(numeros_aleatorios)}")
#if mean(numeros_aleatorios) > median(numeros_aleatorios) > mode(numeros_aleatorios):
#    print("Sesgo positivo a la derecha")
#elif mean(numeros_aleatorios) < median(numeros_aleatorios) < mode(numeros_aleatorios):
#    print("Sesgo positivo a la izquierda")
#else:
#    print("Sin sesgo")

#ejercicio 7
#string=input("ingrese una palabra o frase: ")
#vocales="a","e","i","o","u","A","E","I","O","U"
#len(string)
#if string[-1] in vocales:
#    print(string + "!")
#else:
#    print(string)

#ejercicio 8
#nombre=input("Ingrese su nombre: ")
#contador=float(input("Ingrese 1 para tener su nombre en mayuscula, ingrese 2 para su nombre en minisculas o ingrese 3 para convertir la primera letra de su nombre en mayusculas: "))
#if contador == 1:
#    print(nombre.upper())
#elif contador == 2:
#    print(nombre.lower())
#elif contador == 3:
#    print(nombre.title())
#else:
#    print("No selecciono una opccion valida")

#ejercicio 9
#magnitud=float(input("Ingrese la magnitud del terremoto (Con un numero): "))
#if magnitud < 3:
#    print("Muy leve")
#elif magnitud < 4 and magnitud >=3:
#    print("Leve")
#elif magnitud < 5 and magnitud >=4:
#    print("Moderado")
#elif magnitud < 6 and magnitud >=5:
#    print("Fuerte")
#elif magnitud < 7 and magnitud >=6:
#    print("Muy fuerte")
#elif magnitud >=7:
#    print("Extremo")

#ejercicio 10
#Emisferio=input("Ingrese en que emisferio esta, Sur (S) o norte (N): ")
#mes=int(input("Ingrese que mes es (con un numero, ejemplo 5 para Mayo): "))
#dia=int(input("Ingrese que dia es (como un numero): "))
#if Emisferio == "S":
#    if (mes == 12 and dia>=21) or (mes in [1,2]) or (mes == 3 and dia<=20):
#        print("Verano")
#    if (mes == 3 and dia>=21) or (mes in [4,5]) or (mes == 6 and dia<=20):
#        print("Otoño")
#    if (mes == 6 and dia>=21) or (mes in [7,8]) or (mes == 9 and dia<=20):
#        print("Invierno")
#    if (mes == 9 and dia>=21) or (mes in [10,11]) or (mes == 12 and dia<=20):
#        print("Primavera")
#elif Emisferio == "N":
#    if (mes == 12 and dia>=21) or (mes in [1,2]) or (mes == 3 and dia<=20):
#            print("Invierno")
#    if (mes == 3 and dia>=21) or (mes in [4,5]) or (mes == 6 and dia<=20):
#            print("Primavera")
#    if (mes == 6 and dia>=21) or (mes in [7,8]) or (mes == 9 and dia<=20):
#            print("Verano")
#    if (mes == 6 and dia>=21) or (mes in [10,11]) or (mes == 12 and dia<=20):
#            print("Otoño")
#else:
#    print("Emisferio invalido")
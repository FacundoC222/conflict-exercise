#Ejrcicio 1
#def imprimir_hola_mundo():
#    print ("Hola Mundo!")

#imprimir_hola_mundo()

#Ejercicio 2
#def saludar_usuario(nombre):
#    print(f"Hola {nombre}!")

#nombre=input("Cual es tu nombre? \n")
#saludar_usuario(nombre)

#Ejercicio 3
#def  informacion_personal(nombre, apellido,edad, residencia):
#    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#a=input("Cual es su nombre? \n")
#b=input("Cual es su apellido? \n")
#c=input("Cual es su edad? \n")
#d=input("Donde vive? \n")
#informacion_personal(a,b,c,d)

#Ejercicio 4
#def calcular_perimetro_circulo(radio):
#    print (f"El perimetro del circulo es {2*3.14**radio}")
#def calcular_area_circulo(radio):
#    print (f"El area del circulo es {3.14*radio**2}")

#a=int(input("Cual es el radio del circulo?"))
#calcular_area_circulo(a)
#calcular_perimetro_circulo(a)

#Ejercicio 5
#def segundos_a_horas(segundos):
#    print(f"estos {segundos} segundos equivalen a {segundos/3600} horas")
#
#a=int(input("Ingrese la cantidad de segundos. \n"))
#segundos_a_horas(a)

#Ejercicio 6
#def tabla_multiplicar(numero):
#    mult=0
#    while mult < 11:
#        print(f"{mult} x {numero} = {mult*numero}")
#        mult=mult+1

#a=int(input("Ingrese un numero \n"))
#tabla_multiplicar(a)

#Ejercicio 7
#def operaciones_basicas(a, b):
#    suma= a+b
#    resta= a-b
#    mult= a*b
#    div= a/b
#    return (suma,resta,mult,div)

#a=(int(input("Ingrese el primer valor \n")))
#b=(int(input("Ingrese el segundo valor \n")))

#print(f"El resultado de la suma, resta, multiplicacion y divicion es: {operaciones_basicas(a,b)}") 

#Ejercicio 8
#def calcular_imc(peso, altura):
#    return (peso/altura**2)

#a=(float(input("Ingrese su peso kilos (ej: 85.6): \n")))
#b=(float(input("Ingrese su altura en metros (ej: 1.86): \n")))

#print(f"Su IMC es de {calcular_imc(a,b)}")

#Ejercicio 9
#def celsius_a_fahrenheit(celsius):
#    return ((celsius*9/5)+32)

#a=(float(input("Ingrese la temperatura en Celcius \n")))
#print(f"{a} celcius equivale a {celsius_a_fahrenheit(a)} fahrenheit")

#Ejercicio 10
#def calcular_promedio(a, b, c):
#    return((a+b+c)/3)

#a=int(input("Ingrese el primer numero. \n"))
#b=int(input("Ingrese el segundo numero. \n"))
#c=int(input("Ingrese el tercer numero. \n"))

#print(f"El promedio de los tres numeros es {calcular_promedio(a,b,c)}")
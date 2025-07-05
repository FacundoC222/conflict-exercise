# ejercicio 1
#def factorial_num(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return n * factorial_num(n-1)
    
#numero=int(input("Ingrese un numero: "))
#if numero < 1:
#    print("ingrese mayor o igual que 1")
#else:
#    print("Estos son los numeros factoriales desde 1 hasta", numero, ":")
#    for i in range (1, numero + 1):
#        print(i, "=", factorial_num(i) )

#ejercicio 2
#def fibo_rec(n):
#    if n==0:
#        return 0
#    elif n==1:
#        return 1
#    else:
#        return fibo_rec(n-1) + fibo_rec(n-2)
    
#numero=int(input("Ingrese un numero: "))
#if numero < 0:
#    print("ingrese un numero entero y postivo")
#else:
#    print("Este es el orden de los numeros de la Serie de Fibonacci hasta", numero, ":")
#    for i in range (numero + 1):
#        print("La posicion ",i, "corresponde al numero: ",fibo_rec(i))

#Ejericicio 3
#def pot_rec(base, exponente):
#    if exponente == 0:
#        return 1
#    else:
#        return base * pot_rec(base, exponente-1)
    
#base=float(input("Ingrese la base: "))
#exponente=int(input("Ingrese el exponente (solo enteros): "))
#if exponente<0:
#    print("No se permiten exponentes negativos")
#else:
#    resultado= pot_rec(base,exponente)
#    print(f"resultado:  {base} elevado a {exponente} = {resultado}")
#    print("progression: ")
#    for expo in range(exponente+1):
#        print(f"{base}**{expo} = {pot_rec(base, expo)}")

#Ejercicio 4
#def bin (numero, list_bin=None):
#    if list_bin is None:
#        list_bin=[]
#    
#    if numero == 0:
#        return list_bin[::-1]
#    else:
#        list_bin.append(numero%2)
#        return bin(numero//2,list_bin)

#numero=int(input("Ingrese un numero entero: "))
#binario=bin(numero)
#print("El numero ingresado en binario es: ")
#print("" .join(map(str, binario)))

#Ejercicio 5
#def es_palindromo(palabra):
#    if len(palabra)<=1:
#        return True
#    if palabra[0] != palabra[-1]:
#        return False
#    return es_palindromo(palabra[1:-1])

#palabra=input("ingrese una palabra ")
#if es_palindromo(palabra) is True:
#    print("La palabra es un palindromo")
#else:
#    print("La palabra no es un palindromo")

#Ejercicio 6
#def suma_digitos(n):
#    if n <= 9:
#        return n
#    else:
#        return (n%10)+suma_digitos(n//10)
    
#numero=int(input("Ingrese un numero entero positivo: "))
#print("La suma de los digitos del numero es ", suma_digitos(numero))

#ejercicio 7
#def contar_bloques(n):
#    if n == 1:
#        return n
#    else:
#        return n + contar_bloques(n-1)
    
#cant_bloques=int(input("Cuantos bloques de altura tiene la piramide? "))
#print("se utilizaron ",contar_bloques(cant_bloques), " bloques")

#Ejercicio 8
#def contar_digito(numero, digito):
#    if numero == 0:
#        return 0
#    ult_digito=numero%10
#    if ult_digito == digito:
#        return 1 + contar_digito(numero // 10,digito)
#    else:
#        return contar_digito(numero // 10,digito)
    
#numero=int(input("Ingrese un numero entero: "))
#digito=int(input("Que digito quiere contar? "))
#print(f"el digito {digito} se repite {contar_digito(numero, digito)} veces")
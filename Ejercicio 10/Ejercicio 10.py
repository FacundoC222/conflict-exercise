#Ejercicio 1
#def factorial_numero(num):
#    if num==0 or num==1:
#        return 1
#    else:
#        return num*factorial_numero(num-1)
    
#numero=int(input("Ingrese un numero: "))
#print(f"El numero recursivo de {numero} es {factorial_numero(numero)}")

#Ejercicio 2
#def fibonacci (num):
#    if num == 0:
#        return 0
#    elif num == 1:
#        return 1
#    else:
#        return fibonacci(num-1)+fibonacci(num-2)
    
#pos=int(input("Ingrese la pocicion que desea ver de la serie de Fibonacci: "))
#for i in range(pos + 1):
#    print(fibonacci(i), end=" ")

#Ejercicio 3
#def expo (x,y):
#    if y==0:
#        return 1
#    elif y==1:
#        return base
#    else:
#        return x*x**(y-1)

#base=int(input("Ingrese la base: "))
#expon=int(input("Ingrese el exponente: "))
#print (f"El resultado es {expo(base,expon)}")

#Ejercicio 4
#def binario(x):
#    if x == 0:
#        return"0"
#    elif x == 1:
#        return"1"
#    else:
#        return binario(x//2) + str(x%2)
    
#numero=int(input("Ingrese el numero que desea transformar a bininario: "))
#print(f"El numero {numero} en binario es {binario(numero)}")

#Ejercicio 5
#def palindromo(x):
#    if len(x) <= 1:
#        return True
#    else:
#        if x[0]==x[-1]:
#            return palindromo(x[1:-1])
#        else:
#            return False
        
#palabra=str(input("Ingrese una palabra: "))
#print (f"la palabra es un palindromo? {palindromo(palabra)}")

#Ejercicio 6
#def sum_dig(x):
#    if x<10:
#        return x
#    else:
#        return (x%10) + sum_dig(x//10)
    
#num=int(input("Ingrese un numero: "))
#print(f"La suma de todos los digitos es {sum_dig(num)}")

#Ejercicio 7
#def contar_bloques(n):
#    if n == 1:
#        return 1
#    else:
#        return n + contar_bloques(n-1)
    
#bloq_tot=int(input("Ingrese la cantidad de bloques que se encuentran en la base: "))
#print (f"El total de bloques utilizados para la piramide es de {contar_bloques(bloq_tot)}")

#Ejercicio 8
#def contar_digito(numero, digito):
#    if not (0 <= digito <= 9):
#        return 0
#    if numero == 0:
#        return 1 if digito == 0 else 0
#    else:
#        ultimo_digito=numero%10
#        conteo=1 if ultimo_digito == digito else 0
#        return conteo + contar_digito(numero // 10, digito)
    
#num1=int(input("Ingrese un numero: "))
#num2=int(input("Ingrese que digito quiere buscar en el numero anteriror: "))
#print(f"El numero {num2} aparece {contar_digito(num1,num2)} veces")
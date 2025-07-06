#ejercicio 1
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#precios_frutas["naranja"] = 1200
#precios_frutas["Manzana"] = 1500
#precios_frutas["Pera"] = 2300
#print(precios_frutas)

#ejercicio 2
#precios_frutas={'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450, 'naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
#precios_frutas["Banana"] = 1330
#precios_frutas["Manzana"] = 1700
#precios_frutas["Melon"] = 2800
#print(precios_frutas)

#ejercicio 3
#precios_frutas={'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450, 'naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
#lista_frutas= list(precios_frutas.keys())
#print(lista_frutas)

#ejercicio 4

#def menu_inicial():
#    print("--------------------------------------------")
#    print("Bienvenido a sus contactos, que desea hacer?")
#    print("[1]        Agendar nuevo contacto           ")
#    print("[2]     Consultar numero de contacto        ")
#    print("[3]                Salir                    ")
#    print("--------------------------------------------")
#    opccion=int(input(""))
#    if opccion == 1:
#        agendar()
#    elif opccion == 2:
#        consultar()
#    elif opccion == 3:
#        print("Que tenga un buen dia.")
#    else:
#        print("--------------------------------------------")
#        print("no elegio una opccion correcta.")
#        menu_inicial()

#def agendar():
#    print("--------------------------------------------")
#    nombre=str(input("Ingrese el nombre de contacto: "))
#    numero=str(input("Ingrese el numero de contacto: "))
#    print("--------------------------------------------")
#    print(f"Ingreso {nombre} con el numero {numero} , es eso correcto?")
#    print("--------------------------------------------")
#    print("[Y]/[N]")
#   validador=str(input(""))
#   if validador == "Y":
#       lista_contactos[nombre]=numero
#        print("Contacto agregado con exito!")
#        menu_inicial()
#    elif validador == "N":
#        print("ingrese nuevamente los datos")
#        nombre=str(input("Ingrese el nombre de contacto: "))
#        numero=str(input("Ingrese el numero de contacto: "))
#        print("--------------------------------------------")
#        print(f"Ingreso {nombre} con el numero {numero} , es eso correcto?")
#        print("--------------------------------------------")
#        print("[Y]/[N]")
#        validador=str(input(""))
#        while validador == "N":
#            print("ingrese nuevamente los datos")
#            nombre=str(input("Ingrese el nombre de contacto: "))
#            numero=str(input("Ingrese el numero de contacto: "))
#            print("--------------------------------------------")
#            print(f"Ingreso {nombre} con el numero {numero} , es eso correcto?")
#            print("--------------------------------------------")
#            print("[Y]/[N]")
#            validador=str(input(""))
#        lista_contactos[nombre]=numero
#        print("Contacto agregado con exito!")
#        menu_inicial()
#    else:
#        print("No ingreso una opccion valida")
#        menu_inicial()

#def consultar():
#    busqueda=str(input("Ingrese el nombre del contacto que desea buscar: "))
#    numero_cel=lista_contactos.get(busqueda)
#    if numero_cel is not None:
#        print("--------------------------------------------")
#        print (f"El numero de telefono de {busqueda} es {numero_cel}.")
#        menu_inicial()
#    else:
#        print("--------------------------------------------")
#        print(f"el contacto que usted busca ({busqueda}) no existe.")
#        menu_inicial()
    
#lista_contactos={}
#menu_inicial()

#Ejercicio 5
#frase=input("Ingrese una frase: ")
#palabras=frase.split()
#palabras_unicas=set(palabras)
#recuento={}
#for palabra in palabras:
#    if palabra in recuento:
#        recuento[palabra]+=1
#    else:
#        recuento[palabra]=1

#Ejercicio 6
#alumnos={}

#for i in range(3):
#    nombre=input(f"Ingrese el nombre del alumno {i+1}: ")
#    notas=[]
#    for j in range(3):
#        nota=float(input(f"Ingrese la nota {j+1} para {nombre}: "))
#        notas.append(nota)
#    alumnos[nombre]=tuple(notas)

#print("\nPromedios de los alumnos:")
#for nombre, notas in alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"{nombre}: Notas = {notas} - Promedio = {promedio:.2f}")

#ejercicio 7
#print("Ingrese los nombres de estudiantes que aprobaron el primer parcial (separados por comas):")
#aprobados_p1 = set(input().split(','))
#print("\nIngrese los nombres de estudiantes que aprobaron el segundo parcial (separados por comas):")
#aprobados_p2 = set(input().split(','))
#ambos_parciales = aprobados_p1 & aprobados_p2
#solo_un_parcial = aprobados_p1 ^ aprobados_p2
#total_aprobados = aprobados_p1 | aprobados_p2
#print("\nEstudiantes que aprobaron ambos parciales:", ambos_parciales)
#print("Estudiantes que aprobaron solo un parcial:", solo_un_parcial)
#print("Total de estudiantes que aprobaron al menos un parcial:", total_aprobados)

#ejercicio 8
#Productos={
#    "carton":5,
#    "metal":10,
#    "madera":20
#}

#def menu():
#    print("     menu de stock   ")
#    print("[1]  ver productos   ")
#    print("[2] modificar stock  ")
#    opccion=input("")
#    if opccion=="1":
#        ver_productos()
#    elif opccion=="2":
#        modificar_productos()

#def ver_productos():
#    print (Productos)
#    print ("-----------------------------------")
#    menu ()

#def modificar_productos():
#    producto=input("Ingrese el producto: ")
#    cantidad=input("Ingrese la nueva cantidad del producto: ")
#    Productos[producto]=cantidad
#    print("cambio realizado")
#    print(Productos)
#    menu()
#menu()

#ejercicio 9
#agenda={
#    ("lunes","10:00"): "Reunion", 
#    ("martes","15:00"): "Clase de ingles"
#}

#dia=input("Ingrese el dia: ")
#hora=input("ingrese la hora (xx:xx): ")
#evento = agenda.get((dia, hora), "No hay eventos programados")
#print(f"Evento: {evento}")

#ejercicio 10
#original = {
#    "Argentina": "Buenos Aires",
#    "Chile": "Santiago",
#}
#invertido = {capital: pais for pais, capital in original.items()}
#print("Diccionario invertido:", invertido)
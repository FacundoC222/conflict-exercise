lista=[]

def busqueda_secuencial(lista, palabra):
    for i, objeto in enumerate(lista):
        if objeto == palabra:
            return i
    return -1

def busqueda_binaria(lista, palabra):
    lista_ord=sorted(lista)
    izquierda=0
    derecha = len(lista_ord)-1
    while izquierda <= derecha:
        medio=(izquierda+derecha)//2
        if lista_ord[medio] == palabra:
            return medio
        elif lista_ord[medio] < palabra:
            izquierda=medio+1
        else:
            derecha=medio-1
    return-1

def ing_datos():
    switch="Y"
    while switch=="Y":
        print("------------------------------------------------")
        print(f"Ingrese el dato que quiere agregar a la lista, actualmente hay {len(lista)} datos en la lista.")
        dato=input("")
        lista.append(dato)
        print("Dato añadido con exito, desea seguir añadiendo mas? [Y]/[N]")
        switch=input("")
    menu()    

def enc_datos():
    print("------------------------------------------------")
    print("Que dato desea encontrar?")
    dato=input("")
    print("------------------------------------------------")
    print("Desea acomardar la lista? [Y]/[N]")
    opccion=input("")
    if opccion == "N":
        print("------------------------------------------------")
        print("Solo se podra realizar una busqueda de tipo secuencial, desea continuar? [Y]/[N]")
        afirmacion=input("")
        if afirmacion == "Y":
            print("------------------------------------------------")
            print(busqueda_secuencial(lista,dato))
            menu()
        elif afirmacion == "N":
            menu()
    elif opccion == "Y":
        print("------------------------------------------------")
        print("Lista ordenada con exito, que metodo quiere utilizar para buscar su dato?")
        print("[1] Secuencial")
        print("[2] Binario")
        afirmacion=input("")
        if afirmacion == "1":
            lista_2=sorted(lista)
            print(busqueda_secuencial(lista_2,dato))
            menu()
        elif afirmacion == "2":
            lista_2=sorted(lista)
            print("------------------------------------------------")
            if busqueda_binaria (lista_2,dato) != -1:
                print (f"La ubicacion dentro de la lista es {busqueda_binaria(lista_2,dato)}")
            else:
                print("No se encontro la palabra dentro de la lista")
            menu()
    else:
        print("No eligio una opccion valida")
        enc_datos()

def ver_datos():
    print("------------------------------------------------")
    print(lista)
    menu()

def menu():
    print("------------------------------------------------")
    print("Bienvenido, elija que opccion quiere seleccionar")
    print("[1]        Ingresar datos a la lista            ")
    print("[2]        Encontrar dato especifico            ")
    print("[3]            Visualizar lista                 ")
    print("[4]                  Salir                      ")
    opccion=int(input(""))
    if opccion== 1:
        ing_datos()
    elif opccion== 2:
        enc_datos()
    elif opccion== 3:
        ver_datos()
    elif opccion== 4:
        print("------------------------------------------------")
        print("Que tenga un buen dia")
    else:
        print("------------------------------------------------")    
        print("No eligio una opccion valida")
        menu()

menu()
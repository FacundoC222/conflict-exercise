#Ejercicio 1
#notas=[9,5,6,10,8,7,3,2,1,4]
#contador=0
#total=0
#val_alto=0
#val_bajo=1

#while contador<10:
#    print(notas[contador])
#    contador+=1
#contador=0
#while contador<10:
#    nota=notas[contador]
#    total=total+nota
#    contador+=1
#promedio=total/10
#print(f"El promedio es {promedio}")
#contador=0
#while contador<10:
#    valor=notas[contador]
#    if val_alto < valor:
#        val_alto=valor
#    if val_bajo > valor:
#        val_bajo=valor
#    contador+=1
#print(f"La nota mas alta es {val_alto} y la mas baja es {val_bajo}.")


#Ejercicio 2
#lista_prod=[]
#for i in range(5):
#    producto=input(f"Ingrese el producto {i+1} : ")
#    lista_prod.append(producto)

#lista_prod_ord = sorted(lista_prod)
#print(f"Lista ordenada {lista_prod_ord}")
#eliminar_prod=input("Ingrese que producto desea eliminar: ")
#lista_prod_ord.remove(eliminar_prod)
#print(f"Lista ordenada {lista_prod_ord}")

#Ejercicio 3
#import random
#contador=0
#lista_num=[]
#num_par=[]
#num_imp=[]
#while contador<15:
#    numero=random.randint(1,100)
#    lista_num.append(numero)
#    contador+=1
#contador=0
#while contador<15:
#    numero=lista_num[contador]
#    if numero%2==0:
#        num_par.append(numero)
#    else:
#        num_imp.append(numero)
#    contador+=1
#print(f"Los numeros pares son {num_par} y los numeros impares son {num_imp}.")

#Ejercicio 4
#datos = [1,3,5,3,7,1,9,5,3]
#datos_fin=[]
#contador=0
#while contador<8:
#    valor=datos[contador]
#    if valor in datos_fin:
#        pass    
#    else:
#        datos_fin.append(valor)
#    contador+=1
#print(f"Lista sin valores repetidos {datos_fin}")

#Ejercicio 5
#lista=["carlos","julian","lucas","mateo","tomas","agustin","hernan","maximo"]
#accion=input("Si desea agregar un numbre ingrese 1 , si desea eliminar un nombre ingrese 2 : ")
#if accion=="1":
#    agregar=input("Ingrese el nombre que quiere agregar: ")
#    lista.append(agregar)
#    print(f"Lista actualizada {lista}")
#elif accion=="2":
#    eliminar=input(f"Ingrese el nombre a eliminar ({lista})")
#    lista.remove(eliminar)
#    print(f"Lista actualizada {lista}")
#else:
#    print("No ingreso una opccion correcta")

#Ejercicio 6
#lista=[1,2,3,4,5,6,7]
#lista_inv=[lista[-1]] + lista[:-1]
#print(lista_inv)

#Ejercicio 7
#temp_semana=[[2,15],[3,17],[5,22],[10,20],[5,14],[1,8],[0,6]]
#promedio_temp=[]
#contador=0
#amplitud_max=-1
#dia=0
#while contador<7:
#    numero= temp_semana[contador][0]+temp_semana[contador][1]
#    promedio=numero / 2
#    promedio_temp.append(promedio)
#    amplitud= temp_semana[contador][1]-temp_semana[contador][0]
#    if amplitud>amplitud_max:
#        amplitud_max=amplitud
#        dia=contador+1
#    contador+=1
#print(f"El promedio de temperatura es {promedio_temp}, el dia con mas amplitud termica fue el {dia} con una amplitud de {amplitud_max}")

#Ejercicio 8
#notas=[[5,7,10],[9,4,8],[0,5,6],[10,9,8],[9,4,7]]
#promedios=[]
#notas_materias=[]
#contador=0
#while contador<5:
#    promedio=(notas[contador][0]+notas[contador][1]+notas[contador][2])/2
#    promedios.append(promedio)
#    contador+=1
#for i in range (3):
#    promedio_mat=(notas[0][i]+notas[1][i]+notas[2][i]+notas[3][i]+notas[4][i])/5
#    notas_materias.append(promedio_mat)
#print(f"El promedio de cada estudiante es {promedios} y el promedio de cada materia es {notas_materias}")

#Ejercicio 9
#fila_uno =[["-"],["-"],["-"]]
#fila_dos =[["-"],["-"],["-"]]
#fila_tres=[["-"],["-"],["-"]]
#turno="x"
#activo=True
#while activo==True:
#    if turno=="x":
#        print("turno del jugador X")
#        fila=input("ingrese en que fila desea jugar (1,2,3)")
#        columna=input("Y en cual columna quiere colocar su X (1,2,3)")
#        if fila=="1":
#            if columna=="1":
#                fila_uno[0]="X"
#            elif columna=="2":
#                fila_uno[1]="X"
#            elif columna=="3":
#                fila_uno[2]="X"
#        elif fila=="2":
#            if columna=="1":
#                fila_dos[0]="X"
#            elif columna=="2":
#                fila_dos[1]="X"
#            elif columna=="3":
#                fila_dos[2]="X"
#        elif fila=="3":
#            if columna=="1":
#                fila_tres[0]="X"
#            elif columna=="2":
#                fila_tres[1]="X"
#            elif columna=="3":
#                fila_tres[2]="X"
#        print(f"Movimiento realizado, estado actual del tablero\n{fila_uno}\n{fila_dos}\n{fila_tres}")
#        turno="o"
#    elif turno=="o":
#        print("turno del jugador O")
#        fila=input("ingrese en que fila desea jugar (1,2,3)")
#        columna=input("Y en cual columna quiere colocar su O (1,2,3)")
#        if fila=="1":
#            if columna=="1":
#                fila_uno[0]="O"
#            elif columna=="2":
#                fila_uno[1]="O"
#            elif columna=="3":
#                fila_uno[2]="O"
#        elif fila=="2":
#            if columna=="1":
#                fila_dos[0]="O"
#            elif columna=="2":
#                fila_dos[1]="O"
#            elif columna=="3":
#                fila_dos[2]="O"
#        elif fila=="3":
#            if columna=="1":
#                fila_tres[0]="O"
#            elif columna=="2":
#                fila_tres[1]="O"
#                fila_tres[2]="O"
#        print(f"Movimiento realizado, estado actual del tablero\n{fila_uno}\n{fila_dos}\n{fila_tres}")
#        turno="x"

#Ejercicio 10
#lista=[[10,50,84,6,30,7,48],[26,54,78,99,84,56,37],[77,64,52,35,94,77,49],[55,68,42,38,44,5,30]]
#mas_vend=[]
#vent_dia=[0]*7
#cont=0
#alto=0
#for i in range(4):
#    suma=0
#    for y in range(7):
#        suma+=lista[i][y]
#    mas_vend.append(suma)
#for y in range(7):
#    for i in range (4):
#        vent_dia[y]+=lista[i][y]
#while cont<4:
#    if alto<mas_vend[cont]:
#        alto=cont
#    cont+=1
#print(f"El total vendido de cada producto es {mas_vend}, el dia con mayores ventas fue el {vent_dia.index(max(vent_dia))+1} y el producto mas vendido fue el {alto}")
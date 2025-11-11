#Funcion encargada de revisar si existe el archivo .CSV
def comprobar_CSV():
    try: 
        with open("paises.csv","r") as archivo:
            pass
    except FileNotFoundError:
            with open("paises.csv","w") as archivo:
                archivo.write("nombre,poblacion,superficie,continente\n")
#Funcion encargada de agregar paises al archivo
def agregar_pais():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
    nombre_pais = input("---------------------\nIngrese el nombre del nuevo pais: ").strip()
    if not nombre_pais:
        print("---------------------\nEl nombre del pais no puede estar vacio")
        return 
    for linea in lineas[1:]:
        datos = linea.strip().split(",")
        if len(datos) >= 1 and datos[0].strip().lower() == nombre_pais.lower():
            print(f"---------------------\nYa existe un pais con el nombre: {datos[0].strip()}")
            return
    try:
        poblacion_str = input("Ingrese la poblacion del pais: ").strip()
        poblacion = int(poblacion_str)
        if poblacion < 0:
            print("---------------------\nLa poblacion no puede ser negativa")
            return
    except ValueError:
        print("---------------------\nLa poblacion debe ser un numero entero valido")
        return
    try:
        superficie_str = input("Ingrese la superficie del pais (km): ").strip()
        superficie = int(superficie_str)
        if superficie < 0:
            print("---------------------\nLa superficie no puede ser negativa")
            return
    except ValueError:
        print("---------------------\nLa superficie debe ser un numero valido")
        return
    nombre_continente = input("Ingrese el continente del pais: ").strip()
    if not nombre_continente:
        print("---------------------\nEl nombre del continente no puede estar vacio")
        return   
    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]
    if nombre_continente.lower() not in continentes_validos:
        print("---------------------\nContinente no valido")
        print("Continentes válidos: America, Europa, Asia, Africa, Oceania, Antartida")
        return
    with open("paises.csv", "a") as archivo:
        archivo.write(f"{nombre_pais},{poblacion},{superficie},{nombre_continente}\n")

    print(f"---------------------\nPais agregado exitosamente.\nNombre: {nombre_pais}\nPoblacion: {poblacion}\nSuperficie: {superficie} km\nContinente: {nombre_continente}")  
#Menu de opcciones para las funciones de actualziar datos
def actualizar_datos():
    print("---------------------\nQue dato quiere actualizar?\n1.Poblacion\n2.Superficie\n3.Volver al menu anterior")
    eleccion=input()
    match eleccion:
        case "1":
            actualizar_poblacion()
        case "2":
            actualizar_superficie()
        case "3":
            print("---------------------\nVolviendo al menu anterior")
#Funcion encargada de actualizar la poblacion
def actualizar_poblacion():
    lineas_actualizadas = []
    encontrado = False
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()     
    if len(lineas) <= 1:
        print("---------------------\nEl archivo esta vacio")
        return
    pais_buscado = input("---------------------\nIngrese el nombre del pais a buscar: ").strip()
    if not pais_buscado:
        print("---------------------\nError: Debe ingresar un nombre de pais")
        return
    for i, linea in enumerate(lineas):
        datos_originales = linea  
        datos = linea.strip().split(",")
        if i == 0:
            lineas_actualizadas.append(linea)
            continue
        if len(datos) < 4:
            lineas_actualizadas.append(datos_originales)
            continue    
        nombre_pais = datos[0].strip()
        if nombre_pais.lower() == pais_buscado.lower():
            encontrado = True    
            print(f"---------------------\nPais encontrado {nombre_pais}, ingrese la nueva poblacion:")
            while True:
                nueva_poblacion = input().strip()   
                if not nueva_poblacion:
                    print("---------------------\nLa poblacion no puede estar vacia")
                    continue                    
                if not nueva_poblacion.isdigit():
                    print("---------------------\nLa poblacion debe ser un numero entero")
                    continue
                if int(nueva_poblacion) <= 0:
                    print("---------------------\nLa poblacion debe ser un numero positivo")
                    continue
                break
            datos[1] = nueva_poblacion
            nueva_linea = ",".join(datos) + "\n"
            lineas_actualizadas.append(nueva_linea)                
            print(f"---------------------\nSe actualizo la poblacion de {nombre_pais}, actualmente es {nueva_poblacion}")            
        else:
            lineas_actualizadas.append(datos_originales)
        if encontrado:
            with open("paises.csv", "w") as archivo:
                archivo.writelines(lineas_actualizadas)
        else:
            print(f"---------------------\nNo se encontro el pais {pais_buscado}")
#Funcion encargada de actualizar la superficie
def actualizar_superficie():
        lineas_actualizadas = []
        encontrado = False
        with open("paises.csv", "r") as archivo:
            lineas = archivo.readlines()
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return
        pais_buscado = input("---------------------\nIngrese el nombre del pais a buscar: ").strip()
        if not pais_buscado:
            print("---------------------\nError: Debe ingresar un nombre de pais")
            return
        for i, linea in enumerate(lineas):
            if i == 0:
                lineas_actualizadas.append(linea)
                continue
            datos = linea.strip().split(",")
            if len(datos) < 4:
                lineas_actualizadas.append(linea) 
                continue
            if datos[0].strip().lower() == pais_buscado.lower():
                encontrado = True
                print(f"---------------------\nPais encontrado: {datos[0]}")
                print(f"Superficie actual: {datos[2]} ")    
                nueva_superficie = input("Ingrese la nueva superficie: ").strip()
                if not nueva_superficie.replace('.', '').isdigit():
                    print("Error: La superficie debe ser un numero valido")
                    return
                datos[2] = nueva_superficie
                nueva_linea = ",".join(datos) + "\n"
                lineas_actualizadas.append(nueva_linea)
                print("Superficie actualizada")    
            else:
                lineas_actualizadas.append(linea)
        if encontrado:
            with open("paises.csv", "w") as archivo:
                archivo.writelines(lineas_actualizadas)
        else:
            print(f"El pais {pais_buscado} no fue encontrado")
#Menu de opcciones para las funciones de busqueda
def menu_busqueda():
    print("---------------------\nQue desea realizar?\n1.Buscar por nombre\n2.Filtrar por poblacion\n3.Filtrar por superficie\n4.Filtrar por continente\n5.Volver al menu anterior")
    eleccion=input()
    match eleccion:
        case "1":
            busqueda_nombre()
        case "2":
            busqueda_rango_poblacion()
        case "3":
            busqueda_rango_territorio()
        case "4":
            busqueda_continente()
        case "5":
            print("---------------------\nVolviendo al menu anterior")
        case _:
            print("---------------------\nNo elegio una opccion correcta")
#Funcion encargada de buscar paises por nombre
def busqueda_nombre():
    nombre_buscado = input("---------------------\nIngrese el nombre del pais que quiere buscar: ").strip()    
    if not nombre_buscado:
        print("---------------------\nError: Debe ingresar un nombre de pais")
        return
    encontrado = False
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return
        for linea in lineas[1:]:
            datos = linea.strip().split(",")    
            if len(datos) >= 4 and datos[0].strip().lower() == nombre_buscado.lower():
                encontrado = True
                print(f"Se encontro el pais: {datos[0].strip().upper()}\nPoblacion: {datos[1].strip()}\nSuperficie: {datos[2].strip()} km\nContinente: {datos[3].strip()}")
        if not encontrado:
            print(f"---------------------\nEl pais {nombre_buscado} no fue encontrado")   
#Funcion encargada de buscar paises por el rango de su poblacion
def busqueda_rango_poblacion():
    min_poblacion = input("---------------------\nIngrese la poblacion minima: ").strip()
    max_poblacion = input("---------------------\nIngrese la poblacion maxima: ").strip()    
    if not min_poblacion or not max_poblacion:
        print("---------------------\nError: Debe ingresar ambos valores del rango")
        return
    min_poblacion = int(min_poblacion)
    max_poblacion = int(max_poblacion)    
    if min_poblacion < 0 or max_poblacion < 0:
        print("---------------------\nError: La poblacion no puede ser negativa")
        return
    if min_poblacion > max_poblacion:
        print("---------------------\nError: El valor minimo no puede ser mayor al maximo")
        return
    encontrados = False
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return
        print(f"\nPaises con poblacion entre {min_poblacion} y {max_poblacion}:")
        for linea in lineas[1:]:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                poblacion_actual = int(datos[1].strip())
                if min_poblacion <= poblacion_actual <= max_poblacion:
                    encontrados = True
                    print(f"---------------------\n{datos[0].strip()}\nPoblacion: {datos[1].strip()}\nSuperficie: {datos[2].strip()} km\nContinente: {datos[3].strip()}")      
        if not encontrados:
            print(f"---------------------\nNo se encontraron paises en ese rango de poblacion")
#Funcion encargada de buscar paises por el rango de su territorio
def busqueda_rango_territorio():
    min_territorio = input("---------------------\nIngrese el territorio minimo: ").strip()
    max_territorio = input("---------------------\nIngrese el territorio maximo: ").strip()    
    if not min_territorio or not max_territorio:
        print("---------------------\nError: Debe ingresar ambos valores del rango")
        return
    min_territorio = float(min_territorio)
    max_territorio = float(max_territorio)
    if min_territorio < 0 or max_territorio < 0:
        print("---------------------\nError: El territorio no puede ser negativo")
        return 
    if min_territorio > max_territorio:
        print("---------------------\nError: El valor minimo no puede ser mayor al maximo")
        return
    encontrados = False
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return
        print(f"---------------------\nPaises con territorio entre {min_territorio} km y {max_territorio} km:")
        for linea in lineas[1:]:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                territorio_actual = float(datos[2].strip())
                if min_territorio <= territorio_actual <= max_territorio:
                    encontrados = True  
                    print(f"---------------------\n{datos[0].strip()}\nPoblacion: {datos[1].strip()}\nSuperficie: {datos[2].strip()} km\nContinente: {datos[3].strip()}")       
        if not encontrados:
            print(f"No se encontraron paises en ese rango de territorio")
#Funcion encargada de buscar paises por su continente
def busqueda_continente():
    continente_buscado = input("---------------------\nIngrese el nombre del continente: ").strip().lower()
    if not continente_buscado:
        print("---------------------\nError: Debe ingresar un nombre de continente")
        return
    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]    
    if continente_buscado.lower() not in continentes_validos:
        print("---------------------\nError: Continente no valido")
        print("Continentes validos: America, Europa, Asia, Africa, Oceania, Antartida")
        return
    encontrados = False
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return
        print(f"---------------------\nPaises del continente {continente_buscado.title()}:")
        for linea in lineas[1:]:
            datos = linea.strip().split(",")    
            if len(datos) >= 4:
                continente_actual = datos[3].strip().lower()
                continente_buscado_lower = continente_buscado.lower()               
                if continente_actual == continente_buscado_lower:
                    encontrados = True
                    print(f"---------------------\n{datos[0].strip()}\nPoblacion: {datos[1].strip()}\nSuperficie: {datos[2].strip()} km\nContinente: {datos[3].strip()}")       
        if not encontrados:
            print(f"No se encontraron paises en el continente {continente_buscado}")
#Menu de opcciones para las funciones de estadistica
def menu_estadistica():
    print("---------------------\nQue desea realizar?\n1.Pais con mayor y menor poblacion\n2.Promedio de poblacion\n3.Promedio de superficie\n4.Cantidad de paises por continente\n5.Volver al menu anterior")
    eleccion=input()
    match eleccion:
        case "1":
            mayor_menor_poblacion()
        case "2":
            promedio_poblacion()
        case "3":
            promedio_territorio()
        case "4":
            paises_por_continentes()
        case "5":
            print("---------------------\nVolviendo al menu anterior")
        case _:
            print("---------------------\nNo elegio una opccion correcta")    
#Funcion encargada de mostrar el pais con menor y mayor poblacion
def mayor_menor_poblacion():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()    
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return    
        mayor_poblacion = None
        menor_poblacion = None    
        for linea in lineas[1:]:
            datos = linea.strip().split(",")        
            if len(datos) >= 4:
                poblacion_actual = int(datos[1].strip())        
                if mayor_poblacion is None or poblacion_actual > mayor_poblacion[1]:
                    mayor_poblacion = (datos[0].strip(), poblacion_actual, datos[2].strip(), datos[3].strip())        
                if menor_poblacion is None or poblacion_actual < menor_poblacion[1]:
                    menor_poblacion = (datos[0].strip(), poblacion_actual, datos[2].strip(), datos[3].strip())            
            print("---------------------\nPais con mayor poblacion:")
            if mayor_poblacion:
                print(f"{mayor_poblacion[0]}\nPoblacion: {mayor_poblacion[1]}\nSuperficie: {mayor_poblacion[2]} km\nContinente: {mayor_poblacion[3]}")
            else:
                print("No se pudo determinar")
            print("---------------------\nPais con menor poblacion:")
            if menor_poblacion:
                print(f"{menor_poblacion[0]}\nPoblacion: {menor_poblacion[1]}\nSuperficie: {menor_poblacion[2]} km\nContinente: {menor_poblacion[3]}")
            else:
                print("---------------------\nNo se pudo determinar")    
#Funcion encargada de mostrar el promedio de poblacion de todos los paises
def promedio_poblacion():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()     
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return    
        total_poblacion = 0
        total_paises = 0    
        for linea in lineas[1:]:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                poblacion = int(datos[1].strip())
                total_poblacion += poblacion
                total_paises += 1
        if total_paises > 0:
            promedio = total_poblacion / total_paises
            print(f"---------------------\nPromedio de poblacion: {promedio} ")
        else:
            print("---------------------\nNo se pudo calcular el promedio")    
#Funcion encargada de promediar el terrioriorio de todos los paises
def promedio_territorio():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()    
        if len(lineas) <= 1:
            print("---------------------\nEl archivo esta vacio")
            return   
        total_superficie = 0
        total_paises = 0   
        for linea in lineas[1:]:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                superficie = float(datos[2].strip())
                total_superficie += superficie
                total_paises += 1           
        if total_paises > 0:
            promedio = total_superficie / total_paises
            print(f"---------------------\nPromedio de superficie: {promedio} km")
        else:
            print("---------------------\nNo se pudo calcular el promedio")    
#Funcion encargada de mostrar la cantidad de paises por continente
def paises_por_continentes():
    with open("paises.csv", "r") as archivo:
        lineas = archivo.readlines()    
        if len(lineas) <= 1:
            print("El archivo esta vacio")
            return            
        continentes = {}    
        for linea in lineas[1:]:
            datos = linea.strip().split(",")
            if len(datos) >= 4:
                continente = datos[3].strip()
                if continente not in continentes:
                    continentes[continente] = 0
                continentes[continente] += 1
        print("Cantidad de paises por continente:")
        for continente, cantidad in continentes.items():
            print(f"{continente}: {cantidad} paises")
        total_paises = sum(continentes.values())
        print(f"\nTotal de paises: {total_paises}")
#Menu principal encargado de mostrar todas las opcciones
def main():
    comprobar_CSV()
    activo=True
    while activo==True:
        print("---------------------\nBienvenido, que desea realizar?\n1.Agregar nuevo pais\n2.Actualizar datos\n3.Buscar o filtrar paises\n4.Buscar estadisticas\n5.Salir del programa")
        eleccion=input()
        match eleccion:
            case "1":
                agregar_pais()
            case "2":
                actualizar_datos()
            case "3":
                menu_busqueda()
            case "4":
                menu_estadistica()
            case "5":
                print("---------------------\nFinalizando ejecucion, que tenga un buen dia")
                activo=False
            case _:
                print("---------------------\nElija una opccion correcta")

main()

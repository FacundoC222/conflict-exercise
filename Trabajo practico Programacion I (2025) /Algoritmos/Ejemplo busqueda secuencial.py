comestibles=[
    "manzana", "banana", "naranja", "pera", "uva",
    "sandía", "melón", "frutilla", "arándano", "durazno",
    "papa", "zanahoria", "cebolla", "tomate", "lechuga",
    "brócoli", "espinaca", "ajo", "calabaza", "batata",
    "churrasco", "entraña", "tapa de asado", "bife de chorizo", "costilla",
    "pollo", "pavo", "cerdo", "cordero", "conejo",
    "empanada", "pizza", "hamburguesa", "hot dog", "taco",
    "sushi", "pasta", "lasaña", "paella", "risotto",
    "pan", "galleta", "torta", "factura", "medialuna",
    "helado", "chocolate", "flan", "budín", "yogur"
]

def busqueda_secuencial(lista, palabra):
    for i, objeto in enumerate(lista):
        if objeto == palabra:
            return i
    return -1

def entrada():
    busqueda=input("Ingrese la palabra a buscar: ")
    lugar = busqueda_secuencial(comestibles, busqueda)
    if lugar != -1:
        print(f"El elemento {busqueda} se encontro en la posicion {lugar}")
    else:
       print ("No se encontro el elemento")

entrada()



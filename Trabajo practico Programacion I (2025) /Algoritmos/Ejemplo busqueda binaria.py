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

def entrada():
    busqueda=input("Ingrese la palabra para conocer su ubicacion dentro de la lista: ")
    if busqueda_binaria (comestibles,busqueda) != -1:
        print (f"La ubicacion dentro de la lista es {busqueda_binaria(comestibles,busqueda)}")
    else:
        print("No se encontro la palabra dentro de la lista")

entrada()

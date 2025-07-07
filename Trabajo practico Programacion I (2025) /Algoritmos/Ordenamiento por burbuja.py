lista=[1,5,9,4,8,6,2,7,3]

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista

print(ordenamiento_burbuja(lista))
lista=[1,5,9,4,8,6,2,7,3]

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        elemento_actual = lista[i]
        j = i - 1 
        while j >= 0 and elemento_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento_actual
    return lista

print(ordenamiento_insercion(lista))
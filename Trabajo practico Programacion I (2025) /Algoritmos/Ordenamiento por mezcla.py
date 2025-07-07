lista=[1,5,9,4,8,6,2,7,3]

def separar_juntar(lista):
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = separar_juntar(izquierda)
    derecha = separar_juntar(derecha)
    return acomodar(izquierda, derecha)

def acomodar(izquierda, derecha):
    resultado = []
    i = j = 0  
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

print(separar_juntar(lista))

def buscar_producto():
    exixte=False
    producto_buscado=input("ingrese el producto que desea buscar: ").strip()
    with open("Productos.txt", "r") as archivo:
        for linea in archivo:
            datos=linea.strip().split(",")
            producto=datos[0]
            precio=datos[1]
            cantidad=datos[2]
            if producto.lower() == producto_buscado.lower():
                print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")
                exixte=True
            else:
                print("No se encontro el producto")

def guardar():
    productos=[]
    with open("Productos.txt", "r") as archivo:
        for linea in archivo:
            datos=linea.strip().split(",")
            productos.append(datos)
    
    with open("Productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto[0]},{producto[1]},{producto[2]}\n")

with open("Productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,385,18\n")
    archivo.write("Lapiz,50,100\n")
    archivo.write("Goma,75,25\n")

with open("Productos.txt","r") as archivo:
    for linea in archivo:
        datos=linea.strip().split(",")
        producto=datos[0]
        precio=datos[1]
        cantidad=datos[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

with open("Productos.txt","a") as archivo:
    nuevo_item=input("Ingrese un nuevo producto:")
    nuevo_item2=input("Ingrese el valor del producto:")
    nuevo_item3=input("Ingrese la cantidad del producto:")
    archivo.write(f"{nuevo_item},{nuevo_item2},{nuevo_item3}\n")

with open("Productos.txt","r") as archivo:
    for linea in archivo:
        datos=linea.strip().split(",")
        producto=datos[0]
        precio=datos[1]
        cantidad=datos[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

buscar_producto()

guardar()
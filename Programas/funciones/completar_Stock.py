# Si estoy ejecutando el programa desde este archivo, importa la función desde la misma carpeta.
# Si estoy ejecutando desde otro archivo, por estar modularizando, importo desde carpeta funciones.
if __name__ == '__main__':
    from corroborar_Naturales import corroborar
else:
    from funciones.corroborar_Naturales import corroborar


def funStock(cod, lstCods, lstCant, lstCantMin, lstCantMax):
    '''
    Pide por teclado cantidad mínima, cantidad máxima, y cantidad actual de los productos,
    los corrobora y los agrega, junto a código de producto, a sus correspondientes listas.

    Parametros: cod = Codigo de producto; lstCods = lista de Códigos de Producto;
    lista de cantidad mínima; lista de cantidad máxima; y lista de cantidad actual.


    '''

    # Defino la variable 'texto' y 'texto2' ya que los textos son muy extensos como para colocarlos
    # directamente como parametro.

    # Pide stock mínimo y corrobora que sea mayor o igual que 0.
    texto = "\nIngrese la cantidad mínima de stock que quiere para su producto: "
    texto2 = "Error. El stock mínimo debe ser mayor o igual a cero."
    stockMin = corroborar(texto, texto2)


    # Pide stock máximo y corrobora que sea mayor o igual que stock mínimo.
    texto = "\nIngrese la cantidad máxima de stock que quiere para su producto: "
    texto2 = "Error. La cantidad máxima debe ser mayor o igual a la cantidad mínima de stock."
    stockMax = corroborar(texto, texto2, stockMin)


    # Pide stock actual y corrobora que sea mayor o igual que 0 y menor o igual que stock máximo.
    texto = "\nIngrese el stock actual de su producto: "
    texto2 = "Error. El stock debe ser mayor o igual a 0 y menor o igual al stock máximo."
    # Dentro de la función se va a pedir por teclado 'stock actual' y corroborar que 'stock actual >= 0'.
    stockProducto = corroborar(texto, texto2)
    # Dentro del ciclo while se va a corroborar que 'stock actual <= stock maximo'.
    while stockProducto > stockMax:
        print(texto2)
        # Si no cumplió la condición de ser menor o igual que stock máximo, vuelve a pedir
        # por teclado y corroborar 'stock actual >= 0'.
        stockProducto = corroborar(texto, texto2)


    # Una vez ingresados correctamente todos los stocks, imprime mensaje exitoso.
    print("\nCódigo de producto y Stocks agregados correctamente.")

    # Agrega esos stocks y el codigo de producto a sus correspondientes listas.
    lstCods.append(cod)
    lstCant.append(stockProducto)
    lstCantMin.append(stockMin)
    lstCantMax.append(stockMax)




def main():

    codigo = input("Ingrese un código: ")

    lstCodProd = []
    lstStock = []
    lstStockMin = []
    lstStockMax = []

    funStock(codigo, lstCodProd, lstStock, lstStockMin, lstStockMax)

    print(f"\nLa lista de codigos de producto es: {lstCodProd}"
          f"\nLa lista de stock actual es: {lstStock}"
          f"\nLa lista de stock minimos es: {lstStockMin}"
          f"\nLa lista de stock maximos es: {lstStockMax}")


if __name__ == '__main__':
    main()

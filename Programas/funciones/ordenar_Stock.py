def ordenarStock(lstCodProd, lstStock, lstStockMin):
    '''
    Muestra los productos y su cantidad en stock que se encuentran por debajo del stock mínimo, ordenado por
    stock mínimo.

    Parametros: Recibe tres listas.
    Devuelve: Tres listas ordenadas en base a la lista principal (tercer lista ingresada por parametros).


    '''

    # Crea listas nuevas para no modificar las originales.
    lstCodProd2 = []
    lstStock2 = []
    lstStockMin2 = []


    # Guarda en una lista los índices de los productos que se encuentran con Stock Actual por debajo del Stock Mínimo.
    lstFaltantes = [i for i in range(len(lstStock)) if lstStock[i] < lstStockMin[i]]


    # Agrega a las listas nuevas, los elementos que se encuentran en los índices guardados en 'lista faltantes'.
    for i in range(len(lstFaltantes)):
        # Agrego el elemento que se encuentra en el índice almacenado en la lista de faltantes.
        lstCodProd2.append(lstCodProd[lstFaltantes[i]])
        lstStock2.append(lstStock[lstFaltantes[i]])
        lstStockMin2.append(lstStockMin[lstFaltantes[i]])

    # Ordeno las tres listas en simultaneo por metodo de burbujeo mejorado.
    ordenado = False
    recorrido = 1
    # Si se recorre la lista con ciclo for y no está ordenada en algún índice, se vuelve a iterar
    # el ciclo while y se vuelve a repetir el mismo proceso hasta que la lista quede ordenada.
    while ordenado == False:
        ordenado = True
        for i in range(len(lstStockMin2) - recorrido):
            if lstStockMin2[i] > lstStockMin2[i + 1]:
                aux = lstStockMin2[i]
                lstStockMin2[i] = lstStockMin2[i + 1]
                lstStockMin2[i + 1] = aux

                aux = lstStock2[i]
                lstStock2[i] = lstStock2[i + 1]
                lstStock2[i + 1] = aux

                aux = lstCodProd2[i]
                lstCodProd2[i] = lstCodProd2[i + 1]
                lstCodProd2[i + 1] = aux

                # Si recorre la lista y no está ordenada, devuelve falso para seguir iterando ciclo while.
                ordenado = False

        # Suma uno al recorrido, para no volver a ordenar sobre la misma posición que ya está ordenada.
        recorrido += 1



    # Devuelve las tres listas ordenadas.
    return lstCodProd2, lstStock2, lstStockMin2




def main():


    lstCodProd = ['VSA14', 'BDS10', 'ZCA30', 'AFS42', 'GSD41', 'DFAS1', 'GDD40', 'KDF30', 'ASF30']
    lstStock = [43, 53, 57, 875, 121, 34, 2, 4, 75]
    lstStockMin = [50, 79, 64, 100, 150, 20, 10, 10, 105]

    # Llamo a la funcion y almaceno en tres variables las tres listas ordenadas.
    lst1ord, lst2ord, lst3ord = ordenarStock(lstCodProd, lstStock, lstStockMin)

    # Printeo índice por índice de los faltantes de todas las listas -reducidas- en forma de tabla.
    print("\n{:<15} {:<15} {:<15}".format('Producto:', 'Stock Mín.:', 'Stock Actual:'))
    for i in range(len(lst3ord)):
        print("{:>7} {:>14} {:>16}".format(lst1ord[i], lst3ord[i], lst2ord[i]))


if __name__ == '__main__':
    main()

def eliminarCodigo(lista, lista2, lista3, lista4):
    '''
    Pide un código y lo elimina junto a los elementos correspondientes de las listas relacionadas.
    Parametros: Recibe cuatro listas relacionadas.

    '''

    # Pide código por teclado.
    cod = input("\nIngrese el código de producto que desea eliminar "
                "ó -1 para regresar al menú de opciones: ").upper()

    # Si el código es distinto de -1:
    if cod != '-1':

        # Si el código ingresado no se encuentra en la lista:
        if cod not in lista:
            print("\nEl código ingresado NO se encuentra en la lista.")

        else:
            # Si el código ingresado está en la lista:
            while cod in lista:
                # Almacena en qué indice de la lista está ese código.
                i = lista.index(cod)
                # Elimina el elemento en ese índice de la lista principal y de sus relacionadas.
                del lista[i]
                del lista2[i]
                del lista3[i]
                del lista4[i]
                print("\nCódigo y stocks eliminados correctamente.")


    # Si se ingresó -1:
    else: print("\nSe ingresó -1. NO se ha eliminado ningún producto.")


def main():

    lstCodProd = ['VSA14', 'BDS10', 'ZCA30', 'AFS42', 'GSD41', 'DFAS1', 'GDD40', 'KDF30', 'ASF30']
    lstStock = [43, 53, 57, 875, 121, 34, 2, 4, 75]
    lstStockMin = [50, 79, 64, 100, 150, 20, 10, 10, 105]
    lstStockMax = [70, 100, 80, 200, 300, 30, 40, 20, 500]

    eliminarCodigo(lstCodProd, lstStock, lstStockMin, lstStockMax)

    for i in range(len(lstCodProd)):
        print(lstCodProd[i], lstStock[i], lstStockMin[i], lstStockMax[i])

if __name__ == '__main__':
    main()

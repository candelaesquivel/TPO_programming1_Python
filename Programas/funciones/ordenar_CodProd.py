def ordenarCodProd(lista1, lista2):
    '''
    Ordena dos listas simultaneas.

    Parametros: Recibe dos listas.
    Devuelve: Las dos listas ordenadas.

    '''


    # Creo una copia de la lista1.
    lst1ord = lista1[:]
    # Para la lista2 vamos a insertarle los elementos ordenados, por lo tanto no necesito copiarla.
    lst2ord = []
    # Ordeno solo la copia de mi lista1, que es la que voy a usar para comparar los nuevos índices.
    lst1ord.sort()


    # La listas originales ('lista1' y 'lista2') solo se van a utilizar para leer los índices de sus elementos.
    # lst1ord (lista principal) == lista1 ordenada.
    # lst2ord (lista secundaria) == lista2 ordenada.


    # Recorro mi lista principal (ordenada).
    for i in range(len(lst1ord)):
        # 'cod' almacena elemento a elemento de lst1ord.
        cod = lst1ord[i]
        # 'cambiarCod' busca en la lista sin ordenar y almacena el índice en el que se encontraba dicho elemento
        # antes de ser ordenado.
        cambiarCod = lista1.index(cod)
        # Ya teniendo el índice en el que se encontraba el elemento antes de ser ordenado, busco el elemento de lista2
        # que corresponde a ese índice y lo inserto en la nueva lista, quedando la 'lst2ord' ordenada de
        # igual manera que lst1ord.
        lst2ord.append(lista2[cambiarCod])


    # Retorno las dos listas ordenadas ya que las originales no fueron modificadas.
    return lst1ord, lst2ord




def main():

    # Creo dos listas para poder corroborar.
    lstCodProd = ['VSA14', 'BDS10', 'ZCA30', 'AFS42', 'GSD41', 'DFAS1', 'GDD40', 'KDF30', 'ASF30']
    lstStock = [43, 53, 57, 875, 121, 34, 2, 4, 75]

    # Llamo a la funcion y guardo en dos variables las dos listas ordenadas.
    lst1ord, lst2ord = ordenarCodProd(lstCodProd, lstStock)

    # Printeo índice por índice de todos los productos y sus Stocks Actuales en forma de tabla.
    print("\n{:<15} {:<15}".format('Producto:', 'Stock Actual:'))
    for i in range(len(lst1ord)):
        print("{:>7} {:>14}".format
              (lst1ord[i], lst2ord[i]))


if __name__ == '__main__':
    main()


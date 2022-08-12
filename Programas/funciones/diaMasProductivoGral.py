def DiaMasProductivoGral(matriz):
    '''
    Busca la columna con mayor resultado de suma.

    Parametros: Matriz.
    Devuelve: Maximo y en que columna se encuentra.

    '''

    filas = len(matriz)
    columnas = len(matriz[0])

    lstSumas = []
    for c in range(columnas):
        suma=sum([fila[c] for fila in matriz])
        lstSumas.append(suma)

    maximo = max(lstSumas)
    listamaximo=[c for c in range (columnas) if lstSumas[c] == maximo]

    return maximo, listamaximo


def main():
    matriz = [
        [3, 5, 53],
        [3, 5, 53],
        [3, 5, 53]
    ]

    maximo, i = DiaMasProductivoGral(matriz)
    print(f"el maximo es: {maximo} que se encuentra en el indice: {i}")

if __name__ == '__main__':
    main()
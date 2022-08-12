def DiaMasProd(matriz):
    '''
    Busca el máximo y en que fila se encuentra.
    Parametros: Matriz.
    Devuelve: máximo y en que fila se encuentra.

    '''
    
    maximo = 0
    for f in range(len(matriz)):
        n = max(matriz[f])
        if n > maximo:
            maximo = n
            
    filamaximo=[]
    
    filamaximo=[f for f in range(len(matriz)) for c in range (len(matriz[0])) if matriz[f][c] == maximo ]
       
    return maximo, filamaximo



def main():
    matriz = [
        [1, 53, 26],
        [25, 5, 53],
        [1, 53, 1]
    ]

    maximo, filas = DiaMasProd(matriz)

    print(f"la/s fila/s que mas suma es: {filas} que produjo {maximo}")


if __name__ == '__main__':
    main()
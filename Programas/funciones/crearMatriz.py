from random import randint as azar

numeroazar= lambda a,b : azar(a,b)

def CrearMatriz(filas, columnas,a=0,b=150):
    '''
    Crea una matriz con valores aleatorios entre A y B, de N filas y N columnas.
    Parametros: filas = cantidad de filas; columnas = cantidad de columnas; a y b valores desde y hasta
    para generar aleatorios.
    Retorna: Matriz.

    '''

    # lista por comprension donde se generará la matriz y tenemos dos ciclos for,
    # uno indica las filas y el otro las columnas.
    matriz = [[numeroazar(a,b) for c in range(columnas)] for i in range(filas)]

    # Devuelve la matriz armada.
    return matriz



def main():
    # PROGRAMA PRINCIPAL solo para probar la función, por ese motivo las entradas
    # no poseen sus correspondientes corroboraciones.

    f = int(input("Ingrese la cantidad de filas para la matriz: "))

    c = int(input("\nIngrese la cantidad de columnas para la matriz: "))

    print("\nSe ingresarán los valores desde y hasta con los que se desea rellenar la matriz al azar.")
    a = int(input("\nIngrese el valor desde: "))
    b = int(input("\nIngrese el valor hasta (mayor que desde): "))

    matriz = CrearMatriz(f, c,a ,b)

    print("\nLa matriz es:\n")
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            print("%5d" %matriz[f][c],end="")
        print()

if __name__ == '__main__':
    main()

def CrearNombresPlantas(filas):
    '''
    Crea una lista con los nombres de las plantas.
    Parametros: Cantidad de filas.
    Devuelve: Lista con los nombres de las plantas.

    '''

    listaplantas = []
    for i in range(filas):
        strPlanta = 'Planta '
        # pedimos el nombre de la planta. Si es una cadena vacia me manda error y me pide nuevamente el nombre.
        nombre = input("Ingrese el nombre de la planta (se le agregará el prefijo 'Planta' automáticamente): ")
        while not len(nombre):
            print("Error. No puede ingresar un dato vacío.")
            nombre = input("Ingrese el nombre de la planta (se le agregará el prefijo 'Planta' automáticamente): ")

        nombre= strPlanta +nombre
        listaplantas.append(nombre)


    return listaplantas



def main():

    f = int(input("Ingrese cantidad de filas: "))

    lstPlantas = CrearNombresPlantas(f)

    print(f"Los nombres de las plantas son: {lstPlantas}")


if __name__ == '__main__':
    main()

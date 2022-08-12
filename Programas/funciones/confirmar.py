def confirmeIngreso():
    '''
    Verifica si se desea agregar un código por posibles errores de tipeo.

    Devuelve: Valor corroborado de la verificación ('Y' si desea agregar, 'N' si no desea agregar).

    '''

    x = input("\nEstá seguro que desea agregar? Presione 'Y' para agregar el código "
              "ó 'N' para no agregarlo: ").lower()
    while x != 'y' and x != 'n':
        print("Error.")
        x = input("Está seguro que desea agregar? Presione 'Y' para agregar el código "
                  "ó 'N' para no agregarlo: ").lower()

    return x

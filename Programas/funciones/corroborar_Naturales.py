def corroborar(texto, texto2, num=0):
    '''
    Corrobora que las entradas sean números naturales, y que sean mayores o iguales a otra variable.

    Parametros: texto = texto que se va a insertar en el input; texto2 = texto con mensaje de
    error e info de los parametros que debe cumplir dicho ingreso; num = variable a la que deben
    ser mayores o iguales los números ingresados por teclado (0 por omisión).
    Devuelve: número ingresado por teclado ya corroborado y en enteros.

    '''

    # La variable correcto va a cambiar su valor a 'True' solo si el dato ingresado es un número natural.
    correcto = False
    while not correcto:
        # Pide ingreso por teclado.
        x = input(texto)
        # Corrobora que sean solo números naturales.
        y = x.isdigit()
        # Mientras no sea un número natural, vuelve a pedir por teclado y vuelve a corroborar hasta que lo sea.
        while not y:
            print("Error. Solo se pueden ingresar números naturales.")
            x = input(texto)
            y = x.isdigit()

        # Una vez ingresado un número natural, convierte a entero para comparar con otros parametros en enteros.
        x = int(x)
        # Si el número es correcto, cambia el valor de la variable 'correcto' para finalizar el ciclo.
        if x >= num:
            correcto = True
        # Si no es correcto, imprime mensaje y vuelve a repetir el ciclo.
        else:
            print(texto2)

    # Retorna el número, en enteros, ingresado por teclado que cumplió con todos los pasos anteriores.
    return x

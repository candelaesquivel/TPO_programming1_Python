from funciones.completar_Stock import *
from funciones.ordenar_CodProd import ordenarCodProd
from funciones.ordenar_Stock import ordenarStock
from funciones.confirmar import confirmeIngreso
from funciones.eliminarCodigo import eliminarCodigo


def corroborarCodigo(cod, lstCodProd, lstStock, lstStockMin, lstStockMax):
    '''
    Corrobora que el código de producto sea de 4 o 5 dígitos.
    Si es correcto, llama a la función de stocks para agregar a listas.

    Parametros: Codigos de producto, lista de códigos de producto, tres listas de stock (max, min, actual).
    Devuelve: y = Almacena el valor de True o False para finalizar un ciclo por fuera de la función.
    autorizar = almacena si se desea o no guardar el código ingresado.

    '''


    # Si devuelve 'n' no seguirá con el resto del código (en VENDER o FABRICAR).
    autorizar = 'n'

    # Si el código de producto es de 4 o 5 dígitos.
    if len(cod) == 4 or len(cod) == 5:

        # Si el código de producto no se encuentra en la lista, pide sus stocks y los agrega a las listas.
        if cod not in lstCodProd:
            # Llama a la función para confirmar si realmente se desea ingresar ese código.
            autorizar = confirmeIngreso()
            # Si se desea agregar ese código:
            if autorizar == 'y':
                # Llama a la función de stocks para agregar stocks y código de producto a listas.
                funStock(cod, lstCodProd, lstStock, lstStockMin, lstStockMax)
                # Devuelve 'True' para finalizar el ciclo (en VENDER o FABRICAR).
                y = True

            # Si no se desea agregar ese código:
            else:
                print("\nEl código NO fue agregado.")
                # Devuelve 'False' para que se repita el ciclo y se pueda ingresar otro código.
                y = False


        # Si el código ya se encuentra en la lista:
        else:
            # Imprime mensaje.
            print("\nEl código de producto ya está asociado.")
            # Autorizar lo define por 'y' (para poder seguir adelante en VENDER y FABRICAR)
            autorizar = 'y'
            # Devuelve 'True' para finalizar el ciclo (en VENDER y FABRICAR).
            y = True


    # (solo para VENDER y FABRICAR) Si se ingresa -1 deja de pedir código de producto.
    elif cod == '-1':
        # Devuelve 'True' para que finalice la iteración (deja de pedir cods en VENDER y FABRICAR).
        y = True


    # Si el código de producto se ingresa incorrectamente, imprime mensaje de error.
    else:
        print("\nEl código de producto debe tener 4 o 5 dígitos.")
        # Almacena 'False' para que se pida nuevamente el cod (VENDER y FABRICAR).
        y = False

    # Para vender y fabricar.
    return y, autorizar




def funcMostrarStock(lstCodProd, lstStock):
    '''
    Muestra por pantalla el stock actual de todos los productos en forma de tabla.

    Parametros: lista de códigos y lista de stock actual.

    '''

    # Ordena por código de producto y almacena en dos variables las dos listas ordenadas.
    lst1ord, lst2ord = ordenarCodProd(lstCodProd, lstStock)

    # Si la lst1ord tiene elementos:
    if len(lst1ord):
        # Imprime códigos de producto en forma ascendente con su correspondiente stock actual.
        print("\n{:>45} {:>20}".format('Producto:', 'Stock Actual:'))
        for i in range(len(lst1ord)):
            print("{:>43} {:>16}".format
                  (lst1ord[i], lst2ord[i]))

    # Si no tiene elementos:
    else:
        print("\nEl sistema no posee productos ingresados.")




def modificarStock(accion, lstStock, cant, codigo, i, lstStockMax, lstCodProd):
    '''
    Calcula las cantidades solicitadas con respecto a los stocks.
    Si no excede limites de stock, realiza las modificaciones.

    Parametros: accion = vender o fabricar; listado de stock, stock max y códigos; cantidad a modificar;
    índice de stock que se desea modificar; último código ingresado por teclado.
    Devuelve: y = Almacena el valor de True o False para finalizar un ciclo por fuera de la función.

    '''

    # La variable 'y' va a retornar verdadero solo si la cantidad ingresada logró modificar el stock.
    y = False
    # Si la acción es vender:
    if accion == 'v':

        # Si hay menos stock que cantidad solicitada, imprime mensaje de venta no realizada.
        if lstStock[i] - cant < 0:
            print(f"\nVenta no realizada por stock insuficiente."
                  f"\nEl stock actual de {codigo} es de {lstStock[i]} unidades.")

        # Si el stock alcanza correctamente, imprime la venta y modifica el stock.
        else:
            lstStock[i] -= cant
            print(f"\nVenta realizada con éxito.")
            # Muestra códigos y stock hasta el momento.
            funcMostrarStock(lstCodProd, lstStock)
            y = True

    # Si la acción es fabricar:
    else:

        # Si la cantidad fabricada hace que el stock actual supere el stock máximo, imprime mensaje de error.
        if lstStock[i] + cant > lstStockMax[i]:
            print(f"\nStock NO modificado por stock máximo superado."
                  f"\nEl stock actual de {codigo} es de: {lstStock[i]} unidades."
                  f"\nEl stock máximo de {codigo} es de: {lstStockMax[i]} unidades.")

        # Si la cantidad fabricada no hace superar el stock máximo, modifica el stock e imprime la fabricación.
        else:
            lstStock[i] += cant
            print("\nStock agregado con éxito.")
            # Muestra códigos y stock hasta el momento.
            funcMostrarStock(lstCodProd, lstStock)
            y = True

    # Si el stock se modificó correctamente, la variable 'y' vuelve como 'True' y finaliza el ciclo.
    # En caso de que no se haya modificado por exceder límites de stock, retorna 'False' y se repite el ciclo.
    return y




def consultarStock(lstCods, lstCant):
    '''
    Pide ingresar un código de producto por teclado e informa cuál es su stock actual.

    Parametros: lista de codigos de producto y lista de stock.

    '''

    # Pide un código de producto.
    cod = input("\nIngrese un código de producto: ").upper()

    # Si el código está en la lista:
    if cod in lstCods:
        # Busca su índice.
        i = lstCods.index(cod)
        # Imprime el índice de ese código y su correspondiente cantidad.
        print(f"\nEl stock actual del producto '{lstCods[i]}' es de: {lstCant[i]} unidades.")

    # Si el código no está en la lista:
    else: print("\nEl código de producto ingresado NO se encuentra en la lista.")



#PROGRAMA PRINCIPAL
def main ():

    print("\n\n{:^100}\n{:^105}".format("¡BIENVENIDO A CELULARG®!",
                                        "EMPRESA LÍDER EN CELULARES DE ALTA GAMA\n\n\n"))


    # Crea listas de Código de Productos; Stock Actual; Stock Mínimo; y Stock Máximo.
    lstCodProd = []
    lstStock = []
    lstStockMin = []
    lstStockMax = []


    print("{:^105}".format("¡Comenzaremos ingresando el stock inicial! \n\n"))
    # Solicita código de producto por teclado (-1 para no ingresar e ir al menu de opciones).

    codigo = input("Ingrese un código de producto ó -1 para no ingresar ningún "
                   "código e ir al menu de opciones: ").upper()
    # Termina el ciclo ingresando -1 en el código de producto.
    while codigo != "-1":
        # Corrobora los códigos y llama a las funciones de stock para agregarlos a las listas.
        corroborarCodigo(codigo, lstCodProd, lstStock, lstStockMin, lstStockMax)
        # Muestra el listado de productos y sus cantidades para que el usuario no tenga que
        # acordarse que productos se van ingresando.
        funcMostrarStock(lstCodProd, lstStock)
        # Solicita código nuevamente (-1 para finalizar e ir al menu de opciones).
        codigo = input("\nIngrese un código de producto ó -1 para finalizar e ir al menu de opciones: ").upper()

    # Si no se ingresó ningún producto:
    if len(lstCodProd) == 0:
        print("\nNo se ingresó ningún producto.")

    # Si se ingresaron productos, imprime cuantos se ingresaron.
    else:
        print(f"\nSe ingresaron {len(lstCodProd)} productos.")


    # Imprime menu de opciones y solicita que función desea realizar.
    print("\n\n{:^105}".format("CELULARG®: EMPRESA LÍDER EN CELULARES DE ALTA GAMA."))
    print(
        "\n**MENU DE OPCIONES**"
        "\n1. VENDER o FABRICAR."
        "\n2. Mostrar PRODUCTOS y su STOCK ACTUAL."
        "\n3. Mostrar PRODUCTOS que se encuentran por debajo del Stock Mínimo."
        "\n4. Mostrar STOCK ACTUAL de PRODUCTO seleccionado."
        "\n5. Eliminar CÓDIGO DE PRODUCTO y sus STOCKS correspondientes."
        "\n6. Salir."
    )
    sel = input("Ingrese que función desea realizar: ")
    print()


    # SALIR == '6'
    while sel != '6':


        # VENDER o FABRICAR.
        if sel == '1':

            # Cambia el valor a 'True' solo si se ingresa correctamente un código de producto ó -1.
            agregado = False
            while not agregado:
                # Muestra códigos y stock hasta el momento.
                funcMostrarStock(lstCodProd, lstStock)
                # Solicita un código de producto y lo convierte a mayusculas.
                codigo = input("\nIngrese un código de producto (-1 si desea volver al menu de opciones): ").upper()
                # Una vez ingresado correctamente un código de producto, finaliza el ciclo.
                agregado, autorizar = corroborarCodigo(codigo, lstCodProd, lstStock, lstStockMin, lstStockMax)


            # Si el código ingresado desea ser modificado:
            if autorizar == 'y':

                # Almacena el índice del código recién ingresado.
                i = lstCodProd.index(codigo)


                # Pide por teclado la acción de fabricar o vender. Si es incorrecto,
                # vuelve a pedir hasta que sea correcto.
                accion = input("\nIngrese 'F' si desea fabricar, ingrese 'V' "
                               "si desea vender ó -1 para volver al menu de opciones: ").lower()
                while accion != 'f' and accion != 'v' and accion != '-1':
                    accion = input("Error. Ingrese 'F' si desea fabricar, ingrese 'V' "
                                   "si desea vender ó -1 para volver al menu de opciones: ").lower()

                if accion != '-1':
                    # La variable 'correcto' va a cambiar su valor a 'True' solo si se realizan correctamente
                    # las modificaciones de stock, y de esa manera terminará el ciclo.
                    correcto = False
                    while not correcto:
                        # Pide por teclado y corrobora la cantidad a fabricar/vender.
                        texto = "\nIngrese la cantidad de productos que desea modificar del stock ('0' para no hacer cambios): "
                        texto2 = "Error. El valor debe ser mayor o igual a cero."
                        cant = corroborar(texto, texto2)

                        # Si se ingresa 0, finaliza el ciclo sin modificar stocks.
                        if cant == 0:
                            print("\nNo se han realizado modificaciones en el stock.")
                            correcto = True

                        # Si se ingresa una cantidad en números naturales:
                        else:
                            # Realiza las modificaciones de stock. Si el stock NO se modifica porque
                            # la cantidad ingresada excede el stock maximo en fabricación,
                            # ó cant < 0 en ventas, la variable 'correcto' almacenará el valor de 'False'
                            # y se repetirá el ciclo.
                            correcto = modificarStock(accion, lstStock, cant, codigo, i, lstStockMax, lstCodProd)

                # Si la acción es -1:
                else:
                    print("\nNo se han realizado modificaciones en el stock.")


        # Mostrar PRODUCTOS y su STOCK ACTUAL.
        elif sel == '2':

            funcMostrarStock(lstCodProd, lstStock)


        # Mostrar PRODUCTOS que se encuentran por debajo del Stock Mínimo.
        elif sel == '3':

            # Crea una lista con los productos que estan por debajo del stock mínimo.
            lst1ord, lst2ord, lst3ord = ordenarStock(lstCodProd, lstStock, lstStockMin)

            # Si hay elementos por debajo del stock mínimo:
            if len(lst1ord):
                # Imprime los productos que se encuentran por debajo del stock mínimo, ordenado por stock mínimo.
                print("\n{:>35} {:>20} {:>20}".format('Producto:', 'Stock Mín.:', 'Stock Actual:'))
                for i in range(len(lst3ord)):
                    print("{:>32} {:>18} {:>18}".format(lst1ord[i], lst3ord[i], lst2ord[i]))

            # Si no hay elementos en la lista:
            else:
                print("\nNo hay productos que se encuentren por debajo del stock mínimo.")


        # Mostrar STOCK ACTUAL de PRODUCTO seleccionado.
        elif sel == '4':

            # Imprime el stock actual de un producto seleccionado.
            consultarStock(lstCodProd, lstStock)

        elif sel == '5':

            # Muestra códigos y stock hasta el momento.
            funcMostrarStock(lstCodProd, lstStock)
            # Elimina código de producto y sus stocks.
            eliminarCodigo(lstCodProd, lstStock, lstStockMin, lstStockMax)
            # Muestra nuevamente códigos y stock hasta el momento.
            funcMostrarStock(lstCodProd, lstStock)

        # Si la selección fue incorrecta, imprime error.
        else:
            print("\nError.  Debe ingresar un número del 1 al 5.")



        # Pide selección nuevamente.
        print("\n\n{:^105}".format("CELULARG®: EMPRESA LÍDER EN CELULARES DE ALTA GAMA."))
        print(
            "\n**MENU DE OPCIONES**"
            "\n1. VENDER o FABRICAR."
            "\n2. Mostrar PRODUCTOS y su STOCK ACTUAL."
            "\n3. Mostrar PRODUCTOS que se encuentran por debajo del Stock Mínimo."
            "\n4. Mostrar STOCK ACTUAL de PRODUCTO seleccionado."
            "\n5. Eliminar CÓDIGO DE PRODUCTO y sus STOCKS correspondientes."
            "\n6. Salir."
        )
        sel = input("Ingrese que función desea realizar: ")
        print()



    # Cuando se desea finalizar el programa, imprime mensaje.
    print("{:^100}".format("¡HASTA LUEGO!"))


if __name__ == '__main__':
    main()

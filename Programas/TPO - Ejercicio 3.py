# TPO PROGRAMACION 1 - TP3 EJERCICIO 4)
# Una fabrica de biciletas guarda en una matriz la cantidad de unidades producidas en cada uno de sus plantas durante una
# semana y cada fila representan a una de sus fabricas, se solicita:
# a)Crear una matriz con los datos creados al azar de N fábricas durante la semana. Considerando que la capacidad
# máxima de fabricación es de 150 unidades.
# b)Mostrar la cantidad total de bicicletas fabricadas por cada fabrica
# c)Cual es la fabrica que mas produjo en un solo dia (detallar dia y fabrica)
# d)Cual es el dia mas productivo, considerando todas las fabricas combinadas
# e)Crear una lista por comprension que tenga la menor cantidad fabricada por cada fabrica


# FUNCIONES
# importamos randint que es la que nececitamos y la nombramos azar
from random import randint as azar
# importamos las funciones 
from funciones.corroborar_Naturales import corroborar
from funciones.crearMatriz import CrearMatriz
from funciones.crearNombresPlantas import CrearNombresPlantas
from funciones.diaMasProd import DiaMasProd
from funciones.diaMasProductivoGral import DiaMasProductivoGral

# PROGRAMA             
def Main():
    # monstramos por pantalla un mensaje de bienvenida y usamos el metodo de center para centrar los mensajes
    print("BIENVENIDO A LA EMPRESA FÁBRICA DE BICICLETAS".center(100,' '))
    print()
    print("### A continuación empieza el registro de fabricación de bicicletas según las plantas ###".center(100,' '))
    print()
    
    # pedimos por teclado la cantidad de plantas a crear y con un while chequeamos que no ingrese menos de 0 
    texto= "Por favor ingrese la cantidad numérica existente de plantas de FÁBRICA DE BICICLETAS: "
    texto2="ERROR // Tiene que ser un número natural (>=0)"
    n=corroborar(texto,texto2)
    print()
    
    # verifico que me ingresen aunque sea 1 una planta para crear la matriz 
    if n!= 0:
        
        # a) creamo la lista con los nombres de las plantas y ademas creamos la matriz con el dato n y mostramos
        # la matriz que corresponde a las bicletas creadas por dia segun cada planta (filas)
        plantas=CrearNombresPlantas(n)
        dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
        matriz=CrearMatriz(n,len(dias))
        print()
        # muestro por pantalla la matriz 
        for f in range(len(matriz)):
            for c in range(6):
                print("%5d" %matriz[f][c],end="")
            print()
            
        print()
        
        # b) mostramos la cantidad total de bicicletas fabricadas por planta en una semana
        print()
        print("-- La cantidad total de bicicletas fabricadas según cada planta es: ")
        print()
        for f in range(len(matriz)):
            print(plantas[f], "ha producido",sum(matriz[f]),"bicicletas esta semana.")
        print()
        
        # c)vamos a la funcion que busca el dia que mas se produjo y muestra por pantalla que dia fue y que planta
        print()
        maximo,filamaximo=DiaMasProd(matriz)
        # damos nombre a los dias que estaban indicados del 0 al 6 y la posicion sera dada segun
        # la cantidad maxima de biciletas que se creo en un dia segun la fila y columna
        for i in range (len(filamaximo)):
            print("-- El día más productivo es:",dias[matriz[filamaximo[i]].index(maximo)],
                  "que corresponde a",plantas[filamaximo[i]], "y se generaron ",maximo," bicicletas. ")
            print()
        
        #  d)vamos a la funcion que indica el dia mas productivo considerando todas las plantas
        print()
        maximoGral,posicionGral=DiaMasProductivoGral(matriz)
        for i in range(len(posicionGral)):
            print("-- El día más productivo es:", dias[posicionGral[i]] ,". Se produjo un total de",maximoGral,"bicicletas.")
            print()
        
        # e)lista por comprension que contiene la menor cantidad fabricada por planta
        listaComprension=[min(matriz[i]) for i in range (len(matriz)) ]
        # muestro por pantalla la menor cantidad fabricada por planta
        print()
        for i in range(len(matriz)):
            print("La menor cantidad fabricada por", plantas[i], "esta semana fueron" ,listaComprension[i], "bicicletas.")
        
        
    else:
        # si me ingresan cero plantas lo aviso por pantalla
        print()
        print("ATENCIÓN // Ingresó cero plantas existentes de FÁBRICA DE BICICLETAS".center(100,' '))
        

Main()
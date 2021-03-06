class Instruccion:
    '''This is an abstract class'''
class pekenun(Instruccion) :
    '''
        Esta clase representa la instrucción print.
        La instrucción pekenun únicamente tiene como parámetro una cadena
    '''
    def __init__(self,  cad) :
        self.cad = cad
class tuntepu(Instruccion) :
    '''
        Esta clase representa la instrucción while.
        La instrucción tuntepu recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''
    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones
class Definicion(Instruccion) :
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''
    def __init__(self, id,tipo) :
        self.id = id
        self.tipo = tipo
class Asignacion(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''
    def __init__(self, id, exp,n) :
        self.id = id
        self.exp = exp
        self.n = n
class li(Instruccion) : 
    '''
        Esta clase representa la instrucción if.
        La instrucción li recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''
    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones
class nvli(Instruccion) : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción nvli recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''
    def __init__(self, expLogica, instrliVerdadero = [], instrliFalso = []) :
        self.expLogica = expLogica
        self.instrliVerdadero = instrliVerdadero
        self.instrliFalso = instrliFalso
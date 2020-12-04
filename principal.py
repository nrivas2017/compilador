import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *

def procesar_imprimir(instr, ts) :
    print('> ', resolver_cadena(instr.cad, ts))

def procesar_definicion(instr, ts) :
    if instr.tipo == "rakin":
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.RAKIN, 0)      # inicializamos con 0 como valor por defecto
    if instr.tipo == "chillka":
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHILLKA, "")
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts) :
    if instr.n == 0:
        val = resolver_expresion_aritmetica(instr.exp, ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.RAKIN, val)
    if instr.n == 1:
        val = resolver_cadena(instr.exp, ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CHILLKA, val)
    ts.actualizar(simbolo)

def procesar_tuntepu(instr, ts) :
    while resolver_expreision_logica(instr.expLogica, ts) :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_li(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)

def procesar_nvli(instr, ts) :
    val = resolver_expreision_logica(instr.expLogica, ts)
    if val :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrliVerdadero, ts_local)
    else :
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrliFalso, ts_local)

def resolver_cadena(expCad, ts) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')


def resolver_expreision_logica(expLog, ts) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.MAYOR : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DISTINTO : return exp1 != exp2

def resolver_expreision_booleana(expBool, ts):
    exp1 = resolver_expresion_aritmetica(expBool.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expBool.exp2, ts)
    if expBool.operador == OPERACION_BOOLEANA.KAY : return exp1 and exp2
    if expBool.operador == OPERACION_BOOLEANA.KAM : return exp1 or exp2
    if expBool.operador == OPERACION_BOOLEANA.NV : return exp1 is not exp2

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor


def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, pekenun) : procesar_imprimir(instr, ts)
        elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
        elif isinstance(instr, tuntepu) : procesar_tuntepu(instr, ts)
        elif isinstance(instr, li) : procesar_li(instr, ts)
        elif isinstance(instr, nvli) : procesar_nvli(instr, ts)
        else : print('Error: instrucción no válida')



f = open("./test/test1.txt", "r")
input = f.read()


instrucciones = g.parse(input)

ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global)
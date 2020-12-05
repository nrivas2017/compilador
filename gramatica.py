import ply.lex as lex
import re
import codecs
import os
import sys
from expresiones import *
from instrucciones import *
import ts as TS
import ply.yacc as yacc

# resultado del analisis
resultado_lexema = []
resultado_gramatica = []

reservadas = {
    'llitulun' : 'LLITULUN', 
    'afn' : 'AFN',
    'pvle' : 'PVLE', 
    'nvli' :  'NVLI' ,
    'nv' : 'NV', 
    'li' : 'LI', 
    'tuntepu' : 'TUNTEPU',
    'ponwi' : 'PONWI', 
    'pekenun' : 'PEKENUN', 
    'rakin' : 'RAKIN',
    'chillka':'CHILLKA'
}


tokens= ['ID', 'ENTERO','DECIMAL', 'MAS', 'MENOS', 'POR','DIVIDIDO',
         'ASIGNACION', 'DISTINTO', 'MENOR', 'MAYOR', 'PAREIZQ',
        'PAREDER','COMENTARIO', 'POTENCIA', 'COMENTARIO_MULTILINEA',
		'IGUALQUE', 'CADENA','CONCAT'
        ] + list(reservadas.values())


t_ignore = '\t'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_ASIGNACION = r'='
t_DISTINTO = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_PAREIZQ = r'\('
t_PAREDER = r'\)'
t_POTENCIA = r'\^'
t_IGUALQUE = r'=='
t_CONCAT = r'&'

def t_ID(t):
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    t.type = reservadas.get(t.value.lower(),'ID') 
        
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
  
def t_error(t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

    #print("Illegal character '%s'" % t.value[0])
    #t.lexer.skip(1)
    
# Comentario simple // @ ...
def t_COMENTARIO(t):
    r'@.*'
    pass

# Comentario de múltiples líneas /@ .. @/
def t_COMENTARIO_MULTILINEA(t):
    r'/\@(.|\n)*?\@/'
    pass

def t_ccode_nonspace(t):
    r'\s+'
    pass


# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema
#analizador = lex.lex()

#test = 'test/test1.txt'
#fp = codecs.open(test, "r", "utf-8")
#cadena = fp.read()
#fp.close()

#analizador.input(cadena)

#while True:
#    tok = analizador.token()
#    if not tok : break
#    print (tok)


#begin = llitulun
#end = afn
#and = kay
#del = namemn
#for = pvle
#is = nguen
#raise = kenun
#assert = yafungueltun
#from = mew
#lambda = lambda
#return = weltekun
#break = watron
#else = nvli
#global = kom
#not = nv
#try = pepiltun
#class = fill
#except = wichu
#if = li
#or = kam
#while = tuntepu
#continue = petuln
#exec = deuman
#import = shunul
#pass = non
#with = konme
#def = kudaw
#finally = feywaj
#in = ponwi
#print = pekenun
#yield = yield
#self = inche
#as = chumnone



# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


precedence = (
    ('right','ASIGNACION'),
    ('left','DISTINTO'),
    ('left','MENOR','MAYOR'),
    ('left','MAS', 'MENOS'),
    ('left','POR','DIVIDIDO'),
    ('left','POTENCIA'),
    ('left','PAREIZQ','PAREDER')
)

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instruccion_definicion(t) :
    '''definicion_instr   : RAKIN ID
                          | CHILLKA ID'''
    
    if t[1] == "rakin":
        t[0] =Definicion(t[2],t[1])
    elif t[1] == "chillka":
        t[0] =Definicion(t[2],t[1])

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : pekenun_instr
                        | definicion_instr
                        | asignacion_instr
                        | tuntepu_instr
                        | li_instr
                        | nvli_instr'''
    t[0] = t[1]

def p_instruccion_pekenun(t) :
    'pekenun_instr     : PEKENUN PAREIZQ expresion_cadena PAREDER'
    t[0] =pekenun(t[3])

def p_asignacion_instr(t) :
    '''asignacion_instr   : ID ASIGNACION expresion_numerica
                          | ID ASIGNACION expresion_cadena '''
    
    if (type(t[3].val)==int) : n=0;  t[0] =Asignacion(t[1], t[3],n)
    elif (type(t[3].val)==str) : n=1; t[0] =Asignacion(t[1], t[3],n)

def p_tuntepu_instr(t) :
    'tuntepu_instr     : TUNTEPU PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN'
    t[0] =tuntepu(t[3], t[6])

def p_li_instr(t) :
    'li_instr           : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN'
    t[0] =li(t[3], t[6])

def p_nvli_instr(t) :
    'nvli_instr      : LI PAREIZQ expresion_logica PAREDER LLITULUN instrucciones AFN NVLI LLITULUN instrucciones AFN'
    t[0] =nvli(t[3], t[6], t[10])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica
                        | expresion_numerica POTENCIA expresion_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '^': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIA)

def p_expresion_agrupacion(t):
    'expresion_numerica : PAREIZQ expresion_numerica PAREDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                        | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_cadena(t) :
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_concatenacion(t) :
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])

def p_expresion_cadena_numerico(t) :
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])

def p_expresion_logica(t) :
    '''expresion_logica : expresion_numerica MAYOR expresion_numerica
                        | expresion_numerica MENOR expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica DISTINTO expresion_numerica'''
    if t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR)
    elif t[2] == '<'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR)
    elif t[2] == '==' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DISTINTO)

def p_error(t):
    #print(t)
    #print("Error sintáctico en '%s'" % t.value)
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
"""
def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica"""

parser = yacc.yacc()

def parse(input) :
   
    return parser.parse(input)

def procesar_imprimir(instr, ts) :
    print ('> %s'%(resolver_cadena(instr.cad, ts)))
    return '> %s'%(resolver_cadena(instr.cad, ts))

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

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA : return exp1 ** exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.obtener(expNum.id).valor


def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    global resultado_gramatica
    for instr in instrucciones :
        if isinstance(instr, pekenun) : 
            resultado_gramatica.append(procesar_imprimir(instr, ts))
        elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
        elif isinstance(instr, tuntepu) : procesar_tuntepu(instr, ts)
        elif isinstance(instr, li) : procesar_li(instr, ts)
        elif isinstance(instr, nvli) : procesar_nvli(instr, ts)
        else : 
            print ('Error: instrucción no válida')
            resultado_gramatica.append('> Error: instrucción no válida')
    return resultado_gramatica

def prueba_sintactica(data):
    instrucciones = parse(data)

    ts_global = TS.TablaDeSimbolos()
    return procesar_instrucciones(instrucciones, ts_global)

#print (prueba_sintactica(input))
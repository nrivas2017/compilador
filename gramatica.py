import ply.lex as lex
import re
import codecs
import os
import sys
from expresiones import *
from instrucciones import *
import ply.yacc as yacc

reservadas=[]

reservadas = {
    'llitulun' : 'LLITULUN', 
    'afn' : 'AFN',
    'kay' : 'KAY', 
    'namemn' : 'NAMEMN', 
    'pvle' : 'PVLE', 
    'nguen' : 'NGUEN',
    'kenun' : 'KENUN', 
    'yafungueltun' : 'YAFUNGUELTUN', 
    'mew' : 'MEW', 
    'weltekun' : 'WELTEKUN', 
    'nvli' :  'NVLI' ,
    'watron' : 'WATRON',
    'kom' :  'KOM', 
    'nv' : 'NV', 
    'pepiltun' : 'PEPILTUN',
    'wichu' : 'WICHU', 
    'li' : 'LI', 
    'kam' : 'KAM', 
    'tuntepu' : 'TUNTEPU', 
    'petuln' : 'PETULN', 
    'deuman' : 'DEUMAN', 
    'shunul' : 'SHUNUL', 
    'non' : 'NON', 
    'konme' : 'KONME',
    'kudaw' : 'KUDAW', 
    'feywaj' : 'FEYWAJ', 
    'ponwi' : 'PONWI', 
    'pekenun' : 'PEKENUN', 
    'inche' : 'INCHE', 
    'chumnone' : 'CHUMNONE',
    'numero':'NUMERO'
}


tokens= ['ID', 'ENTERO','DECIMAL', 'MAS', 'MENOS', 'POR','DIVIDIDO',
         'ASIGNACION', 'DISTINTO', 'MENOR', 'MAYOR', 'PAREIZQ',
        'PAREDER','LLAVIZQ','LLAVDER','COMENTARIO', 'POTENCIA', 'COMENTARIO_MULTILINEA',
		'COMA', 'IGUALQUE', 'CADENA','CONCAT'
        ] + list(reservadas.values())

print (tokens)
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
t_LLAVIZQ = r'\{'
t_LLAVDER = r'\}'
t_POTENCIA = r'\^'
t_COMA = r','
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
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
    ('left','PAREIZQ','PAREDER'),
    ('left','LLAVIZQ','LLAVDER')
)

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : pekenun_instr
                        | asignacion_instr
                        | tuntepu_instr
                        | li_instr
                        | if_else_instr'''
    t[0] = t[1]

def p_instruccion_pekenun(t) :
    'pekenun_instr     : PEKENUN PAREIZQ expresion_cadena PAREDER'
    t[0] =pekenun(t[3])

def p_asignacion_instr(t) :
    'asignacion_instr   : ID ASIGNACION expresion_numerica'
    t[0] =Asignacion(t[1], t[3])

def p_tuntepu_instr(t) :
    'tuntepu_instr     : TUNTEPU PAREIZQ expresion_logica PAREDER LLAVIZQ instrucciones LLAVDER'
    t[0] =tuntepu(t[3], t[6])

def p_li_instr(t) :
    'li_instr           : LI PAREIZQ expresion_logica PAREDER LLAVIZQ instrucciones LLAVDER'
    t[0] =li(t[3], t[6])

def p_if_else_instr(t) :
    'if_else_instr      : LI PAREIZQ expresion_logica PAREDER LLAVIZQ instrucciones LLAVDER NVLI LLAVIZQ instrucciones LLAVDER'
    t[0] =IfElse(t[3], t[6], t[10])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

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
    print(t)
    print("Error sintáctico en '%s'" % t.value)


parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
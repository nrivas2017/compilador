import ply.lex as lex
import re
import codecs
import os
import sys

reservadas=['LLITULUN', 'AFN', 'KAY', 'NAMEMN', 'PVLE', 'NGUEN', 'KENUN', 'YAFUNGUELTUN', 
            'MEW', 'LAMBDA', 'WELTEKUN', 'WATRON', 'NVLI', 'KOM', 'NV', 'PEPILTUN', 'FILL', 
            'WICHU', 'LI', 'KAM', 'TUNTEPU', 'PETULN', 'DEUMAN', 'SHUNUL', 'NON', 'KONME',
            'KUDAW', 'FEYWAJ', 'PONWI', 'PEKENUN', 'YIELD', 'INCHE', 'CHUMNONE']

tokens= reservadas+['ID', 'ENTERO','DECIMAL', 'MAS', 'MENOS', 'POR','DIVIDIDO',
         'ASIGNACION', 'DISTINTO', 'MENOR', 'MENORIGUAL','MAYOR',
        'MAYORIGUAL','PAREIZQ','PAREDER','CORIZQ','CORDER','COMENTARIO', 'POTENCIA'
			]
t_ignore = '\t'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_ASIGNACION = r'='
t_DISTINTO = r'!='
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_PAREIZQ = r'\('
t_PAREDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_POTENCIA = r'\^'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
        
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
    r'/\*(.|\n)*?\*/'
    pass

def t_ccode_nonspace(t):
    r'\s+'
    pass


analizador = lex.lex()

test = 'test/test1.txt'
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print (tok)


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
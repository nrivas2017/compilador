import ply.lex as lex
import re
import codecs
import os
import sys

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
    'chumnone' : 'CHUMNONE'
}


tokens= ['ID', 'ENTERO','DECIMAL', 'MAS', 'MENOS', 'POR','DIVIDIDO',
         'ASIGNACION', 'DISTINTO', 'MENOR', 'MAYOR', 'PAREIZQ',
        'PAREDER','LLAVIZQ','LLAVDER','COMENTARIO', 'POTENCIA', 'COMENTARIO_MULTILINEA',
		'COMA', 'IGUALQUE', 'CADENA'
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
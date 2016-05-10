# -*- encondig: utf-8 -*-

# --------------------------------------
# JacuScript Analizador Lexico
# --------------------------------------

import ply.lex as lex

# Lista de Tokens
tokens = (

	# Palabras Reservadas
	'SINO',
	'SI',
	'ENTERO',
	'REAL',
	'BOOL',
	'CAR',
	'REGRESA',
	'FUNCION',
	'MIENTRAS',
	'DEPLANO',
	'PARA',
	'FLOTANTE',
	'NULO',
	'CADENA',
	'AND',
	'OR',
	'XOR',
	'NOT',
#	'ERROR',
	'IMPORTAME',
	
	
	
	# Simbolos
	'SUMA',
	'RESTA',
	'PRODUCTO',
	'DIVISION',
	'MENOR',
	'MENORIGUAL',
	'MAYOR',
	'MAYORIGUAL',
	'IGUAL',
	'IGUALDAD',
	'DIFERENTE',
	'NEGACION',
	'PUNTOCOMA',
	'COMA',
	'LPAREN',
	'RPAREN',
	'LLLAVE',
	'RLLAVE',
	'LCORCHETE',
	'RCORCHETE',

	# Otros	
	'ID', 
	'NUMERO',
)

reserved = {
'NULL' : 'NULO',
}

# Regular expressions rules for a simple tokens
t_SUMA 	 = r'\+'
t_RESTA	 = r'-'
t_PRODUCTO  = r'\*'
t_DIVISION = r'/'
t_MENOR 	 = r'<'
t_MAYOR = r'>'
t_IGUAL  = r'='
t_NEGACION = r'!'
t_PUNTOCOMA = ';'
t_COMA	 = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_LCORCHETE   = r'\['
t_RCORCHETE   = r'\]'


#def t_ERROR(t):
#	r'([+-]?[0-9]+(\.([0-9]+))?[eE][+-][0-9]+[+-][0-9]+)|([0-9]+[+-][+-]+[0-9]+)'
#	return t
	#print "Error Lexico: " + str(t.value[0])
	#t.lexer.skip(1)

def t_IMPORTAME(t):
	r'importame'
	return t

def t_NULO(t):
	r'NULO'
	return t

def t_SINO(t):
	r'sino'
	return t
	
def t_SI(t):
	r'si'
	return t

def t_DEPLANO(t):
	r'deplano'
	return t
	
def t_PARA(t):
	r'para'
	return t
	
def t_CADENA(t):
	r'("|\').*("|\')'
	return t

def t_ENTERO(t):
	r'entero'
	return t

def t_REAL(t):
	r'real'
	return t

def t_BOOL(t):
	r'bool'
	return t
	
def t_CAR(t):
	r'car'
	return t
		
def t_REGRESA(t):
	r'regresa'
	return t
	
def t_FUNCION(t):
	r'funcion'
	return t
	
def t_MIENTRAS(t):
	r'mientras'
	return t

	
def t_FLOTANTE(t):
	r'[+-]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][+-]?[0-9]+)'
	return t
	
	
#OPERADORES LOGICOS
def t_AND(t):
	r'and'
	return t
	
def t_OR(t):
	r'or'
	return t
	
def t_XOR(t):
	r'xor'
	return t
	
def t_NOT(t):
	r'no'
	return t
	
def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t
	#corregir

	
def t_ID(t):
	r'\w+(_\d\w)*'
	return t

def t_MENORIGUAL(t):
	r'<='
	return t

def t_MAYORIGUAL(t):
	r'>='
	return t

def t_IGUALDAD(t):
	r'=='
	return t

def t_DIFERENTE(t):
	r'!='
	return t

def t_nuevalinea(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	
def t_error (t) :
    print 'Illegal lexer input line ' + str(t.lineno) + ' ' + t.value[:16]
    sys.exit(-1)

t_ignore = ' \t'

def t_comentarios(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_comentario(t):
	r'\#.*'    
	t.lexer.lineno += 1
	pass

#def t_error(self,t):
#	print("Illegal character '%s'" % t.value[0])
#	t.lexer.skip(1)
#	pass	

def tokenize(data, lexer):
	tokens = []
	lexer.input(data)
	while True:
		tok = lexer.token()
		
		if not tok:break
		tokens.append(tok)
		print(tok.type, tok.value, tok.lineno, tok.lexpos)
	
	return tokens
		#print tok
def inptokenize(data):
	lexer = lex.lex()
	tokenize(data,lexer)
	

lexer = lex.lex()

programa = '''#comenatrio simple
/*
  esto es un comentrio
de
vraias
lienas
*/






entero r_7/123;
real pi = 3.234e-9;
car jorge;

jorge = "la cadena se comorta como cadena";
si (jorge > 10000.880) {
	funcion abc(){
		regresa vacio;
	}
}
3+-4
r8999= 34e+2-2;
entero 
123sddee
= 
NULO;
para i 23 <= 67;
( (76  and 89) or 89) 
'''
#lexer.input(programa)
#tokenize(programa,lexer)
# Test 

# -*- enconding: utf-8 -*-
import ply.yacc as yacc
from jacu_lexer import tokens
import jacu_lexer
import sys

VERBOSE = 1

def p_program(p):
	'program : declaracion_list'
	pass

def p_declaracion_list_1(p):
	'declaracion_list : declaracion_list declaracion'
	 #p[0] = p[1] + p[2]  
	pass

def p_declaracion_list_2(p):
	'declaracion_list : declaracion'
	pass

def p_declaracion(p):
	'''declaracion : var_declaracion
				  | fun_declaracion
				  |	libreria'''
	pass

def p_libreria(p):
	'libreria : IMPORTAME CADENA PUNTOCOMA'
	pass

def p_var_declaracion_1(p):
	'var_declaracion : type_specifier ID PUNTOCOMA'
	pass

def p_var_declaracion_2(p):
	'var_declaracion : type_specifier ID LCORCHETE NUMERO RCORCHETE PUNTOCOMA'
	pass

def p_var_declaracion_3(p):
	'var_declaracion : type_specifier ID IGUAL expression PUNTOCOMA'
	pass
	
def p_var_declaracion_4(p):
	'var_declaracion : ID IGUAL expression PUNTOCOMA'
	pass
	
def p_type_specifier_1(p):
	'type_specifier : ENTERO'
	pass

def p_type_specifier_2(p):
	'type_specifier : REAL'
	pass

def p_type_specifier_3(p):
	'type_specifier : BOOL'
	pass
	
def p_type_specifier_4(p):
	'type_specifier : CAR'
	pass

def p_fun_declaracion(p):
	'fun_declaracion : FUNCION ID LPAREN params RPAREN compount_stmt'
	pass

def p_params_1(p):
	'params : param_list'
	pass


def p_params_2(p):
	'params : empty'
	pass

def p_param_list_1(p):
	'param_list : param_list COMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : type_specifier ID'
	pass

def p_param_2(p):
	'param : type_specifier ID LCORCHETE RCORCHETE'
	pass

def p_compount_stmt(p):
	'compount_stmt : LLLAVE local_declarations statement_list RLLAVE'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaracion'
	pass


def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
				| para_stmt
				| fun_declaracion
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression PUNTOCOMA'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : PUNTOCOMA'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : SI LPAREN expression RPAREN statement SINO LPAREN expression RPAREN statement DEPLANO statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : SI LPAREN expression RPAREN statement SINO LPAREN expression RPAREN statement'
	pass


def p_selection_stmt_3(p):
	'selection_stmt : SI LPAREN expression RPAREN statement'
	pass	

def p_iteration_stmt(p):
	'iteration_stmt : MIENTRAS LPAREN expression RPAREN statement'
	pass

def p_para_stmt(p):
	'para_stmt : PARA LPAREN expression COMA expression COMA expression RPAREN statement'

def p_return_stmt_1(p):
	'return_stmt : REGRESA PUNTOCOMA'
	pass

def p_return_stmt_2(p):
	'return_stmt : REGRESA expression PUNTOCOMA'
	pass

def p_expression_1(p):
	'expression : var IGUAL expression'
	pass

def p_expression_2(p):
	'expression : comp_expression'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LCORCHETE expression RCORCHETE'
	pass

def p_comp_expression_1(p):
	'comp_expression : simple_expression compop simple_expression'
	pass

def p_comp_expression_2(p):
	'comp_expression : simple_expression'
	pass

def p_compop(p):
	'''compop : AND
			| OR
			| XOR
			| NOT
	'''
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_relop(p):
	'''relop : MENOR 
			| MENORIGUAL
			| MAYOR
			| MAYORIGUAL
			| IGUALDAD
			| NEGACION
			| DIFERENTE
	'''
	pass

def p_additive_expression_1(p):
	'additive_expression : additive_expression addop term'
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_addop(p):
	'''addop : SUMA 
			| RESTA
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	PRODUCTO
				| DIVISION
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMERO' 
	pass

#maybe
def p_factor_5(p):
	'factor : CADENA'
	pass

def p_factor_6(p):
	'factor : FLOTANTE'
	pass

def p_factor_7(p):
	'factor : NULO'
	pass
	
def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	#print str(dir(p))
	#print str(dir(cminus_lexer))
	cont = 0
	if VERBOSE:
		if p is not None:
			print "Error de sintaxis en la linea " + str(p.lexer.lineno) + " token inesperado  " + str(p.value)
			cont+=1
		else:
			print "Error de sintaxis en la linea: " + str(jacu_lexer.lexer.lineno)
			cont+=1
	else:
		raise Exception('syntax', 'error')
	if cont == 0:
		print "Compilacion exitosa"
	
	
		


parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.jacu'

	f = open(fin, 'r')
	data = f.read()
	jacu_lexer.tokenize(data,jacu_lexer.lexer)
	print data
	
	parser.parse(data, tracking=True)
	



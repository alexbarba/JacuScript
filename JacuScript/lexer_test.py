import jacu_lexer

if __name__ == '__main__':

	# Test
	info = '''
		entero r_7/123;
		car jorge;
		
		si (jorge > 10000.880) {
		   funcion abc(){
			   regresa vacio;
		   }
		}
		r8999= 34e+2-2;
		entero 
		123sddee= NULO;
		
	'''
	
	
		
		
	# Build lexer and try on
	jacu_lexer.lexer.input(info)
	jacu_lexer.tokenize(info, jacu_lexer.lexer)

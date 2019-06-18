import re
linea=0
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','POTENCY','DIVIDE_INT','STR','LIST',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POTENCY = r'\*{2}'
t_DIVIDE_INT = r'\/{2}'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STR(t):
    r'(\'(\s*\w*\S*)+\')|(\"(\s*\w*\S*)+\")'
    t.value =t.value
    return t

def t_LIST(t):
    r'\[(\s*\w*\S*)+\]'
    t.value=t.value
    return t

t_ignore = " \t"

def t_error(t):
    print("Caracter no válido '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lex.lex()

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

names = { }


def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    aux=str(p[1])
    print(re.sub('"', "", re.sub("'","",aux)))

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression 
                  | expression POTENCY expression
                  | expression DIVIDE_INT expression'''
    try:
        if p[2] == '+': p[0] = p[1] + p[3]
        elif p[2] == '-': p[0] = p[1] - p[3]
        elif p[2] == '*': p[0] = p[1] * p[3]
        elif p[2] == '/': p[0] = p[1] / p[3]
        elif p[2]== '**':  p[0]= p[1] ** p[3]
        elif p[2]== '//':  p[0]= p[1] // p[3]
    except:
        print("La operacion no es válida")

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expresion_str(p):
    'expression : STR'
    p[0]= str(p[1])

def p_expresion_list(p):
    'expression : LIST'
    p[0]=str(p[1])

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("La variable '%s' no esta definida " % p[1])

def p_error(p):
    print("Error de sintaxis '%s'" % p.value)

import ply.yacc as yacc
yacc.yacc()
while True:
    try:
        s = input("Linea %s:"%linea)
        linea=linea+1
    except EOFError:
        break
    yacc.parse(s)
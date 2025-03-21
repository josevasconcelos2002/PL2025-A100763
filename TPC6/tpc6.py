import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    if p[3] == 0:
        print("Erro: Divisão por zero!")
        p[0] = 0  # Ou outra forma de tratar o erro
    else:
        p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")



precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

parser = yacc.yacc()

while s := input('calc > '):
   result = parser.parse(s)
   print(result)





# 1 + 2
# exp: exp sinal NUM
#    | NUM

# sinal: ...



#                     exp(1+2*3)
#          exp(1+2)               sinal(*)      NUM(3)       
#   exp(1) sinal(+) NUM(2)
# NUM(1)


# COMO DAR PRIORIDADE À MULTIPLICACAO ? 

# isto reconhece de baixo para cima, da esquerda para a direita


# exp: exp PLUS term
#    | exp MINUS term
#    | term

# term: term MULT NUM
#     | term DIV NUM
#     | NUM


#                             exp(1+2*3)
#                   exp(1)                  PLUS(+)      term(2*3)
# ....             


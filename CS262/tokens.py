import ply.lex as lex

def test_lexer(lexer,input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### Not used in this problem. 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

states = ( ('comment', 'exclusive'),)

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_comment_error(t):
    t.lexer.skip(1)

def t_eolcomment(t):
    r'//.*'
    pass

t_ignore               = ' \t\v\r'
t_comment_ignore       = ' \t\v\r'
    
t_ANDAND          = r'&&'
t_COMMA           = r','
t_DIVIDE          = r'/'
t_ELSE            = r'else'
t_EQUAL           = r'='
t_EQUALEQUAL      = r'=='
t_TRUE            = r'true'
t_FALSE           = r'false'
t_FUNCTION        = r'function'
t_IF              = r'if'
t_RETURN          = r'return'
t_VAR             = r'var'
t_LPAREN          = r'\('
t_LBRACE          = r'{'
t_RBRACE          = r'}'
t_SEMICOLON       = r';'
t_MINUS           = r'-'
t_NOT             = r'!'
t_OROR            = r'\|\|'
t_PLUS            = r'\+'
t_RPAREN          = r'\)'
t_TIMES           = r'\*'
t_LE              = r'<='
t_LT              = r'<'
t_GT              = r'>'
t_GE              = r'>='

# from unit 6  fitting them together
def t_javascript_start(token):
    pass
    r'\<script\ type =\"text/\javascript\"\>'   # <script type ="text/javascript>"
    token.lexer.code_start = token.lexer.lexpos
    token.lexer.begin("javascript")             

def t_javascript_end(token):
    pass
    r'\<\/script\>'                             # </script>
    token.value = token.lexer.lexdata[token.lexer.code_start: token.lexer.lexpos-9] # 取出jascript标签的的代码部分
    token.type = 'JAVASCRIPT'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin.('INITIAL')  # goto init state: 这时可以处理html标签.
    return token

# 13
# -13
# 13.
# 13.00001
def t_NUMBER(token):
    r'-?[0-9]+(?:\.[0-9]*)?'
    token.value = float(token.value)
    return token
    
def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token
    
# string: 
# 必须包含在""内;
# 可以分成两种类型的，一种是非 转义的字符"" "abc 3j923j)*(&"
# 一种是转义字符，例如"\n \s"
def t_STRING(token):
    r'"(?:[^"\\]|(?:\\.))*"'
    token.value = token.value[1:-1]
    return token

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)

lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print (test_lexer(input1) == output1)

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print (test_lexer(input2) == output2)
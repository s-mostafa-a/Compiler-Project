import codecs

import ply.lex as lex
import sys

sTable = []

tokens = ['Const_KW', 'reserved', 'Num', 'Letter', 'idLetter','idNum', 'Opening_Bracket', 'Closing_Bracket', 'Semicolon', 'Boolean_KW',
          'Character_KW', 'Integer_KW', 'char_KW', 'bool_KW', 'int_KW', 'void_KW', 'If_KW', 'Other_KW', 'Till_KW',
          'ComeBack_KW', 'GiveBack_KW', 'Continue_KW', 'PP', 'MM', 'Opening_Parentheses', 'Static_KW',
          'Closing_Parentheses', 'Opening_Brace', 'Closing_Brace', 'Equal', 'PlusEqual',
          'MinusEqual', 'TimesEqual', 'DivideEqual', 'Then_KW', 'Else_KW', 'LEqual', 'GEqual',
          'EEqual', 'GreaterOP', 'LessOP', 'NonEqualOP', 'Plus', 'Minus', 'Times',
          'Divide', 'ModeOP', 'QMark', 'True_KW', 'False_KW', 'DoubleAnd', 'DoubleOr',
          'Tilda', 'And_KW', 'Or_KW', 'Comment', 'Comma', 'Colon', 'Dot']


t_ignore = ' \t'
t_Colon = '\:'
t_Comma = r'\,'
t_Opening_Bracket = r'\['
t_Closing_Bracket = r']'
t_Semicolon = r';'
t_PP = r'\+\+'
t_MM = r'--'
t_Opening_Parentheses = r'\('
t_Closing_Parentheses = r'\)'
t_Opening_Brace = r'\{'
t_Closing_Brace = r'}'
t_Equal = r'='
t_PlusEqual = r'\+='
t_MinusEqual = r'-='
t_TimesEqual = r'\*='
t_DivideEqual = r'/='
t_LEqual = r'<='
t_GEqual = r'>='
t_EEqual = r'=='
t_GreaterOP = r'>'
t_LessOP = r'<'
t_NonEqualOP = r'!='
t_Plus = r'\+'
t_Minus = r'-'
t_Times = r'\*'
t_Divide = r'/'
t_ModeOP = r'%'
t_QMark = r'\?'
t_DoubleAnd = r'\&\&'
t_DoubleOr = r'\|\|'
t_Tilda = r'\~'

t_Dot = r'\.'

reserved = {
    'boolean': 'Boolean_KW',
    'character': 'Character_KW',
    'integer': 'Integer_KW',
    'char': 'char_KW',
    'bool': 'bool_KW',
    'int': 'int_KW',
    'void': 'void_KW',
    'if': 'If_KW',
    'other': 'Other_KW',
    'till': 'Till_KW',
    'comeBack': 'ComeBack_KW',
    'giveBack': 'GiveBack_KW',
    'continue': 'Continue_KW',
    'static': 'Static_KW',
    'then': 'Then_KW',
    'else': 'Else_KW',
    'CONST': 'Const_KW',
    'true': 'True_KW',
    'false': 'False_KW',
    'and' : 'And_KW',
    'or' : 'Or_KW'
}



def t_idNum(t):
    r'[0-9]+[a-zA-Z]+[a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'IDENTSYM')
    return t

def t_Num(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_idLetter(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'idLetter')  # Check for reserved words
    #
    if t.value not in reserved:
        t.type = reserved.get(t.value,'idLetter')
    return t


def t_error(t):
    print("Invalid character: ", t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'(//.*)|%%%.*[\r\n]*.*%%%'
    pass

def t_newline( t):
    r'\r?\n+'
    t.lexer.lineno += t.value.count("\n")


lexer = lex.lex()
for i in range(5):
    orig_stdout = sys.stdout
    out = open('./../phase1/test_case{0}_answer.txt'.format(i+1), 'w')
    sys.stdout = out
    f = codecs.open('./../phase1/test_case{0}.code'.format(i+1), encoding='utf-8')
    lexer.input(f.read())
    print("type \t\t\t\t\t value \t\t\t\t\t line \t\t\t\t\t lexpos ")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(str(tok.type) + "\t\t\t\t\t" + str(tok.value) + "\t\t\t\t\t" + str(tok.lineno) + "\t\t\t\t\t" + str(
            tok.lexpos))
    f.close()

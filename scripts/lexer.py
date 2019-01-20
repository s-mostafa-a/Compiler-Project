import codecs

import ply.lex as lex


reserved = {
    'boolean': 'BOOLEAN_KW',
    'character': 'CHARACTER_KW',
    'integer': 'INTEGER_KW',
    'char': 'CHAR_KW',
    'bool': 'BOOL_KW',
    'int': 'INT_KW',
    'void': 'VOID_KW',
    'static': 'STATIC_KW',
    'if': 'IF_KW',
    'other': 'OTHER_KW',
    'till': 'TILL_KW',
    'comeback': 'COMEBACK_KW',
    'giveback': 'GIVEBACK_KW',
    'continue': 'CONTINUE_KW',
    'then': 'THEN_KW',
    'else': 'ELSE_KW',
    'CONST': 'CONST_KW',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = [
    'NUMBER',
    'LETTER',
    'COMMENT',


    'COLON',    #
    'COMA',     #
    'SEMICOLON',    #
    'OPENING_BRACKET',  #
    'CLOSING_BRACKET',  #
    'OPENING_PARENTHESES',  #
    'CLOSING_PARENTHESES',  #
    'OPENING_BRACE',  #
    'CLOSING_BRACE',  #


    'PL_OP',    # +
    'MI_OP',    # -
    'MU_OP',    # *
    'DI_OP',    # /
    'PE_OP',    # %
    'EQ_OP',    # =
    'PLE_OP',   # +=
    'MIE_OP',   # -=
    'MUE_OP',   # *=
    'DIE_OP',   # /=
    'PP_OP',    # ++
    'MM_OP',    # --
    'QU_UOP',   # ?
    'AA_LOP',   # &&
    'OO_LOP',   # ||
    'TIL_LOP',  # ~
    'AND_LOP',  # AND
    'OR_LOP',   # OR


    'GT_REL',   # >
    'LT_REL',   # <
    'EQ_REL',   # ==
    'NEQ_REL',  # !=
    'LE_REL',   # <=
    'GE_REL'    # >=
] + list(reserved.values())

t_ignore = ' \t'

t_COMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_OPENING_BRACKET = r'\['
t_CLOSING_BRACKET = r'\]'
t_OPENING_PARENTHESES = r'\('
t_CLOSING_PARENTHESES = r'\)'
t_OPENING_BRACE = r'\{'
t_CLOSING_BRACE = r'\}'

t_PL_OP = r'\+'
t_MI_OP = r'-'
t_MU_OP = r'\*'
t_DI_OP = r'\/'
t_PE_OP = r'%'
t_EQ_OP = r'='
t_PLE_OP = r'\+='
t_MIE_OP = r'-='
t_MUE_OP = r'\*='
t_DIE_OP = r'\/='
t_PP_OP = r'\+\+'
t_MM_OP = r'--'
t_QU_UOP = r'\?'
t_AA_LOP = r'\&\&'
t_OO_LOP = r'\|\|'
t_TIL_LOP = r'\~'
t_AND_LOP = r'AND'
t_OR_LOP = r'OR'

t_GT_REL = r'>'
t_LT_REL = r'<'
t_EQ_REL = r'=='
t_NEQ_REL = r'!='
t_LE_REL = r'<='
t_GE_REL = r'>='

def t_COMMENT(t):
    r'\/\/.*'
    return t

def t_NUMBER(t):
    r'\d +'
    t.value = int(t.value)
    return t

def t_LETTER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'LETTER')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\r?\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()

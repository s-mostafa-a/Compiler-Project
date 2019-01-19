import codecs

import ply.lex as lex


class Lexer:
    """
    t_BOOLEAN_KW = r'boolean'
    t_CHARACTER_KW = r'character'
    t_INTEGER_KW = r'integer'
    t_CHAR_KW = r'char'
    t_BOOL_KW = r'bool'
    t_INT_KW = r'int'
    t_VOID_KW = r'void'
    t_STATIC_KW = r'static'
    t_IF_KW = r'if'
    t_OTHER_KW = r'other'
    t_TILL_KW = r'till'
    t_COMEBACK_KW = r'comeback'
    t_GIVEBACK_KW = r'giveback'
    t_CONTINUE_KW = r'continue'
    t_THEN_KW = r'then'
    t_ELSE_KW = r'else'
    t_CONST_KW = r'CONST'
    t_TRUE_KW = r'true'
    t_FALSE_KW = r'false'
    """
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


        'SEMICOLON',
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

    def t_COMMENT(self, t):
        r'\/\/.*'
        return t

    def t_NUMBER(self, t):
        r'\d +'
        t.value = int(t.value)
        return t

    def t_LETTER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'LETTER')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\r?\n+'
        t.lexer.lineno += t.value.count("\n")

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

if __name__ == '__main__':
    lexer = Lexer().build()
    f = codecs.open('./../test.code', encoding='utf-8')
    lexer.input(f.read())
    f.close()
    print("type \t\t\t\t\t value \t\t\t\t\t line \t\t\t\t\t lexpos ")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(str(tok.type) + "\t\t\t\t\t" + str(tok.value) + "\t\t\t\t\t" + str(tok.lineno) + "\t\t\t\t\t" + str(tok.lexpos))

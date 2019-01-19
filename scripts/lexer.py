import ply.lex as lex


class Lexer:
    tokens = (
        'NUMBER',
        'LETTER',
        'COMMENT',


        'IGNORE',


        'SEMICOLON',
        'OPENING_BRACKET',  #
        'CLOSING_BRACKET',  #
        'OPENING_PARENTHESES',  #
        'CLOSING_PARENTHESES',  #
        'OPENING_BRACE',  #
        'CLOSING_BRACE',  #


        'BOOLEAN_KW',
        'CHARACTER_KW',
        'INTEGER_KW',
        'CHAR_KW',
        'BOOL_KW',
        'INT_KW',
        'VOID_KW',
        'STATIC_KW',
        'IF_KW',
        'OTHER_KW',
        'TILL_KW',
        'COMEBACK_KW',
        'GIVEBACK_KW',
        'CONTINUE_KW',
        'THEN_KW',
        'ELSE_KW',
        'CONST_KW',
        'TRUE_KW',
        'FALSE_KW',


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
        'GE_REL',   # >=
    )

    t_IGNORE = ' \t'

    t_SEMICOLON = r';'
    t_OPENING_BRACKET = r'\['
    t_CLOSING_BRACKET = r'\]'
    t_OPENING_PARENTHESES = r'\('
    t_CLOSING_PARENTHESES = r'\)'
    t_OPENING_BRACE = r'\{'
    t_CLOSING_BRACE = r'\}'

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
    t_FALSE_KW = r'flase'

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


if __name__ == '__main__':
    print("hi")

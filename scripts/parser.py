from ply import yacc
from scripts import lexer


class Yacc:
    tokens = lexer.tokens

    precedence = (
        ('nonassoc', 'OPENING_PARENTHESES'),  # Nonassociative operators
        ('nonassoc', 'OTHER_KW'),  # Nonassociative operators
        ('left', 'THEN_KW'),
        ('left', 'ELSE_KW'),
        #('left', 'logicOp'),
        # AA_LOP
        # | OO_LOP
        # | TIL_LOP
        # | AND_LOP
        # | OR_LOP
        ('left', 'AA_LOP', 'OO_LOP', 'TIL_LOP', 'AND_LOP', 'OR_LOP'),
        # ('left', 'mathOp'),
        # """mathOp : EQ_OP
        # | PLE_OP
        # | MIE_OP
        # | MUE_OP
        # | DIE_OP"""
        ('left', 'EQ_OP', 'PLE_OP', 'MIE_OP', 'MUE_OP', 'DIE_OP'),


        # ('left', 'op'),
        # """op : PL_OP
        # | MI_OP
        # | MU_OP
        # | DI_OP
        # | PE_OP"""
        ('left', 'PL_OP', 'MI_OP', 'MU_OP', 'DI_OP', 'PE_OP'),

        # ('left', 'unaryop'),
        # """unaryop : MI_OP
        # | MU_OP
        # | QU_UOP"""
        ('left', 'MI_OP', 'MU_OP', 'QU_UOP'),

    )

    def p_program(self, p):
        """program : list"""
        print("1")

    def p_numOrLetter(self, p):
        """numOrLetter : NUMBER
        | LETTER
        |
        """
        print("2")

    def p_list(self, p):
        """list : list declaration
        | declaration"""
        print("3")

    def p_declaration(self, p):
        """declaration : VOID_KW LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE localDeclarations statementList CLOSING_BRACE
        | VOID_KW LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES statementWithoutBracket
        | type LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE localDeclarations statementList CLOSING_BRACE
        | type LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES statementWithoutBracket
        | type LETTER varInitialization SEMICOLON
        | type LETTER varInitialization COMA variableList SEMICOLON"""
        print("4")
        #for i in p:
        #    print(i)


    def p_ScopedVariableDec(self, p):
        """ScopedVariableDec : scopedSpecifier variableList SEMICOLON"""
        print("5")


    def p_variableList(self, p):
        """variableList : variableList COMA variableList
        | varInitialization"""
        print("6")


    def p_varInitialization(self, p):
        """varInitialization : varForm
        | varForm COLON OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES"""
        print("7")


    def p_varForm(self, p):
        """varForm : LETTER OPENING_BRACKET NUMBER CLOSING_BRACKET
        | numOrLetter """
        print("8")

    def p_scopedSpecifier(self, p):
        """scopedSpecifier : STATIC_KW type
        | type"""
        print("9")


    def p_type(self, p):
        """type : BOOLEAN_KW
        | CHARACTER_KW
        | INTEGER_KW
        | CHAR_KW
        | BOOL_KW
        | INT_KW"""
        print("10")

    def p_parameter(self, p):
        """parameter : listOfParameters
        | """
        print("11")


    def p_listOfParameters(self, p):
        """listOfParameters : listOfParameters SEMICOLON paramTypeList
        | paramTypeList"""
        print("12")


    def p_paramTypeList(self, p):
        """paramTypeList : type paramList"""
        print("13")


    def p_paramList(self, p):
        """paramList :  paramList COMA paramId
        | paramId"""
        print("14")


    def p_localDeclarations(self, p):
        """localDeclarations : ScopedVariableDec localDeclarations
        | """
        print("15")

    def p_paramId(self, p):
        """paramId : LETTER
        | LETTER OPENING_BRACKET CLOSING_BRACKET"""
        print("16")


    def p_statement(self, p):
        """statement : phrase
        | compoundPhrase
        | selectPhrase
        | iterationPhrase
        | returnPhrase
        | continue"""
        print("17")


    def p_statement_without_bracket(self, p):
        """statementWithoutBracket : phrase
        | selectPhrase
        | iterationPhrase
        | returnPhrase
        | continue"""
        print("18")


    def p_compoundPhrase(self, p):
        """compoundPhrase : OPENING_BRACE localDeclarations  statementList CLOSING_BRACE"""
        print("19")


    def p_statementList(self, p):
        """statementList : statementList statement
        | """
        print("20")


    def p_phrase(self, p):
        """phrase : allExpression SEMICOLON
        | SEMICOLON"""
        print("21")


    def p_selectPhrase(self, p):
        """selectPhrase : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statementWithoutBracket
                        | IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statementWithoutBracket OTHER_KW statement
                        | IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES ifBodyWithBracket
                            """
        print("22")


    def p_ifBody(self, p):
        """ifBodyWithBracket : OPENING_BRACE ScopedVariableDec localDeclarations statementList CLOSING_BRACE
        | OPENING_BRACE statement statement statementList CLOSING_BRACE
        | OPENING_BRACE statement OTHER_KW statement statement CLOSING_BRACE
        | OPENING_BRACE statement statement OTHER_KW statement CLOSING_BRACE
        | OPENING_BRACE statement OTHER_KW statement statement OTHER_KW statement CLOSING_BRACE
        """
        print("23")


    def p_iterationPhrase(self, p):
        """iterationPhrase : TILL_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statement"""
        print("24")


    def p_returnPhrase(self, p):
        """returnPhrase : COMEBACK_KW SEMICOLON
        | GIVEBACK_KW allExpression SEMICOLON
        | GIVEBACK_KW numOrLetter SEMICOLON"""
        print("25")


    def p_continue(self, p):
        """continue : CONTINUE_KW SEMICOLON"""
        print("26")


    def p_allExpression(self, p):
        """allExpression : alterable mathOp allExpression
        | alterable PP_OP
        | alterable MM_OP
        | eachExpression"""
        print("27")


    def p_mathOp(self, p):
        """mathOp : EQ_OP
        | PLE_OP
        | MIE_OP
        | MUE_OP
        | DIE_OP"""
        print("28")


    def p_eachExpression(self, p):
        """eachExpression : eachExpression logicOp eachExpression
        | eachExpression logicOp THEN_KW eachExpression
        | logicOp eachExpression
        | relExpression
        | eachExpression logicOp ELSE_KW eachExpression"""
        print("29")


    def p_relExpression(self, p):
        """relExpression : mathEXP compareType mathEXP
        | mathEXP"""
        print("30")

#fargh dare
    def p_mathEXP(self, p):
        """mathEXP : mathEXP op mathEXP
        | unaryExpression"""
        print("31")


    def p_compareType(self, p):
        """compareType : equal
        | nonEqual"""
        print("32")


    def p_equal(self, p):
        """equal : LE_REL
        | GE_REL
        | EQ_REL"""
        print("33")


    def p_nonEqual(self, p):
        """nonEqual : GT_REL
        | LT_REL
        | NEQ_REL"""
        print("34")


    def p_op(self, p):
        """op : PL_OP
        | MI_OP
        | MU_OP
        | DI_OP
        | PE_OP"""
        print("35")


    def p_unaryExpression(self, p):
        """unaryExpression : unaryop unaryExpression
        | factor"""
        print("36")


    def p_unaryop(self, p):
        """unaryop : MI_OP
        | MU_OP
        | QU_UOP"""
        print("37")


    def p_factor(self, p):
        """factor : inalterable
        | alterable"""
        print("38")


    def p_alterable(self, p):
        """alterable : numOrLetter
        | alterable OPENING_BRACKET allExpression CLOSING_BRACKET
        | alterable LETTER"""
        print("39")

#TODO dot!
    def p_inalterable(self, p):
        """inalterable : OPENING_PARENTHESES allExpression CLOSING_PARENTHESES
        | constant
        | LETTER OPENING_PARENTHESES args CLOSING_PARENTHESES"""
        print("40")


    def p_args(self, p):
        """args : arguments
        | """
        print("41")


    def p_arguments(self, p):
        """arguments : arguments COMA allExpression
        | allExpression"""
        print("42")


    def p_constant(self, p):
        """constant : CONST_KW
        | TRUE
        | FALSE"""
        print("43")


    def p_logicOp(self, p):
        """logicOp : AA_LOP
        | OO_LOP
        | TIL_LOP
        | AND_LOP
        | OR_LOP"""
        print("44")


    def p_error(self, p):
        if p:
            print('syntax error in', p.lexpos)
        else:
            print('syntax error with nontype obj')
        #    for i in p:
        #        print(i)
        exit(5)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs, debug=True)
        return self.parser

if __name__ == '__main__':
    parser = Yacc().build()
    while True:
        try:
            s = input('parser> ')
        except EOFError:
            break
        parser.parse(s)

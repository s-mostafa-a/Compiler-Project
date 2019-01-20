from ply import yacc
from scripts import lexer


class Yacc:
    tokens = lexer.tokens

    def p_program(self, p):
        """program : list"""

    def p_numOrLetter(self, p):
        """numOrLetter : NUMBER
        | LETTER
        |
        """

    def p_list(self, p):
        """list : list declaration
        | declaration"""

    def p_declaration(self, p):
        """declaration : VOID_KW LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE localDeclarations statementList CLOSING_BRACE
        | VOID_KW LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES statementWithoutBracket
        | type LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACE localDeclarations statementList CLOSING_BRACE
        | type LETTER OPENING_PARENTHESES parameter CLOSING_PARENTHESES statementWithoutBracket
        | scopedSpecifier LETTER varInitialization SEMICOLON
        | scopedSpecifier LETTER varInitialization COMA variableList SEMICOLON"""
        #| STATIC_KW type LETTER varInitialization SEMICOLON
        #| STATIC_KW type LETTER varInitialization COMA variableList SEMICOLON
        #| type LETTER varInitialization SEMICOLON
        #| type LETTER varInitialization COMA variableList SEMICOLON """

    def p_ScopedVariableDec(self, p):
        """ScopedVariableDec : scopedSpecifier variableList SEMICOLON"""

    def p_variableList(self, p):
        """variableList : variableList COMA variableList
        | varInitialization"""

    def p_varInitialization(self, p):
        """varInitialization : varForm
        | varForm COLON OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES"""

    def p_varForm(self, p):
        """varForm : LETTER numOrLetter OPENING_BRACKET NUMBER CLOSING_BRACKET
        | LETTER  numOrLetter """
        # inja fahmidam id_uc yani LETTER  numOrLetter
    def p_scopedSpecifier(self, p):
        """scopedSpecifier : STATIC_KW type
        | type"""

    def p_type(self, p):
        """type : BOOLEAN_KW
        | CHARACTER_KW
        | INTEGER_KW
        | CHAR_KW
        | BOOL_KW
        | INT_KW"""

    def p_function(self, p):
        """function : VOID_KW numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES OPENING_BRACKET statement CLOSING_BRACKET
                    | type LETTER numOrLetter OPENING_PARENTHESES parameter CLOSING_PARENTHESES statement"""

    def p_parameter(self, p):
        """parameter : listOfParameters
        | """

    def p_listOfParameters(self, p):
        """listOfParameters : listOfParameters SEMICOLON paramTypeList
        | paramTypeList"""

    def p_paramTypeList(self, p):
        """paramTypeList : type paramList"""

    def p_paramList(self, p):
        """paramList :  paramList COMA paramId
        | paramId"""

    def p_localDeclarations(self, p):
        """localDeclarations : localDeclarations ScopedVariableDec
        | """

    def p_paramId(self, p):
        """paramId : LETTER numOrLetter
        | LETTER numOrLetter OPENING_BRACKET CLOSING_BRACKET"""

    def p_statement(self, p):
        """statement : phrase
        | compoundPhrase
        | selectPhrase
        | iterationPhrase
        | returnPhrase
        | continue"""

    def p_compoundPhrase(self, p):
        """compoundPhrase : OPENING_BRACE localDeclarations  statementList CLOSING_BRACE"""

    def p_statementList(self, p):
        """statementList : statementList statement
        | """

    def p_phrase(self, p):
        """phrase : allExpression SEMICOLON
        | SEMICOLON"""

    def p_selectPhrase(self, p):
        """selectPhrase : IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES ifBody
                        | IF_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES OPENING_BRACE ifBody ifBody CLOSING_BRACE"""

    def p_ifBody(self, p):
        """ifBody : statement
        | statement OTHER_KW statement
        | SEMICOLON"""

    def p_iterationPhrase(self, p):
        """iterationPhrase : TILL_KW OPENING_PARENTHESES eachExpression CLOSING_PARENTHESES statement"""

    def p_returnPhrase(self, p):
        """returnPhrase : COMEBACK_KW SEMICOLON
        | GIVEBACK_KW allExpression SEMICOLON
        | GIVEBACK_KW numOrLetter SEMICOLON"""

    def p_continue(self, p):
        """continue : CONTINUE_KW SEMICOLON"""

    def p_allExpression(self, p):
        """allExpression : alterable mathOp allExpression
        | alterable PP_OP
        | alterable MM_OP
        | eachExpression
        | alterable mathOp alterable"""

    def p_mathOp(self, p):
        """mathOp : EQ_OP
        | PLE_OP
        | MIE_OP
        | MUE_OP
        | DIE_OP"""

    def p_eachExpression(self, p):
        """eachExpression : eachExpression logicOp eachExpression
        | eachExpression logicOp THEN_KW eachExpression
        | logicOp eachExpression
        | relExpression
        | eachExpression logicOp ELSE_KW eachExpression"""

    def p_relExpression(self, p):
        """relExpression : mathEXP compareType mathEXP
        | mathEXP"""

    def p_compareType(self, p):
        """compareType : equal
        | nonEqual"""

    def p_equal(self, p):
        """equal : LE_REL
        | GE_REL
        | EQ_REL"""

    def p_nonEQ_OP(self, p):
        """nonEqual : GT_REL
        | LT_REL
        | NEQ_REL"""

    def p_mathEXP(self, p):
        """mathEXP : mathEXP op mathEXP
        | unaryExpression"""

    def p_op(self, p):
        """op : PL_OP
        | MI_OP
        | MU_OP
        | DI_OP
        | PE_OP"""

    def p_unaryExpression(self, p):
        """unaryExpression : unaryop unaryExpression
        | factor"""

    def p_unaryop(self, p):
        """unaryop : MI_OP
        | MU_OP
        | QU_UOP"""

    def p_factor(self, p):
        """factor : inalterable
        | alterable"""

    def p_alterable(self, p):
        """alterable : LETTER numOrLetter
        | alterable OPENING_BRACKET allExpression CLOSING_BRACKET
        | alterable LETTER numOrLetter"""

    def p_inalterable(self, p):
        """inalterable : OPENING_PARENTHESES allExpression CLOSING_PARENTHESES
        | constant
        | LETTER numOrLetter OPENING_PARENTHESES args CLOSING_PARENTHESES"""

    def p_args(self, p):
        """args : arguments
        | """

    def p_arguments(self, p):
        """arguments : arguments COMA allExpression
        | allExpression"""

    def p_constant(self, p):
        """constant : CONST_KW
        | TRUE
        | FALSE"""

    def p_logicOp(self, p):
        """logicOp : AA_LOP
        | OO_LOP
        | TIL_LOP
        | AND_LOP
        | OR_LOP"""

    def p_error(self, p):
        print('syntax error')
        exit(5)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

if __name__ == '__main__':
    parser = Yacc().build()
    while True:
        try:
            s = input('parser> ')
        except EOFError:
            break
        parser.parse(s)

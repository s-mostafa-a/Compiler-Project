import codecs
import sys

from ply import yacc
from scripts import lexer
from ply.yacc import yaccdebug


class Yacc:
    tokens = lexer.tokens

    precedence = (
        ('nonassoc', 'Opening_Parentheses'),  # Nonassociative operators
        ('nonassoc', 'Other_KW'),  # Nonassociative operators
        ('left', 'Then_KW'),
        ('left', 'Else_KW'),
        ('left', 'DoubleAnd', 'DoubleOr', 'Tilda', 'And_KW', 'Or_KW'),
        ('left', 'Equal', 'PlusEqual', 'MinusEqual', 'TimesEqual', 'DivideEqual'),
        ('left', 'Plus', 'Minus', 'Times', 'Divide', 'ModeOP'),
        ('left', 'Minus', 'Times', 'QMark'),
    )


    def p_program(self, p):
        """program :list"""
        print("program : list")

    def p_numOrLetter_num(self, p):
        """numOrLetter : Num"""
        print("numOrLetter : Num")
    def p_numOrLetter_idLetter(self, p):
        """numOrLetter : idLetter"""
        print("numOrLetter : idLetter")

    def p_list(self, p):
        """list : list declaration
        | declaration"""
        if len(p)==3:
            print("list : list declaration")
        else:
            print("list : declaration ")

    def p_declaration_idNum(self, p):
        """declaration : void_KW idNum Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace
                    | type idNum Opening_Parentheses parameter Closing_Parentheses statement
                    """
        if len(p)==7:
            print("declaration : type idNum Opening_Parentheses parameter Closing_Parentheses statement")
        else:
            print("declaration : void_KW idNum Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace ")

    def p_declaration_idLetter(self, p):
        """declaration :  void_KW idLetter Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace
                    | type idLetter Opening_Parentheses parameter Closing_Parentheses statement
                    | type  variableList Semicolon"""
        if len(p)==4:
            print("declaration : type  variableList Semicolon")
        elif len(p) == 7:
            print("declaration : type idLetter Opening_Parentheses parameter Closing_Parentheses statement")
        else:
            print("declaration : void_KW idLetter Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace")

    def p_variableList(self, p):
        """variableList : variableList Comma varInitialization
        | varInitialization"""
        if len(p) == 2:
            print("variableList : varInitialization")
        else:
            print(
                "variableList : variableList Comma varInitialization")

    def p_varInitialization(self, p):
        """varInitialization : varForm
        | varForm Colon Opening_Parentheses eachExpression Closing_Parentheses"""
        if len(p) == 2:
            print("varInitialization : varForm")
        else:
            print(
                "varInitialization : varForm Colon Opening_Parentheses eachExpression Closing_Parentheses")

    def p_varForm(self, p):
        """varForm : idLetter Opening_Bracket Num Closing_Bracket
        | idLetter """
        if len(p) == 2:
            print("varForm : idLetter ")
        else:
            print(
                "varForm : idLetter Opening_Bracket Num Closing_Bracket")


    def p_type(self, p):
        """type : Boolean_KW
        | Character_KW
        | Integer_KW
        | char_KW
        | bool_KW
        | int_KW"""
        print("type : someTypeKeyWord")

    def p_parameter(self, p):
        """parameter : listOfParameters
        | """
        if(len(p)==2):
            print("parameter : listOfParameters")
        else:
            print("parameter : ")

    def p_listOfParameters(self, p):
        """listOfParameters : listOfParameters Semicolon paramTypeList
        | paramTypeList"""
        if (len(p) == 2):
            print("listOfParameters : listOfParameters Semicolon paramTypeList")
        else:
            print("listOfParameters : paramTypeList")

    def p_paramTypeList(self, p):
        """paramTypeList : type paramList"""
        print("paramTypeList : type paramList")

    def p_paramList(self, p):
        """paramList :  paramList Comma paramId
        | paramId"""
        if(len(p)==4):
            print("paramList :  paramList Comma paramId")
        else:
            print("paramList :  paramId")

    def p_localDeclarations(self, p):
        """localDeclarations : localDeclarations Static_KW type variableList Semicolon
        | localDeclarations type variableList Semicolon
        | """
        if(len(p)==5):
            print("localDeclarations :  localDeclarations type variableList Semicolon")
        elif(len(p)==6):
            print("localDeclarations : localDeclarations Static_KW type variableList Semicolon")
        else:
            print("localDeclarations : ")

    def p_paramId(self, p):
        """paramId : idLetter
        | idLetter Opening_Bracket Closing_Bracket"""
        if(len(p)==2):
            print("paramId : idLetter")
        else:
            print("paramId : idLetter Opening_Bracket Closing_Bracket")

    def p_statementList(self, p):
        """statementList :  statement statementList
        | """
        if(len(p)==3):
            print("statementList :  statement statementList")
        else:
            print("statementList :  ")


    def p_statement_phrase(self, p):
        """statement : phrase
        """

        print("statement : phrase")
    def p_statement_compoundphrase(self, p):
        """statement : compoundPhrase
        """
        print("statement : compoundPhrase")
    def p_statement_selectphrase(self, p):
        """statement : selectPhrase
        """
        print("statement : selectPhrase")
    def p_statement_iterationphrase(self, p):
        """statement : iterationPhrase
        """
        print("statement : iterationPhrase")
    def p_statement_returnphrase(self, p):
        """statement : returnPhrase"""
        print("statement : returnPhrase")
    def p_statement_continue(self, p):
        """statement : continue"""
        print("statement : continue")

    def p_compoundPhrase(self, p):
        """compoundPhrase : Opening_Brace localDeclarations  statementList Closing_Brace"""
        print("compoundPhrase : Opening_Brace localDeclarations  statementList Closing_Brace")


    def p_phrase(self, p):
        """phrase : allExpression Semicolon
        | Semicolon"""
        if(len(p)==3):
            print("phrase : allExpression Semicolon")
        else:
            print("phrase : Semicolon")

    def p_selectPhrase(self, p):
        """selectPhrase : If_KW Opening_Parentheses eachExpression Closing_Parentheses ifBody
                        | If_KW Opening_Parentheses eachExpression Closing_Parentheses Opening_Brace ifBody ifBody Closing_Brace"""
        if(len(p)==6):
            print("selectPhrase : If_KW Opening_Parentheses eachExpression Closing_Parentheses ifBody")
        else:
            print("selectPhrase : If_KW Opening_Parentheses eachExpression Closing_Parentheses Opening_Brace ifBody ifBody Closing_Brace")


    def p_ifBody(self, p):
        """ifBody : statement
        | statement Other_KW statement
        """
        if(len(p)==2):
            print("ifBody : statement")
        else:
            print("ifBody : statement Other_KW statement")


    def p_ifBody_semicolon(self, p):
        """ifBody : Semicolon"""
        print("ifBody : Semicolon")

    def p_iterationPhrase(self, p):
        """iterationPhrase : Till_KW Opening_Parentheses eachExpression Closing_Parentheses statement"""
        print("iterationPhrase : Till_KW Opening_Parentheses eachExpression Closing_Parentheses statement")

    def p_returnPhrase_cs(self, p):
        """returnPhrase : ComeBack_KW Semicolon"""
        print("returnPhrase : ComeBack_KW Semicolon")

    def p_returnPhrase_gas(self, p):
        """returnPhrase : GiveBack_KW allExpression Semicolon"""
        print("returnPhrase : GiveBack_KW allExpression Semicolon")

    def p_returnPhrase_gns(self, p):
        """returnPhrase : GiveBack_KW numOrLetter Semicolon"""
        print("returnPhrase : GiveBack_KW numOrLetter Semicolon")

    def p_continue(self, p):
        """continue : Continue_KW Semicolon"""
        print("continue : Continue_KW Semicolon")

    def p_allExpression_a(self, p):
        """allExpression : alterable mathOp allExpression"""
        print("allExpression : alterable mathOp allExpression")

    def p_allExpression_pp(self, p):
        """allExpression : alterable PP"""
        print("allExpression : alterable PP")

    def p_allExpression_mm(self, p):
        """allExpression : alterable MM"""
        print("allExpression : alterable MM")

    def p_allExpression_e(self, p):
        """allExpression : eachExpression"""
        print("allExpression : eachExpression")

    def p_allExpression_ama(self, p):
        """allExpression : alterable mathOp alterable"""
        print("allExpression : alterable mathOp alterable")

    def p_mathOp_e(self, p):
        """mathOp : Equal"""
        print("mathOp : Equal")

    def p_mathOp_p(self, p):
        """mathOp : PlusEqual"""
        print("mathOp : PlusEqual")

    def p_mathOp_mi(self, p):
        """mathOp : MinusEqual"""
        print("mathOp : MinusEqual")

    def p_mathOp_t(self, p):
        """mathOp : TimesEqual"""
        print("mathOp : TimesEqual")

    def p_mathOp_d(self, p):
        """mathOp : DivideEqual"""
        print("mathOp : DivideEqual")

    def p_eachExpression_e(self, p):
        """eachExpression : eachExpression logicOp eachExpression"""
        print("eachExpression : eachExpression logicOp eachExpression")

    def p_eachExpression_et(self, p):
        """eachExpression : eachExpression logicOp Then_KW eachExpression"""
        print("eachExpression : eachExpression logicOp Then_KW eachExpression")

    def p_eachExpression_l(self, p):
        """eachExpression : logicOp eachExpression"""
        print("eachExpression : logicOp eachExpression")

    def p_eachExpression_r(self, p):
        """eachExpression : relExpression"""
        print("eachExpression : relExpression")

    def p_eachExpression_ele(self, p):
        """eachExpression : eachExpression logicOp Else_KW eachExpression"""
        print("eachExpression : eachExpression logicOp Else_KW eachExpression")

    def p_relExpression_c(self, p):
        """relExpression : mathEXP compareType mathEXP"""
        print("relExpression : mathEXP compareType mathEXP")
        p[0] = p[1] + str(p[2]) + p[3]

    def p_relExpression_m(self, p):
        """relExpression : mathEXP"""
        print("relExpression : mathEXP")

    def p_compareType_e(self, p):
        """compareType : equal"""
        print("compareType : equal")

    def p_compareType_n(self, p):
        """compareType : nonEqual"""
        print("compareType : nonEqual")

    def p_equal_l(self, p):
        """equal : LEqual"""
        print("equal : LEqual")

    def p_equal_g(self, p):
        """equal : GEqual"""
        print("equal : GEqual")


    def p_equal_e(self, p):
        """equal : EEqual"""
        print("equal : EEqual")


    def p_nonEqual_g(self, p):
        """nonEqual : GreaterOP"""
        print("nonEqual : GreaterOP")


    def p_nonEqual_l(self, p):
        """nonEqual : LessOP"""
        print("nonEqual : LessOP")


    def p_nonEqual_n(self, p):
        """nonEqual : NonEqualOP"""
        print("nonEqual : NonEqualOP")


    def p_mathEXP_u(self, p):
        """mathEXP : unaryExpression"""
        print("mathEXP : unaryExpression")


    def p_mathEXP_m(self, p):
        """mathEXP : mathEXP op mathEXP"""
        print("mathEXP : mathEXP op mathEXP")
        p[0] = p[1] + str(p[2]) + p[3]



    def p_op_p(self, p):
        """op : Plus"""
        print("op : Plus")


    def p_op_m(self, p):
        """op : Minus"""

        print("op : Minus")


    def p_op_t(self, p):
        """op : Times"""
        print("op : Times")


    def p_op_d(self, p):
        """op : Divide"""
        print("op : Divide")


    def p_op_mo(self, p):
        """op : ModeOP"""
        print("op : ModeOP")


    def p_unaryExpression_u(self, p):
        """unaryExpression : unaryop unaryExpression"""
        print("unaryExpression : unaryop unaryExpression")


    def p_unaryExpression_f(self, p):
        """unaryExpression : factor"""
        print("unaryExpression : factor")


    def p_unaryop_m(self, p):
        """unaryop : Minus"""
        print("unaryop : Minus")


    def p_unaryop_t(self, p):
        """unaryop : Times"""
        print("unaryop : Times")


    def p_unaryop_q(self, p):
        """unaryop : QMark"""
        print("unaryop : QMark")


    def p_factor_i(self, p):
        """factor : inalterable"""
        print("factor : inalterable")

    def p_factor_a(self, p):
        """factor : alterable"""
        print("factor : alterable")


    def p_alterable_n(self, p):
        """alterable : numOrLetter"""
        print("alterable : numOrLetter")


    def p_alterable_a(self, p):
        """alterable : alterable Opening_Bracket allExpression Closing_Bracket"""
        print("alterable : alterable Opening_Bracket allExpression Closing_Bracket")


    def p_alterable_ad(self, p):
        """alterable : alterable Dot numOrLetter"""
        print("alterable : alterable Dot numOrLetter")


    def p_inalterable_o(self, p):
        """inalterable : Opening_Parentheses allExpression Closing_Parentheses"""
        print("inalterable : Opening_Parentheses allExpression Closing_Parentheses")


    def p_inalterable_c(self, p):
        """inalterable : constant"""
        print("inalterable : constant")


    def p_inalterable_i(self, p):
        """inalterable : idLetter Opening_Parentheses args Closing_Parentheses"""
        print("inalterable : idLetter Opening_Parentheses args Closing_Parentheses")


    def p_args_a(self, p):
        """args : arguments"""
        print("args : arguments")


    def p_args_e(self, p):
        """args : """
        print("args : ")


    def p_arguments_ar(self, p):
        """arguments : arguments Comma allExpression"""
        print("arguments : arguments Comma allExpression")


    def p_arguments_al(self, p):
        """arguments : allExpression"""
        print("arguments : allExpression")


    def p_constant_C(self, p):
        """constant : Const_KW"""
        print("constant : Const_KW")


    def p_constant_T(self, p):
        """constant : True_KW"""
        print("constant : True_KW")


    def p_constant_F(self, p):
        """constant : False_KW"""
        print("constant : False_KW")


    def p_logicOp_DA(self, p):
        """logicOp : DoubleAnd"""
        print("logicOp : DoubleAnd")


    def p_logicOp_DO(self, p):
        """logicOp : DoubleOr"""
        print("logicOp : DoubleOr")


    def p_logicOp_T(self, p):
        """logicOp : Tilda"""
        print("logicOp : Tilda")


    def p_logicOp_A(self, p):
        """logicOp : And_KW"""
        print("logicOp : And_KW")


    def p_logicOp_O(self, p):
        """logicOp : Or_KW"""
        print("logicOp : Or_KW")

    def p_error(self, p):
        stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

        print('Syntax error in input! Parser State:{} {} . {}'
              .format(parser.state,
                      stack_state_str,
                      p))
        exit(5)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs, debug=True)
        return self.parser


if __name__ == '__main__':
    yacc = Yacc().build()
    parser = yacc
    for i in range(5):
        orig_stdout = sys.stdout
        out = open('./../phase2/test_case{0}_answer.txt'.format(i+1), 'w')
        sys.stdout = out
        f = codecs.open('./../phase2/test_case{0}.code'.format(i+1), encoding='utf-8')
        parser.parse(f.read())
        f.close()


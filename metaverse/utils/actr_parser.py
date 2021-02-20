import pyparsing as pp
from pyparsing import *



'''

ACT-R model file from http://act-r.psy.cmu.edu/actr7/reference-manual.pdf

(clear-all)
{Lisp functions for presenting an experiment, data collection or other support needs}
(define-model model-name
 (sgp {parameter value}*)
 {chunk-type definitions}
 {initial chunks are defined}
 {productions are specified}
 {any additional model set-up commands}
 {additional model parameter settings}
)

An informal BN grammar for ACT-R model files:

model ::= clear-all lisp-functions define-model
clear-all ::=  '(clear-all)'
lisp-functions ::= '{' alphas+ '}'


'''

# identifier = Word(alphas, alphanums+'_')
# number = Word(nums+".")

# integer  = Word(nums)            # simple unsigned integer
# variable = Char(alphas)          # single letter variable, such as x, z, m, etc.
# arithOp  = oneOf("+ - * /")      # arithmetic operators
# equation = variable + "=" + integer + arithOp + integer    # will match "x=2+2", etc.

lparen = pp.Suppress("(")
rparen = pp.Suppress(")")

clear = "(" + "clear-all" + ")"

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()



def parseFile(filename: str):
    '''
    From example: https://stackoverflow.com/questions/52666229/parse-a-multiline-text-with-pyparsing
    '''

    global FileSyntax

    print("\nparse results:\n")

    try:

        TestFile = open(filename)
        testdata = "".join(TestFile.readlines())
        FileSyntax = Grammar()
        FileSyntax.parseString(testdata)

    except ParseException as err:

        print(err.line)
        print(" " * (err.column - 1) + "^")
        print("* " + str(err))

    except Exception as e:
        import traceback
        traceback.print_exc(e)

def pprint_model():
    import pprint
    # isrecursive = pprint.isrecursive(result.asList())
    # print("recursive?: " + str(isrecursive))

    branch_num = 1
    for branch in model_tree.asList():
        print('\n' + "branch: " + str(branch_num))
        pprint.pprint(branch)
        branch_num += 1

if __name__ == '__main__':
    ##directory = '..\\Environments\\StarCraft2'
    directory = '.'
    infile = 'cmu_count_test.lisp'
    #fd = open(directory + '/' + infile, encoding='utf8')

    #testdata = fd.read()

    # primitives
    NL = Suppress(LineEnd())
    alpha_nums = Word(alphanums)
    alpha_nums_dash = Word(alphanums)
    dash = Literal("-")

    simple_punc = Word("-./_:*+=")
    token = Combine(OneOrMore(alpha_nums) + ZeroOrMore(Literal('-')) + ZeroOrMore(alpha_nums))
    # TODO: Forward() declaration for recursive match
    comment = Literal("\"") + OneOrMore(token) + Literal("\"")
    simple_param = alphanums | simple_punc
    tokenlist = lparen + Group(OneOrMore(token)) + rparen

    # (clear-all)
    clear_cmd = Literal("(clear-all)")

    # {Lisp functions for presenting an experiment, data collection or other support needs}

    # (define-model model-name
    define_model_cmd = lparen + Group(Literal("define-model") + token)

    # (sgp {parameter value}*)
    sgp_key = Literal(':').suppress() + token
    sgp_val = Optional('.') + token
    sgp_pair = sgp_key + sgp_val
    sgp_cmd = lparen + Literal("sgp").suppress() + Group(OneOrMore(sgp_pair)) + rparen
    sgp_cmd.setResultsName("sgp_cmd")

    # {chunk-type definitions}

    chunk_type = Group(lparen + Literal("chunk-type") + OneOrMore(token) + rparen)
    chunk_block = Group(OneOrMore(chunk_type))

    # {initial chunks are defined}
    add_dm = Group(lparen + Literal("add-dm") + OneOrMore(tokenlist) + rparen).setResultsName("DeclarativeMemory")

    # *** productions are specified ***

    # [Description]
    '''     
    # Variables are symbols which start with an “=” character e.g. =slot, =answer, =goal \
    # Constants are symbols used in the production for values which are not variables are \ 
    assumed to be the names of chunks
    # Modifiers (integers): =, - , <, >, <=, and >=
    '''
    buffer = token

    # [ISA]
    '''chunk-type specification is only used during the definition of the production \
    and does not directly affect the condition or action in which it occurs.'''

    # [Conditions]
    'also referred to as the production’s left hand side (LHS).'

    ''' [[Buffer test: starts with a variable that names the buffer followed by the ‘>’ character]] \
    # A query starts with a symbol composed of a ‘?’, the name of the buffer being queried, \
    and the symbol ‘>’. '''

    # TODO: test for buffer queries (i.e. [buffer/state/error][empty/full/failure])
    # TODO: !eval! statement for arbitrary logging
    # TODO: !bind! statement for to save evals to a variable

    # [Actions]
    'When a production fires it executes all of its actions, which are also referred to as its \
    right hand side (RHS)'

    # [[ buffer modification ]]
    '''used to change the slot values of a chunk in a buffer. \
    # name the buffer to be modified by using a symbol composed of the ‘=’ character, the name \
    of the buffer and the ‘>’ character. '''

    chunk_name = token
    chunk_variable = Literal('=') + token
    chunk_value = token
    slot_name = token
    # bound_slot_value = token

    slot_value = chunk_variable | chunk_value
    slot_value_pair = slot_name + slot_value

    # slot_modifier = Literal("=") | Literal("-") | Literal("<") | Literal(">") | Literal("<=") | Literal(">=")
    slot_modifier = oneOf("= - < > <= >=")

    slot_test = Group(Optional(slot_modifier) \
                      + slot_name.setResultsName("slot-name") \
                      + slot_value.setResultsName("slot-value")).setResultsName("slot")

    isa_test = oneOf("isa ISA") + chunk_name
    # buff_test_cmd = buff_test + Optional(buffer_test) + OneOrMore(slot_test)

    buff_test_cmd = Literal('=') + buffer + Literal('>')
    buff_mod_cmd = Literal('-') + buffer.setResultsName("buffer") + Literal('>')
    buff_clear_cmd = Literal('*') + buffer + Literal('>')
    buff_overwrite_cmd = Literal('@') + buffer + Literal('>')
    buff_request_cmd = Literal('+') + buffer + Literal('>')
    buff_query_cmd = Literal('?') + buffer + Literal('>')

    output_cmd = Group(Literal('!output!') + lparen + slot_value + rparen)

    # LHS options

    # condition: := [buffer-test | query | eval | binding | multiple-value- binding]

    # RHS options
    prod_action = buff_mod_cmd | buff_request_cmd | buff_clear_cmd | buff_mod_cmd | output_cmd

    # TODO: implement buffer-overwrite | binding | multiple-value-binding |  !stop!

    prod_command = Group(buff_test_cmd | buff_request_cmd \
                         | buff_clear_cmd | buff_overwrite_cmd \
                         | buff_mod_cmd \
                         ).setResultsName("Prod Cmd")
    prod_name = token

    prod_condition = Group((prod_command + OneOrMore(slot_test)) | output_cmd)
    conditions = Group(OneOrMore(prod_condition)).setResultsName("Conditions")

    actions = Group(OneOrMore(prod_condition)).setResultsName("Actions")

    # TODO: implement production doc-string

    # prod_rule = lparen + oneOf("p P")+ prod_name + conditions + Literal('==>') + actions
    prod_rule = lparen + Group(oneOf("p P") + prod_name \
                               + conditions.setResultsName("conditions") \
                               + Literal('==>') \
                               + actions.setResultsName("actions")).setResultsName("Prod Rule") \
                + rparen

    # OneOrMore(simple_param) + \
    # rparen

    productions = OneOrMore(prod_rule).setResultsName("Productions")

    # {any additional model set-up commands}

    chunk_name = token
    goal_focus = lparen + Group(Literal("goal-focus") + chunk_name) + rparen

    # {additional model parameter settings}

    # end define-model with Literal(')')

    localtest = '''
        (clear-all)       

        (define-model count

        (sgp :esc t :lf .05 :trace-detail high)

        (chunk-type count-order first second)
        (chunk-type count-from start end count)

        (add-dm
        (b ISA count-order first 1 second 2)
        (c ISA count-order first 2 second 3)
        (d ISA count-order first 3 second 4)
        (e ISA count-order first 4 second 5)
        (f ISA count-order first 5 second 6)
        (first-goal ISA count-from start 2 end 4))

        (goal-focus first-goal)

        (p start
           =goal>
              ISA         count-from
              start       =num1
              count       nil
        ==>
           =goal>
              ISA         count-from
              count       =num1
           +retrieval>
              ISA         count-order
              first       =num1
        )

        (P increment
           =goal>
              ISA         count-from
              count       =num1
            - end         =num1
           =retrieval>
              ISA         count-order
              first       =num1
              second      =num2
         ==>
           =goal>
              ISA         count-from
              count       =num2
           +retrieval>
              ISA         count-order
              first       =num2
           !output!       (=num1)
        )

        )                
    '''

    # Line = Optional('(') + OneOrMore(token) + Optional(')')
    # Lines = OneOrMore(Group(Line))

    # productions.setResultsName("productions")

    # model_tree = productions.parseString(prodtest)

    model_file = Group(clear_cmd \
                       + define_model_cmd \
                       + sgp_cmd \
                       + chunk_block \
                       + add_dm \
                       + goal_focus \
                       + productions).setResultsName("Model")

    model_tree = model_file.parseString(localtest)

    # model_tree = parseString(localtest)
    # model_tree = prod_rule.parseString(prodtest)

    import pprint
    # print("Declarative Memory:")
    stuff = model_tree
    # pprint.pprint(model_tree.dm)

    pprint_model()

    print(model_tree.asXML())

#End class ACTParser()

import logging
log = logging.getLogger(__name__)
def add_subcommand_hello(subparsers):
    parser = subparsers.add_parser('how-to')
    parser.set_defaults(func=hello)

def hello(args):
    log.info(' Calculator Welcome')
    log.info('   Hello, welcome to the CLI fraction processor.')
    log.info('   A command-line program that will take equations with whole numbers/mixed numbers/fractions as an input and produce a fractional result.')
    log.info('')
    log.info(' Information regarding calculator')
    log.info('   Legal operators shall be *, /, +, - (multiply, divide, add, subtract)')
    log.info('   Operands and operators shall be separated by one or more spaces')
    log.info('   Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"')
    log.info('   Improper fractions and whole numbers are also allowed as operands ')
    log.info('   Only two operands are allowed')
    log.info('')
    log.info(' Example run:')
    log.info('')
    log.info('   python -m process calc \'1/2 * 3_3/4\'')
    log.info('   1_7/8')
    log.info('')
    log.info('   python -m process calc \'2_3/8 + 9/8\'')
    log.info('   3_1/2')
    log.info('')
    log.info(' Loglevel details:')
    log.info('   There are also different loglevels utilized. I utilized loglevel debug to track debugging the system.')
    log.info('   Example run: python -m process --loglevel debug calculate_mixed \'2_3/8 + 9/8\'')

'''
Coding Challenge. 
Write a command-line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.
Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
Operands and operators shall be separated by one or more spaces
Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
Improper fractions and whole numbers are also allowed as operands 
Example run:
? 1/2 * 3_3/4
= 1_7/8? 2_3/8 + 9/8
= 3_1/2
'''
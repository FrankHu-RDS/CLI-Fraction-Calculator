import logging
import sys
import math

log = logging.getLogger(__name__)

def add_subcommand_calc(subparsers):
    parser = subparsers.add_parser('calc')
    parser.add_argument('equation', type=str)
    parser.set_defaults(func=calc)


def check_fraction(number):
    if '/' in number and len(number) != 1:
        return True
    return False

def process_fraction(process_fraction):
    if process_fraction is None:
        return None,None
    if '/' not in process_fraction:
        return process_fraction, 1
    
    fraction = process_fraction.split('/')
    num = fraction[0]
    denom = fraction[1]
    return num,denom

def mixed_number(number):
    if '_' in number:
        return True
    return False
    
def process_mixed_numbers(equation_parsed):
    # three kinds of numbers, mixed, fraction, whole
    # We will convert both numbers to fractions. 
    for index in range(len(equation_parsed)):
        is_fraction = check_fraction(equation_parsed[index])
        is_mixed_number = mixed_number(equation_parsed[index])
        if is_mixed_number and is_fraction: # mixed
            # split up via number and fraction, for example 3_3/4, break it up into 3 and 3/4
            broken_mixed_number = equation_parsed[index].split('_')
            whole = broken_mixed_number[0]
            # process fraction
            fraction = broken_mixed_number[1]
            numerator, denominator = process_fraction(fraction)
            numerator = int(numerator) + (int(whole)*int(denominator))
            equation_parsed[index] = str(numerator) + '/' + str(denominator)
        elif is_fraction: # fraction, we don't need to do anything.
            pass
        elif is_mixed_number: # mixed number with no fraction improperly formatted.
            raise ValueError('Improperly formatted equation')
            pass
        else: # Number is a whole number, or a calculation sign
            pass
        log.debug('      processed - ' + str(equation_parsed[index]))
    
def convert_fraction_to_mixed(numerator, denominator):
    log.debug('      Debug Log end numerator - ' + str(numerator))
    log.debug('      Debug Log end denominator - ' + str(denominator))
    new_numerator = abs(numerator) % denominator
    whole = math.trunc(numerator/denominator)
    log.debug('      Debug Log end whole- ' + str(whole))
    if new_numerator == 0:
        return str(whole)
    if whole != 0:
        return str(whole) + '_' + str(new_numerator) + '/' + str(denominator)
    else:
        return str(numerator) + '/' + str(denominator)

def find_lcm(denominator_1, denominator_2):
    denom_1 = int(denominator_1)
    denom_2 = int(denominator_2)
    if denom_1 > denom_2:
       greater = denom_1
    else:
       greater = denom_2
    while(True):
       if((greater % denom_1 == 0) and (greater % denom_2 == 0)):
           lcm = greater
           break
       greater += 1
    return lcm

def process_equation(equation_parsed):
    numerator_0, denominator_0 = process_fraction(equation_parsed[0])
    numerator_1, denominator_1 = process_fraction(equation_parsed[2])
    numerator_0, denominator_0 = int(numerator_0), int(denominator_0)
    numerator_1, denominator_1 = int(numerator_1), int(denominator_1)
    lcm = find_lcm(denominator_0, denominator_1)
    log.debug('         LCM: ' + str(lcm))
    if equation_parsed[1] == '*':
        # multiplying fractions is straightforward
        new_numerator = numerator_0 * numerator_1
        new_denominator = denominator_0 * denominator_1
        return str(new_numerator) + '/' + str(new_denominator)
    elif equation_parsed[1] == '/':
        # dividing fractions is same as multiplying number_1 by the reciprocal of number_2, 
        new_numerator = numerator_0 * denominator_1
        new_denominator = denominator_0 * numerator_1
        return str(new_numerator) + '/' + str(new_denominator)
    elif equation_parsed[1] == '+':
        # adding fractions requires making the denominators the same. 
        # to make denominator the same we can use 
        # 1. Common Denominator Method, or the
        # 2. Least Common Denominator Method
        # I will use Least Common Denominator here
        if lcm == denominator_0 and lcm == denominator_1:
            # they're the same denominator no conversion needs to occur
            new_numerator_0 = numerator_0
            new_denominator_0 = denominator_0
            new_numerator_1 = numerator_1
            new_denominator_1 = denominator_1
            pass
        elif lcm == denominator_0:
            new_numerator_1 = numerator_1 * (denominator_0 // denominator_1)
            new_denominator_1 = denominator_0 
            new_numerator_0 = numerator_0
            new_denominator_0 = denominator_0
        elif lcm == denominator_1:
            new_numerator_0 = numerator_0 * (denominator_1 // denominator_0)
            new_denominator_0 = denominator_1
            new_numerator_1 = numerator_1
            new_denominator_1 = denominator_1
        else:
            new_numerator_0 = numerator_0 * lcm
            new_numerator_1 = numerator_1 * lcm
            new_denominator_0 = denominator_0 * lcm
            new_denominator_1 = denominator_1 * lcm
        
        new_numerator = new_numerator_0 + new_numerator_1
        new_denominator = new_denominator_0
        return str(new_numerator) + '/' + str(new_denominator)
    elif equation_parsed[1] == '-':
        if lcm == denominator_0 and lcm == denominator_1:
            # they're the same denominator no conversion needs to occur
            new_numerator_0 = numerator_0
            new_denominator_0 = denominator_0
            new_numerator_1 = numerator_1
            new_denominator_1 = denominator_1
            pass
        elif lcm == denominator_0:
            new_numerator_1 = numerator_1 * (denominator_0 // denominator_1)
            new_denominator_1 = denominator_0 
            new_numerator_0 = numerator_0
            new_denominator_0 = denominator_0
        elif lcm == denominator_1:
            new_numerator_0 = numerator_0 * (denominator_1 // denominator_0)
            new_denominator_0 = denominator_1
            new_numerator_1 = numerator_1
            new_denominator_1 = denominator_1
        else:
            new_numerator_0 = numerator_0 * lcm
            new_numerator_1 = numerator_1 * lcm
            new_denominator_0 = denominator_0 * lcm
            new_denominator_1 = denominator_1 * lcm
        
        new_numerator = new_numerator_0 - new_numerator_1
        new_denominator = new_denominator_0
        return str(new_numerator) + '/' + str(new_denominator)

def calc(args):
    log.debug('   calculating')
    log.debug('   ' + str(args.equation))
    equation_parsed = args.equation.split()

    if len(equation_parsed)  < 2:
        sys.stdout.write("Too few arguments, can only process 2 operands at a time, please enter a properly formatted equation")
        return "Too few arguments, can only process 2 operands at a time."
    if len(equation_parsed) > 3:
        sys.stdout.write("Too few arguments, can only process 2 operands at a time.")
        return "Too many arguments, can only process 2 operands at a time."
    
    if equation_parsed[2] == '0' and equation_parsed[1] == '/':
        sys.stdout.write('error cannot divide by 0')
        return
    log.debug('   ' + str(list(equation_parsed)))

    log.debug('      process mixed numbers into fractions')
    process_mixed_numbers(equation_parsed)
    log.debug('      ' + str(equation_parsed))

    try:
        numerator_0, denominator_0 = process_fraction(equation_parsed[0])
        numerator_1, denominator_1 = process_fraction(equation_parsed[2])
        if denominator_1 == '0' or denominator_0 == '0':
            sys.stdout.write('error cannot divide by 0')
            return
        int(numerator_0)
        int(numerator_1)
        int(denominator_0)
        int(denominator_1)
        if equation_parsed[1] == '/' or equation_parsed[1] == '+' or equation_parsed[1] == '*' or equation_parsed[1] == '-':
            pass
        else:
            raise ValueError('Improperly Formatted Equation')
    except ValueError:
        sys.stdout.write('The equation was improperly formatted, please put in a correctly formatted equation')
        return
        
    log.debug('         Perform operations')
    calculation = process_equation(equation_parsed)
    log.debug('         Operations done')
    log.debug('         Calculation: ' + str(calculation))
    num, denom = process_fraction(calculation)
    calculation = convert_fraction_to_mixed(int(num),int(denom))
    log.debug('         Reduce: ' + str(calculation))
    log.debug('      Calculation: ' + str(calculation))
    sys.stdout.write(calculation)
import re

# Regular expressions
re_op = re.compile(r' \+|\- ')
re_digits = re.compile(r'^[0-9]{1,4}$')

def arithmetic_arranger(problems, display=False):

    # result line strings
    first = ''
    second = ''
    third = ''
    results = ''

    # Check for too many problems
    if len(problems) >= 5:
        return 'Error: Too many problems.'

    for p in problems:
        # Check for addition or subtraction operator
        if bool(re.findall(re_op, p)) is False:
            return "Error: Operator must be '+' or '-'."

        (upper, symbol, lower) = p.split(' ')

        # Check for letters in operands
        if not bool(re.findall(re_digits, upper)) or not bool(re.findall(re_digits, lower)):
            return "Error: Numbers must only contain digits." 

        # Check for too many digits
        if len(upper) > 4 or len(lower) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if symbol == '+':
            result = int(upper) + int(lower)
        elif symbol == '-':
            result = int(upper) - int(lower)

        op_length = len(f'{symbol} ') + \
            ( len(upper) if len(upper)> len(lower) else len(lower) )

        first += f'{upper.rjust(op_length)}'
        second += f"{symbol}{lower.rjust(op_length - 1)}"
        third += '-' * op_length
        results += f'{str(result).rjust(op_length)}'

        if p is not problems[-1]:
            first += ' ' * 4
            second += ' ' * 4
            third += ' ' * 4
            results += ' ' * 4


    arranged_problems = f'{first}\n{second}\n{third}'
    if display:
        arranged_problems += f"\n{results}"


    return arranged_problems
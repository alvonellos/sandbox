# P48 from
# https://prof.ti.bfh.ch/hew1/informatik3/prolog/p-99/

from pprint import pprint
And=lambda x,y:x and y
Or=lambda x,y:x or y
Not=lambda x:not x
Impl=lambda x,y:Or(Not(x), y)

def fixed_table(numvars):
    """
    Generate true/false permutations for the given number of variables.
    So if numvars=2
    Returns (not necessarily in this order):
        True, True
        True, False
        False, False
        False, True
    """
    if numvars is 1:
        yield [True]
        yield [False]
    else:
        for i in fixed_table(numvars-1):
            yield i + [True]
            yield i + [False]

def truth_table(vars, expr):
    """
    Takes an array of variables, vars, and displays a truth table
    for each possible value combination of vars.
    """
    for cond in fixed_table(len(vars)):
        values=dict(zip(vars,cond))
        yield cond + [eval_expr(values, expr)]

def eval_expr(values, expr):
    """
    Takes a dictionary values {var1 : val1, var2 : val2} and a tuple
    expr (lambda, var1, var2) returns evaluated value.
    expr needs to be in a LISP like format (operator, arg1, arg2).

    Returns the value of expr when variables are set according to
    values.
    """
    argarr=[]
    for arg in expr[1:]:
        if (type(arg) in [tuple, list]):
            argarr.append(eval_expr(values, arg))
        elif (arg in values):
            argarr.append(values[arg])
        else:
            raise ValueError('Invalid expr')

    return expr[0](*argarr)

if __name__ == '__main__':
    # Print truth table for the Impl operator.
    pprint([i for i in truth_table(['x','y'], (Impl, 'x', 'y'))])


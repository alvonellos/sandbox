from sympy import *
from sympy.abc import p, q, r
from sympy.utilities.iterables import cartes

def get_vars():
	vars = []
        print "Please enter the number of variables to use in the equation"
        numVars = int(raw_input())
	print "please enter each of the variables on a newline"
        for i in xrange(numVars):
		vars.append(raw_input())
	return vars

def get_expr():
	print "Please enter the expression to use"
	return str(raw_input())
	
def convert_to_expr(inputStr):
	return eval(inputStr)

def main():
	vars = get_vars()
	expr = get_expr()
			
	print("recieved input: " + str(vars) + " expr " + str(expr))

	print "Truth table for " + str(len(vars)) + "variable(s)"
	for i in enumerate(truth_table(vars, expr)):
		print i

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
        yield cond + [eval(expr)]	

def explore():
    expr_string = raw_input("Enter an expression: ")
    expr = sympify(expr_string)
    variables = sorted(expr.free_symbols)
    print variables
    for truth_values in list(variations([True, False], len(variables), True)):
        values = dict(zip(variables, truth_values))
        print sorted(values.items()), expr.subs(values)

if __name__ == "__main__":
#	main()
	explore()

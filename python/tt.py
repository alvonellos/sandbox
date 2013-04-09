from sympy import *
from sympy.abc import p, q, r, s
from sympy.utilities.iterables import cartes

def explore():
    expr_string = raw_input("Enter an expression: ")
    expr = sympify(expr_string)
    variables = sorted(expr.free_symbols)
    print variables
    for truth_values in list(variations([True, False], len(variables), True)):
        values = dict(zip(variables, truth_values))
        print sorted(values.items()), expr.subs(values)

if __name__ == "__main__":
	explore()

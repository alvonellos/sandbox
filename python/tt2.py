from sympy import *
import sqlite3 as lite
import sys
from sympy.utilities.iterables import cartes


def explore(expr_string):
    """
    Get an expression string (as provided by the user)
    and return a truth table for it.
    """
    expr = sympify(expr_string)
    variables = sorted(expr.free_symbols)
    for truth_values in list(variations([True, False], len(variables), True)):
        values = dict(zip(variables, truth_values))
        print sorted(values.items()), expr.subs(values)

if __name__ == "__main__":
	input = raw_input("Please enter an expression string: ")
	while input != '':
		explore(input)
		input = raw_input("Please enter an expression string: ")


		

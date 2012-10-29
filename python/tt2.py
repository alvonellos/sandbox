from sympy import *
from sympy.abc import p, q, r, s
from sympy.utilities.iterables import cartes
import sqlite3 as lite

def explore():
    expr_string = raw_input("Enter an expression: ")
    expr = sympify(expr_string)
    variables = sorted(expr.free_symbols)
    print variables
    for truth_values in list(variations([True, False], len(variables), True)):
        values = dict(zip(variables, truth_values))
        print sorted(values.items()), expr.subs(values)
    print table(expr_string)

def table(expr_string, variables):
    expr = sympify(expr_string)
    variables = sorted(variables)
    table = []
    for truth_values in list(variations([True, False], len(variables), True)):
        values = dict(zip(variables, truth_values))
        table.append([sorted(values.items()), expr.subs(values)])
    return table

def get_expr_list():
    expr_string = " "
    expr_list = []
    while expr_string != '':
	expr_string = raw_input("Enter a premise: ")
	expr_list.append(expr_string)
    expr_list = expr_list[:len(expr_list)-1]

    conclusion = raw_input("Enter a conclusion: ")
    expr_list.append(conclusion)
    return expr_list

def get_free_vars(expr_list):
    vars = []
    for expr in expr_list:
        sym = sympify(expr)
        myvars = sym.free_symbols
        for var in myvars:
            vars.append(var)
    return sorted(list(set(vars)))

def get_row_defs(expr_list):
    free_vars = get_free_vars(expr_list)
    rows = [str(x) for x in free_vars]
    rows += ['['+str(y)+']' for y in expr_list]
    return rows

def truth_table(expr_list):
	table = []
	variables = get_free_vars(expr_list)
#	for truth_values in list(variations([True, False], len(variables), True)):
	return

if __name__ == "__main__":
	expr_list = get_expr_list()
	print expr_list
	free_vars = get_free_vars(expr_list)
	print "free vars: " + str(free_vars)
	print "row defs: " + str(get_row_defs(expr_list))
	for expr in expr_list:
		print expr
		print table(expr, sympify(expr).free_symbols)	
	

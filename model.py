import sympy
def eval_exp(exp):# функция решения уравнения
    x = sympy.Symbol('x')
    return sympy.solve(exp,x)
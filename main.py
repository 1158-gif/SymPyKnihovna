import sympy as sp

print("Uloha 1")
m, v = sp.symbols('m v')
E = sp.Rational(1, 2) * m * v**2
print(E)

print("\nUloha 2")
E_value = E.subs({m: 1200, v: 25})
print(E_value.evalf())

print("\nUloha 3")
A, B = sp.symbols('A B')
expr = (A + B)**2 - (A**2 + 2*A*B)
expanded = sp.expand(expr)
simplified = sp.simplify(expr)
print("Expand:", expanded)
print("Simplify:", simplified)

print("\nUloha 4")
x = sp.symbols('x')
expr2 = x**2 - 25
factored = sp.factor(expr2)
print(factored)

print("\nUloha 5")
s, v, t = sp.symbols('s v t')
eq = sp.Eq(s, v*t)
solution_t = sp.solve(eq, t)
time_value = solution_t[0].subs({s: 150, v: 75})
print(time_value)

print("\nUloha 6")
t = sp.symbols('t')
h = -5*t**2 + 20*t
times = sp.solve(h, t)
print(times)

print("\nUloha 7")
s, t = sp.symbols('s t')
eq1 = sp.Eq(3*s + 2*t, 44)
eq2 = sp.Eq(2*s + 5*t, 46)
prices = sp.solve((eq1, eq2), (s, t))
print(prices)

print("\nUloha 8")
U, R, I = sp.symbols('U R I')
ohm = sp.Eq(U, R*I)
R_expr = sp.solve(ohm, R)
I_expr = sp.solve(ohm, I)
print("R =", R_expr)
print("I =", I_expr)

print("\nUloha 9")
rho, m, V = sp.symbols('rho m V')
density_eq = sp.Eq(rho, m/V)
m_expr = sp.solve(density_eq, m)[0]
mass = m_expr.subs({rho: 7800, V: 0.002})
print(mass.evalf())

print("\nUloha 10")
p, q = sp.symbols('p q')
expr3 = (p + q)**3
expanded_expr3 = sp.expand(expr3)
print(expanded_expr3)

print("\nUloha 11")
a, b = sp.symbols('a b')
expr_a = (a + b)**2
expr_b = a**2 + 2*a*b + b**2
check = sp.simplify(expr_a - expr_b)
print(check)

print("\nUloha 12")
v, s, t = sp.symbols('v s t')
speed_eq = sp.Eq(v, s/t)
s_expr = sp.solve(speed_eq, s)
t_expr = sp.solve(speed_eq, t)
print("s =", s_expr)
print("t =", t_expr)

print("\nUloha 13")
x = sp.symbols('x')
eq_check = sp.Eq(3*x + 7, 25)
solution = sp.solve(eq_check, x)[0]
verification = eq_check.subs(x, solution)
print("x =", solution)
print("Kontrola:", verification)

print("\nUloha 14")
p, q, d, C = sp.symbols('p q d C')
price_eq = sp.Eq(C, p*q + d)
q_expr = sp.solve(price_eq, q)[0]
result_q = q_expr.subs({C: 550, p: 45, d: 100})
print(result_q)

print("\nUloha 15")
r, pi = sp.symbols('r pi')
area = pi*r**2
area_value = area.subs({pi: sp.pi, r: 5})
print(area_value.evalf())

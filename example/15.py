from sympy import symbols, Eq, solve, limit, diff, integrate, tan, cos, pi, sqrt, oo

# Định nghĩa biến
x, y, z = symbols('x y z')

# a) Giải hệ phương trình
def solve_system():
    eq1 = Eq(2*x - 5*y + z, -5)
    eq2 = Eq(4*x + 2*y - 2*z, 2)
    eq3 = Eq(x + y - z, 0)
    solution = solve((eq1, eq2, eq3), (x, y, z))
    return solution

# b) Tính giới hạn của hàm
def calculate_limit():
    f = (x**3 - 3*x**2)**(1/3) + (x**2 - 2*x)**(1/2)
    lim = limit(f, x, 5)
    return lim

# c) Tính đạo hàm
def calculate_derivative():
    f = (4*x - 1)/(3*x + 5)
    derivative = diff(f, x)
    return derivative

# d) Tính nguyên hàm
def calculate_integral():
    f = 5*x/(x**2 + 2)
    integral = integrate(f, x)
    return integral

# e) Tính tích phân
def calculate_definite_integral():
    f = (1 - x*tan(x))/(x**2*cos(x) + x)
    definite_integral = integrate(f, (x, pi, 3*pi/2))
    return definite_integral

# Chương trình chính
solution_system = solve_system()
limit_f = calculate_limit()
derivative_f = calculate_derivative()
integral_f = calculate_integral()
definite_integral_f = calculate_definite_integral()


print(solution_system, limit_f, derivative_f, integral_f, definite_integral_f
)
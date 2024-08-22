from aprox_derivadas import AproxDerivadas as D

# Função
def f(x):
    return x**2 - 6*x + 5

# Derivada primeira
def df1(x):
    return 2*x - 6

# Derivada segunda
def df2(x):
    return 2

# Método de Newton com derivadas exatas
def met_newton(f, df1, df2, x_inicial, tol, max_iter):
    i = 0
    x0 = x_inicial
    x1 = x0 - df1(x0) / df2(x0)
    
    while(abs(x1 - x0) > tol and i < max_iter):
        x0 = x1
        x1 = x0 - df1(x0) / df2(x0)
        
        print("Iteração: ", i, "x0: ", x0, "x1: ", x1, "f(x1): ", f(x1))
        i+=1
    
    print("Solução: ", x1)
    return x1

# Método de Newton com derivadas aproximadas
def met_newton_derivadas_aprox(f, x_inicial, tol, max_iter):
    i = 0
    x0 = x_inicial
    x1 = x0 - D(f).df1(x0) / D(f).df2(x0)
    
    while(abs(x1 - x0) > tol and i < max_iter):
        x0 = x1
        x1 = x0 - D(f).df1(x0) / D(f).df2(x0)
        
        print("Iteração: ", i, "x0: ", x0, "x1: ", x1, "f(x1): ", f(x1))
        i+=1
    
    print("Solução: ", x1)
    return x1
    
#
# Implementação do método de Newton
#
a = 1
tol = 0.0001
max_iter = 100

# met_newton(f, df1, df2, a, tol, max_iter)

met_newton_derivadas_aprox(f, a, tol, max_iter)



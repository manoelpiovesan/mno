fi = 0.618

# Método da seção áurea
def secao_aurea(f, a, b, tol, max_iter):
    xl = a
    xh = b
    i = 0
    
    while (abs(xh - xl) > tol and i < max_iter):
        x1 = xh - fi * (xh - xl)
        x2 = xl + fi * (xh - xl)
        
        if(f(x1) < f(x2)):
            xh = x2
        else:
            xl = x1
        
        print("Iteração: ", i, "xl: ", xl, "xh: ", xh, "f(x1): ", f(xl), "f(x2): ", f(xh))
        i+=1
        
    print("Solução: ", (xl + xh) / 2)
    return (xl + xh) / 2

# Função
def f(x):
    return x**2 - 6*x + 5

# 
# Implementação do método da seção áurea
#
a = 0
b = 4
tol = 0.0001
max_iter = 100

secao_aurea(f, a, b, tol, max_iter)
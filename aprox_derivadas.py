class AproxDerivadas:
    
    def __init__(self, f, h=1e-5):
        self.f = f
        self.h = h
        
    def df1(self, x):
        return (self.f(x + self.h) - self.f(x)) / self.h
    
    def df2(self, x):
        return (self.f(x + self.h) - self.f(x - self.h)) / (2 * self.h)
    
    def df3(self, x):
        return (self.f(x - 2*self.h) - 8*self.f(x - self.h) + 8*self.f(x + self.h) - self.f(x + 2*self.h)) / (12 * self.h)

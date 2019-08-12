class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __mul__(self, other):
        return (self.real * other.real, self.img * other.img)

    def __truediv__(self, other):
        return (self.real / other.real, self.img / other.img)

x, y = 4, 5
a = Complex(x, y)
p, q = 7, 10
b = Complex(p, q)
mul = a * b
div = a / b
print("Multiplication : ",mul)
print("Division : ",div) 

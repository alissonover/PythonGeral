b = float(input('Digite a base: '))
a = float(input('Digite a altura: '))

class Forma:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def CalcPeriRet(self):
        calc = (a*2) + (b*2)
        print(f'O perimetro é {calc}')
    def CalcAreaRet(self):
        calc1 = a*b
        print(f'A área é {calc1}')

class Triangulo(Forma):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def CalcAreaTri(self):
        calc2 = (a*b)/2
        print(f'A área do triângulo é {calc2}')
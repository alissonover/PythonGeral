class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print(f'O valor do ingresso normal é R${self.valor}')

class Vip(Ingresso):
    def imprimeValorVip(self, vl2):
        self.adicional = vl2
        return print(f'O valor do ingresso vip é R${self.valor+self.adicional}'
                     f' e o valor adicinel é R${self.adicional}')
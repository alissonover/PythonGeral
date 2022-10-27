class Atleta:
    def __init__(self, peso, aposentado =False):
        self.aposentado = aposentado
        self.peso = peso
    def aquecer(self):
        print('aquecer')
    def aposentar(self):
        print('aposentado com sucesso!')
class Corredor(Atleta):
    def __init__(self, correndo = False):
       self.correndo = correndo
    def correr(self):
        print('correndo')
class Ciclista(Atleta):
    def __init__(self, pedalando = False):
        self.pedalando = pedalando
    def pedalar(self):
        print('pedalando')
class Nadador(Atleta):
    def __init__(self, nadando = False):
        self.nadando = nadando
    def nadar(self):
        print('nadando')
class Triatleta(Nadador, Corredor, Ciclista):
    def __init__(self, maratonando = False):
        self.maratonando = maratonando
    def maratonar(self):
        print('maratonando')








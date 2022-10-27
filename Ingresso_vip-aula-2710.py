from Biblioteca import *

vl1 = float(input('Digite o valor do ingresso normal: '))
vl2 = float(input('Digite o valor adicional do ingresso vip: '))

ing1 = Vip(vl1)
ing1.imprimeValor()
ing1.imprimeValorVip(vl2)
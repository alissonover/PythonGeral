from Biblioteca import Conta_bancaria

p1 = Conta_bancaria('Alisson Felipe', 12344, 'Corrente', 0)

p1.ativar_ct()
p1.check_saldo()
p1.depositar(float(input('Digite o valor a ser depositado: ')))
p1.check_saldo()
p1.ativar_limite(500)
p1.check_limite()
p1.sacar(float(input('Digite o valor do saque: ')))
p1.check_saldo()
p1.depositar(float(input('Digite um valor para depositar: ')))
p1.check_saldo()
p1.check_limite()
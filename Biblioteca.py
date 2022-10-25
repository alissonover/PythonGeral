class Conta_bancaria:
    def __init__(self, nome, numero, tipo, limite=0, saldo=0, status=False):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo
        self.status = status
        self.limite = limite
        self.limite_atual = limite

    def ativar_ct(self):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta foi ativada com sucesso!')
            self.status = True
        else:
            print(f'Você não pode ativar sua conta, pois sua conta já está ativada!')

    def desativar_ct(self):
        if self.status == True:
            print(f'Olá {self.nome}, sua conta foi desativada! Caso queira reativar a sua conta fique a vontade!')
            self.status = False
        else:
            print(f'Sua conta não pode ser desativada, pois já está desativada!')

    def check_saldo(self):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta está desativada, por favor ativar antes de fazer qualquer outra ação! ')
        else:
            print(f'O saldo da sua conta é R${self.saldo}.')

    def depositar(self, valor):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta está desativada, por favor ativar antes de fazer qualquer outra ação! ')
        elif self.limite_atual < self.limite:
            self.limite_atual = self.limite_atual + valor
            sobra = self.limite_atual - self.limite
            self.saldo = self.saldo + sobra
            print(f'Olá {self.nome}, seu depósito foi realizado com sucesso e foi ressarcido {sobra} no seu limite especial.')
        else:
            self.saldo = self.saldo + valor

    def ativar_limite(self, aumentar):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta está desativada, por favor ativar antes de fazer qualquer outra ação! ')
        else:
            self.limite = self.limite + aumentar


    def check_limite(self):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta está desativada, por favor ativar antes de fazer qualquer outra ação! ')
        else:
            print(f'O seu limite no cheque especial é R${self.limite} e pode ser usado a qualquer momento.')

    def sacar(self, valor_saque):
        if self.status == False:
            print(f'Olá {self.nome}, sua conta está desativada, por favor ativar antes de fazer qualquer outra ação! ')
        elif valor_saque > self.saldo:
            especial1 = valor_saque - self.saldo
            self.limite_atual = self.limite - especial1
            self.saldo = self.saldo - self.saldo
            print(f'Atenção {self.nome}, você utilizou {especial1} do limite especial. Seu saldo é {self.saldo} e seu limite especial é {self.limite_atual}.')
        else:
            self.saldo = self.saldo - valor_saque







class Conta:
    def __init__(self, name, CPF, END):
        self.cliente = name
        self.CPF = CPF
        self.END = END
        self.saldo = 0.0

    def Cliente(self):
        return self.cliente

    def Saldo(self):
        return self.saldo

    def Depositar(self, valor):
        self.saldo += valor

    def Transferir(self, conta, valor):
        self.saldo = self.saldo - valor
        conta.saldo = conta.saldo + valor


from datetime import datetime
import pytz
from random import randint

class ContaCorrent:
     
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []
        
    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, f"Saldo: {self.saldo}", self._data_hora()))

    def sacar(self, valor):
        if self.saldo <= 0:
            print(f"Você não pode sacar, saldo insuficiente..")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, f"Saldo: {self.saldo}", ContaCorrent._data_hora()))
  
    def consultar_saldo(self):
        print(f"Seu saldo atual é: R${self.saldo:,.2f}")

    def consultar_historico(self):
        print(f"Histórico de transação:")
        for transacao in self.transacoes:
            valor, saldo, horario = transacao
            print(f"Valor: {valor}")
            print(saldo)
            print(f"Horario: {horario}")
            print("------------------------------------")

    def transferir(self, valor, conta_destino):
        if self.saldo <= 0:
            print(f"Você não possui saldo suficiente pra fazer a transferencia..")
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, f"Saldo: {self.saldo}", ContaCorrent._data_hora()))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, f"Saldo:{conta_destino.saldo}", ContaCorrent._data_hora()))
        
class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
        

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self.cod_seg = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.limite = 1000
        self.senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


if __name__ == '__main__':
    ## Testes de conta ##
    conta_vini = ContaCorrent('Vinicius', 302321031, 20320, 200)
    conta_jusefino = ContaCorrent('Jusefino', 2313222, 23234, 2211)
    conta_vini.consultar_saldo()

    # vini_cartao = CartaoCredito('Robervaldo', conta_vini)
    # print(conta_vini.cartoes[0].numero)


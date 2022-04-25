from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 100000000
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"O caixa está abaixo do nivel recomendado. Caixa atual: {self.caixa}")
        else:
            print(f"Valor do caixa atual:{self.caixa}")
    
    def emprestar_dinheiro(self, valor, cpf):
        if self.caixa > valor:
            self.caixa -= valor
            self.emprestimos.append((valor, cpf))
        else:
            print("Emprestimo não disponivel")

    def add_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000000



# class AgenciaVirtual(Agencia):  # FILHA

#     def __init__(self, site, telefone, cnpj):
#         self.site = site
#         # tem todas a caracteristicas da agencia e também tem as outras.
#         super().__init__(telefone, cnpj, 1000)
#         self.caixa = 1000000
#         self.caixa_paypal = 0

#     def depositar_paypal(self, valor):
#         self.caixa -= valor
#         self.caixa_paypal += valor

#     def sacar_paypal(self, valor):
#         self.caixa_paypal -= valor
#         self.caixa += valor


## TESTES ##
if __name__ == '__main__':
    
    ## Agencia comum ##
    primeira_comum = AgenciaComum(35211111, 70798540000148)
    premium = AgenciaPremium(231231, 23131231, 222)
    print(primeira_comum.numero)
    print(primeira_comum.cnpj)
    
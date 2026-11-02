"""
Code smell(s) identificado(s):
Lista longa de parâmetros
Feature envy (parâmetros que fazem sentido em outras classes)
Obsessão por tipos primitivos
"""

class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"({self.ddd}) {self.numero}"


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: {self.telefone}")
        print(f"Endereço: {self.endereco}")

'''
class Funcionario:
    def __init__(self, nome, cargo, salario, rua, numero, bairro, cidade, estado, cep, ddd, telefone_numero):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.ddd = ddd
        self.telefone_numero = telefone_numero

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: ({self.ddd}) {self.telefone_numero}")
        print(f"Endereço: {self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}")
'''
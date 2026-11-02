"""
Code smell(s) identificado(s):
Lista longa de parâmetros
Obsessão por tipos primitivos
Viola SRP
"""

class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


class Reserva:
    VALOR_CAFE_DA_MANHA_DIARIO = 50

    def __init__(self, hospede, quarto, data_checkin, data_checkout, possui_cafe_da_manha):
        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def calcular_total_dias(self):
        return (self.data_checkout - self.data_checkin).days

    def calcular_total(self):
        total_dias = self.calcular_total_dias()
        total = total_dias * self.quarto.valor_diaria
        if self.possui_cafe_da_manha:
            total += self.VALOR_CAFE_DA_MANHA_DIARIO * total_dias
        return total

    def exibir_resumo(self):
        print(f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})")
        print(f"Quarto {self.quarto.numero} ({self.quarto.tipo})")
        print(f"De {self.data_checkin} até {self.data_checkout}")
        print(f"Total a pagar: R$ {self.calcular_total()}")

'''
def criar_reserva(nome_hospede, cpf_hospede, email_hospede, numero_quarto, tipo_quarto, data_checkin, data_checkout, valor_diaria, possui_cafe_da_manha):
    print(f"Reserva criada para {nome_hospede} (CPF: {cpf_hospede})")
    print(f"Quarto {numero_quarto} ({tipo_quarto})")
    print(f"De {data_checkin} até {data_checkout}")
    total_dias = (data_checkout - data_checkin).days
    total = total_dias * valor_diaria
    if possui_cafe_da_manha:
        total += 50 * total_dias
    print(f"Total a pagar: R$ {total}")
'''
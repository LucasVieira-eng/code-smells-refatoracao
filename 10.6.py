"""
Code smell(s) identificado(s):
Comentários excessivos
Código duplicado
"""

class ProcessadorFinanceiro:
    TAXA_CREDITO = 0.05
    TAXA_DEBITO = 0.02

    def processar_pagamento_credito(self, valor):
        self._processar_pagamento("crédito", valor, self.TAXA_CREDITO)

    def processar_pagamento_debito(self, valor):
        self._processar_pagamento("débito", valor, self.TAXA_DEBITO)

    def _processar_pagamento(self, tipo, valor, taxa):
        if valor <= 0:
            print("Valor inválido")
            return

        valor_com_taxa = valor + (valor * taxa)
        print(f"Processando {tipo}: R$ {valor_com_taxa}")


'''
class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        # Verifica se o valor é maior que zero
        if valor > 0:
            # Adiciona a taxa do cartão de crédito (5%)
            valor_com_taxa = valor + (valor * 0.05)
            # Imprime o valor na tela
            print(f"Processando crédito: R$ {valor_com_taxa}")
        else:
            # Retorna erro se for menor que zero
            print("Valor inválido")

    def processar_pagamento_debito(self, valor):
        # Verifica se o valor é maior que zero
        if valor > 0:
            # Adiciona a taxa do cartão de débito (2%)
            valor_com_taxa = valor + (valor * 0.02)
            # Imprime o valor na tela
            print(f"Processando débito: R$ {valor_com_taxa}")
        else:
            # Retorna erro se for menor que zero
            print("Valor inválido")
'''
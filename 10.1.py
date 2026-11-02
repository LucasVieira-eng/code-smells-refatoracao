"""
Code smell(s) identificado(s):
Método viola SRP
Método longo
"""


# noinspection method-may-be-static
class GerenciadorDeVendas:
    TIPO_CLIENTE_VIP = 'VIP'
    FATOR_DESCONTO_VIP = 0.90

    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self._calcular_total(itens)
        total = self._aplicar_desconto(total, cliente)
        self._processar_pagamento(total, metodo_pagamento)
        self._gerar_relatorio(total, cliente)
        print("Venda processada com sucesso.")

    def _calcular_total(self, itens):
        total = 0
        for item in itens:
            total += item['preco'] * item['quantidade']
        return total

    def _aplicar_desconto(self, total, cliente):
        if cliente['tipo'] == self.TIPO_CLIENTE_VIP:
            return total * self.FATOR_DESCONTO_VIP
        return total

    def _processar_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

    def _gerar_relatorio(self, total, cliente):
        relatorio = f"--- Relatório de Venda ---\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)

'''
class GerenciadorDeVendas:
    def processar_venda_e_gerar_relatorio(self, itens, cliente, metodo_pagamento):
        # Lógica de cálculo
        total = 0
        for item in itens:
            total += item['preco'] * item['quantidade']

        # Lógica de desconto
        if cliente['tipo'] == 'VIP':
            total = total * 0.90

        # Lógica de pagamento
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

        # Lógica de relatório
        relatorio = f"--- Relatório de Venda ---\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)
        print("Venda processada com sucesso.")
'''
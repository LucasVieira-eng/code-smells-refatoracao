"""
Code Smell(s) identificado(s):
Divergent Change
Violação do SRP
"""

class Produto:
    ALIQUOTA_IMPOSTO = 0.15

    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * (1 + self.ALIQUOTA_IMPOSTO)


# noinspection method-may-be-static
class ProdutoRepository:
    def salvar(self, produto):
        print(f"INSERT INTO produtos (id, nome, preco) VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});")


class ProdutoXmlExporter:
    def exportar(self, produto):
        return f"<produto><id>{produto.id_produto}</id><nome>{produto.nome}</nome><preco>{produto.preco}</preco></produto>"

'''
class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * 1.15

    def salvar_no_banco_de_dados(self):
        print(f"INSERT INTO produtos (id, nome, preco) VALUES ({self.id_produto}, '{self.nome}', {self.preco});")

    def exportar_para_xml(self):
        return f"<produto><id>{self.id_produto}</id><nome>{self.nome}</nome><preco>{self.preco}</preco></produto>"
'''
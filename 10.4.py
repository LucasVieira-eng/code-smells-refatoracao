"""
Code Smell(s) identificado(s):
Switch statements / Conditional complexity
"""

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def calcular_frete(self, distancia):
        pass


class Moto(Transporte):
    VALOR_POR_KM = 2.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM


class Carro(Transporte):
    VALOR_POR_KM = 3.5
    TAXA_BASE = 10.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM + self.TAXA_BASE


class Caminhao(Transporte):
    VALOR_POR_KM = 8.0
    TAXA_BASE = 50.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM + self.TAXA_BASE


class Bicicleta(Transporte):
    VALOR_POR_KM = 1.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM


class CalculadoraDeFrete:
    TRANSPORTES = {
        "MOTO": Moto(),
        "CARRO": Carro(),
        "CAMINHAO": Caminhao(),
        "BICICLETA": Bicicleta(),
    }

    def calcular_frete(self, tipo_transporte, distancia):
        transporte = self.TRANSPORTES.get(tipo_transporte)
        if transporte is None:
            raise ValueError("Tipo de transporte desconhecido")
        return transporte.calcular_frete(distancia)

'''
class CalculadoraDeFrete:
    def calcular_frete(self, tipo_transporte, distancia):
        if tipo_transporte == "MOTO":
            return distancia * 2.0
        elif tipo_transporte == "CARRO":
            return distancia * 3.5 + 10.0  # taxa base do carro
        elif tipo_transporte == "CAMINHAO":
            return distancia * 8.0 + 50.0  # taxa base do caminhão
        elif tipo_transporte == "BICICLETA":
            return distancia * 1.0
        else:
            raise ValueError("Tipo de transporte desconhecido")
'''
class Apartamento(object):

    def __init__(self, numero, qtdQuartos, ocupacao):
        self.numero = numero
        self.qtdQuartos = qtdQuartos
        self.ocupation = ocupacao

    def getNumero(self):
        return self.numero

    def getQuartos(self):
        return self.qtdQuartos

    def getOcupation(self):
        return self.ocupation

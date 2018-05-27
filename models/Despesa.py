class Despesa(object):

    def __init__(self, mes_ano, valor):
        self.mes_ano = mes_ano
        self.valor = valor

    def get_mes_ano(self):
        return self.mes_ano

    def get_valor(self):
        return self.valor

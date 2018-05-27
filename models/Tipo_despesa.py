class Tipo_despesa(object):

    def __init__(self, nome, valor_rateado):
        self.nome = nome
        self.valor_rateado = valor_rateado

    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.valor_rateado

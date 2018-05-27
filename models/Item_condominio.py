class Item_condominio(object):

    def __init__(self, referencia, valor):
        self.referencia = referencia
        self.valor = valor

    def get_referencia(self):
        return self.referencia

    def get_valor(self):
        return self.valor

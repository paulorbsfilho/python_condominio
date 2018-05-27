class Condominio(object):

    def __init__(self, mes_ano, data_pagamento, valor_pago, valor_a_pagar):
        self.mesAno = mes_ano
        self.data_pagamento = data_pagamento
        self.valor_pago = valor_pago
        self.valor_a_pagar = valor_a_pagar

    def get_MesAno(self):
        return self.mesAno

    def get_dataPagamento(self):
        return self.dataPagamento

    def get_valor_pago(self):
        return self.valor_pago

    def get_valor_a_pagar(self):
        return self.valor_a_pagar
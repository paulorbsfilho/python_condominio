from enum import Enum

from django.db import models


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class TipoOcupacao(ChoiceEnum):
    PROPRIETARIO = 'P'
    INQUILINO = 'I'
    VAZIO = 'V'


class Apartamento(models.Model):
    numero = models.IntegerField('Numero ap')
    qtdQuartos = models.IntegerField('Q. de quartos', default=0)
    ocupacao = models.CharField('Ocupacao', max_length=12, choices=TipoOcupacao.choices())



class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone',max_length=20)


class Fatura(models.Model):
    mes_ano = models.CharField('Mes/Ano', max_length=20)
    data_pagamento = models.DateField('Data de pagamento')
    valor_pago = models.FloatField('Valor pago')
    valor_a_pagar = models.FloatField('Valor a pagar')


class ItemFatura(models.Model):
    referencia = models.CharField('Ref', max_length=50)
    valor = models.FloatField()


class Despesa(models.Model):
    mes_ano = models.CharField('Mes/Ano',max_length=50)
    valor = models.FloatField('Valor')


class TipoDespesa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    valor_rateado = models.BooleanField('Rateado?')


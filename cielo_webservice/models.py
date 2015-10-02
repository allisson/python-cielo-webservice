# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six


class Comercial(object):

    def __init__(self, numero=None, chave=None):
        self.numero = numero
        self.chave = chave
        self.validate()

    def validate(self):
        if not isinstance(self.numero, six.integer_types):
            raise TypeError('numero precisa ser do tipo inteiro.')

        if not isinstance(self.chave, six.string_types):
            raise TypeError('chave precisa ser do tipo string.')


class Cartao(object):

    def __init__(self, numero=None, validade=None, indicador=None,
                 codigo_seguranca=None, nome_portador=None, token=None):
        self.numero = numero
        self.validade = validade
        self.indicador = indicador
        self.codigo_seguranca = codigo_seguranca
        self.nome_portador = nome_portador
        self.token = token
        self.validate()

    def validate(self):
        if self.numero and not isinstance(self.numero, six.integer_types):
            raise TypeError('numero precisa ser do tipo inteiro.')

        if self.validade and not isinstance(self.validade, six.integer_types):
            raise TypeError('validade precisa ser do tipo inteiro.')

        if self.indicador and not isinstance(self.indicador, six.integer_types):
            raise TypeError('indicador precisa ser do tipo inteiro.')

        if self.indicador == 1 and not isinstance(self.codigo_seguranca, six.integer_types):
            raise TypeError('codigo_seguranca precisa ser do tipo inteiro.')

        if self.nome_portador and not isinstance(self.nome_portador, six.string_types):
            raise TypeError('nome_portador precisa ser do tipo string.')

        if self.numero and self.token:
            raise TypeError(
                'você não pode usar os dados do cartão e token na mesma requisição.'
            )

        if self.token and not isinstance(self.token, six.string_types):
            raise TypeError('token precisa ser do tipo string.')


class Pedido(object):

    def __init__(self, numero=None, valor=None, moeda=986, data_hora=None,
                 descricao=None, idioma='PT', taxa_embarque=None,
                 soft_descriptor=None):
        self.numero = numero
        self.valor = valor
        self.moeda = moeda
        self.data_hora = data_hora
        self.descricao = descricao
        self.idioma = idioma
        self.taxa_embarque = taxa_embarque
        self.soft_descriptor = soft_descriptor
        self.validate()

    def validate(self):
        if not isinstance(self.numero, six.string_types):
            raise TypeError('numero precisa ser do tipo string.')

        if not isinstance(self.valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        if not isinstance(self.moeda, six.integer_types):
            raise TypeError('moeda precisa ser do tipo inteiro.')

        if not isinstance(self.data_hora, six.string_types):
            raise TypeError('data_hora precisa ser do tipo string.')

        if self.descricao and not isinstance(self.descricao, six.string_types):
            raise TypeError('descricao precisa ser do tipo string.')

        if self.idioma and not isinstance(self.idioma, six.string_types):
            raise TypeError('idioma precisa ser do tipo string.')

        if self.taxa_embarque and not isinstance(self.taxa_embarque, six.integer_types):
            raise TypeError('taxa_embarque precisa ser do tipo inteiro.')

        if self.soft_descriptor and not isinstance(self.soft_descriptor, six.string_types):
            raise TypeError('soft_descriptor precisa ser do tipo string.')

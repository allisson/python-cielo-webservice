# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase

from cielo_webservice.models import Comercial, Cartao, Pedido


class TestComercial(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Comercial(numero='1234', chave='1234')

        self.assertIn(
            'numero precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Comercial(numero=1234, chave=1234)

        self.assertIn(
            'chave precisa ser do tipo string.', context.exception
        )


class TestCartao(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Cartao(
                numero='1234', validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )

        self.assertIn(
            'numero precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(
                numero=1234, validade='201805', indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )

        self.assertIn(
            'validade precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(
                numero=1234, validade=201805, indicador='1',
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )

        self.assertIn(
            'indicador precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca='123', nome_portador='Fulano Silva'
            )

        self.assertIn(
            'codigo_seguranca precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador=123
            )

        self.assertIn(
            'nome_portador precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva', token='123'
            )

        self.assertIn(
            'você não pode usar os dados do cartão e token na mesma requisição.',
            context.exception
        )

        with self.assertRaises(TypeError) as context:
            Cartao(token=123)

        self.assertIn(
            'token precisa ser do tipo string.', context.exception
        )


class TestPedido(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Pedido(
                numero=1234, valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37',
            )

        self.assertIn(
            'numero precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor='10000', moeda=986,
                data_hora='2011-12-07T11:43:37',
            )

        self.assertIn(
            'valor precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda='986',
                data_hora='2011-12-07T11:43:37',
            )

        self.assertIn(
            'moeda precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora=20111207,
            )

        self.assertIn(
            'data_hora precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', descricao=123
            )

        self.assertIn(
            'descricao precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', idioma=123
            )

        self.assertIn(
            'idioma precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', taxa_embarque='123'
            )

        self.assertIn(
            'taxa_embarque precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', soft_descriptor=123
            )

        self.assertIn(
            'soft_descriptor precisa ser do tipo string.', context.exception
        )

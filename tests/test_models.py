# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase

from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Autenticacao, Autorizacao, Transacao
)


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


class TestPagamento(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Pagamento(bandeira=1, produto=1, parcelas=1)

        self.assertIn(
            'bandeira precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pagamento(bandeira='visa', produto=1, parcelas=1)

        self.assertIn(
            'produto precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Pagamento(bandeira='visa', produto='1', parcelas='1')

        self.assertIn(
            'parcelas precisa ser do tipo inteiro.', context.exception
        )


class TestAutenticacao(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Autenticacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )

        self.assertIn(
            'codigo precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autenticacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )

        self.assertIn(
            'mensagem precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, eci=7
            )

        self.assertIn(
            'data_hora precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', eci=7
            )

        self.assertIn(
            'valor precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci='7'
            )

        self.assertIn(
            'eci precisa ser do tipo inteiro.', context.exception
        )


class TestAutorizacao(TestCase):

    def test_validate(self):
        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )

        self.assertIn(
            'codigo precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )

        self.assertIn(
            'mensagem precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, lr=1, arp=1, nsu=1
            )

        self.assertIn(
            'data_hora precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', lr=1, arp=1, nsu=1
            )

        self.assertIn(
            'valor precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr='1', arp=1, nsu=1
            )

        self.assertIn(
            'lr precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp='1', nsu=1
            )

        self.assertIn(
            'arp precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu='1'
            )

        self.assertIn(
            'nsu precisa ser do tipo inteiro.', context.exception
        )


class TestTransacao(TestCase):

    def test_validate(self):
        comercial = Comercial(numero=1234, chave='1234')
        cartao = Cartao(
            numero=1234, validade=201805, indicador=1,
            codigo_seguranca=123, nome_portador='Fulano Silva'
        )
        pedido = Pedido(
            numero='1234', valor=10000, moeda=986,
            data_hora='2011-12-07T11:43:37',
        )
        pagamento = Pagamento(bandeira='visa', produto='1', parcelas=1)
        autenticacao = Autenticacao(
            codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
            valor=10000, eci=7
        )
        autorizacao = Autorizacao(
            codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
            valor=10000, lr=1, arp=1, nsu=1
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=1, cartao=cartao, pedido=pedido,
                pagamento=pagamento,
            )

        self.assertIn(
            'comercial precisa ser do tipo Comercial.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=1, pedido=pedido,
                pagamento=pagamento,
            )

        self.assertIn(
            'cartao precisa ser do tipo Cartao.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=1,
                pagamento=pagamento,
            )

        self.assertIn(
            'pedido precisa ser do tipo Pedido.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=1,
            )

        self.assertIn(
            'pagamento precisa ser do tipo Pagamento.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar='1'
            )

        self.assertIn(
            'autorizar precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar=1, url_retorno=1
            )

        self.assertIn(
            'url_retorno precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, capturar='false'
            )

        self.assertIn(
            'capturar precisa ser do tipo booleano.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, campo_livre=1
            )

        self.assertIn(
            'campo_livre precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, bin='1234'
            )

        self.assertIn(
            'bin precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, gerar_token='false'
            )

        self.assertIn(
            'gerar_token precisa ser do tipo booleano.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, avs=1
            )

        self.assertIn(
            'avs precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=1, autorizacao=autorizacao
            )

        self.assertIn(
            'autenticacao precisa ser do tipo Autenticacao.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=autenticacao, autorizacao=1
            )

        self.assertIn(
            'autorizacao precisa ser do tipo Autorizacao.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid=1, pan='pan', status=1
            )

        self.assertIn(
            'tid precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan=1, status=1
            )

        self.assertIn(
            'pan precisa ser do tipo string.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status='1',
                url_autenticacao='http://google.com'
            )

        self.assertIn(
            'status precisa ser do tipo inteiro.', context.exception
        )

        with self.assertRaises(TypeError) as context:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1,
                url_autenticacao=1
            )

        self.assertIn(
            'url_autenticacao precisa ser do tipo string.', context.exception
        )

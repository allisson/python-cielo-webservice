# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase
import pytest
import os

from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Autenticacao, Autorizacao, Token,
    Transacao, Avs, Captura, xml_to_object
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestComercial(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Comercial(numero='1234', chave='1234')
        assert excinfo.value.message == 'numero precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Comercial(numero=1234, chave=1234)
        assert excinfo.value.message == 'chave precisa ser do tipo string.'


class TestCartao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero='1234', validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert excinfo.value.message == 'numero precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade='201805', indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert excinfo.value.message == 'validade precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador='1',
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert excinfo.value.message == 'indicador precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca='123', nome_portador='Fulano Silva'
            )
        assert excinfo.value.message == 'codigo_seguranca precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador=123
            )
        assert excinfo.value.message == 'nome_portador precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva', token='123'
            )
        assert excinfo.value.message == 'você não pode usar os dados do cartão e token na mesma requisição.'

        with pytest.raises(TypeError) as excinfo:
            Cartao(token=123)
        assert excinfo.value.message == 'token precisa ser do tipo string.'


class TestPedido(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero=1234, valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37',
            )
        assert excinfo.value.message == 'numero precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor='10000', moeda=986,
                data_hora='2011-12-07T11:43:37',
            )
        assert excinfo.value.message == 'valor precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda='986',
                data_hora='2011-12-07T11:43:37',
            )
        assert excinfo.value.message == 'moeda precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora=20111207,
            )
        assert excinfo.value.message == 'data_hora precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', descricao=123
            )
        assert excinfo.value.message == 'descricao precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', idioma=123
            )
        assert excinfo.value.message == 'idioma precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', taxa_embarque='123'
            )
        assert excinfo.value.message == 'taxa_embarque precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', soft_descriptor=123
            )
        assert excinfo.value.message == 'soft_descriptor precisa ser do tipo string.'


class TestPagamento(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira=1, produto=1, parcelas=1)
        assert excinfo.value.message == 'bandeira precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira='visa', produto=1, parcelas=1)
        assert excinfo.value.message == 'produto precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira='visa', produto='1', parcelas='1')
        assert excinfo.value.message == 'parcelas precisa ser do tipo inteiro.'


class TestAutenticacao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )
        assert excinfo.value.message == 'codigo precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )
        assert excinfo.value.message == 'mensagem precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, eci=7
            )
        assert excinfo.value.message == 'data_hora precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', eci=7
            )
        assert excinfo.value.message == 'valor precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci='7'
            )
        assert excinfo.value.message == 'eci precisa ser do tipo inteiro.'


class TestAutorizacao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert excinfo.value.message == 'codigo precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert excinfo.value.message == 'mensagem precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert excinfo.value.message == 'data_hora precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', lr=1, arp=1, nsu=1
            )
        assert excinfo.value.message == 'valor precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr='1', arp=1, nsu=1
            )
        assert excinfo.value.message == 'lr precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp='1', nsu=1
            )
        assert excinfo.value.message == 'arp precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu='1'
            )
        assert excinfo.value.message == 'nsu precisa ser do tipo inteiro.'


class TestToken(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Token(codigo=1, status=1, numero='1234')
        assert excinfo.value.message == 'codigo precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Token(codigo='code', status='1', numero='1234')
        assert excinfo.value.message == 'status precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Token(codigo='code', status=1, numero=1234)
        assert excinfo.value.message == 'numero precisa ser do tipo string.'


class TestAvs(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco=1, complemento='', numero=1, bairro='Bairro',
                cep='00000-000'
            )
        assert excinfo.value.message == 'endereco precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento=1, numero=1, bairro='Bairro',
                cep='00000-000'
            )
        assert excinfo.value.message == 'complemento precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero='1', bairro='Bairro',
                cep='00000-000'
            )
        assert excinfo.value.message == 'numero precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero=1, bairro=1,
                cep='00000-000'
            )
        assert excinfo.value.message == 'bairro precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero=1, bairro='Bairro',
                cep=00000000
            )
        assert excinfo.value.message == 'cep precisa ser do tipo string.'


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
        token = Token(codigo='codigo', status=1, numero='1234')
        avs = Avs(
            endereco='Rua 1', complemento='', numero=1, bairro='Bairro',
            cep='00000-000'
        )
        captura = Captura(
            codigo=1, mensagem='mensagem',
            data_hora='2011-12-07T11:43:37', valor=10000, taxa_embarque=0
        )

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=1, cartao=cartao, pedido=pedido,
                pagamento=pagamento,
            )
        assert excinfo.value.message == 'comercial precisa ser do tipo Comercial.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=1, pedido=pedido,
                pagamento=pagamento,
            )
        assert excinfo.value.message == 'cartao precisa ser do tipo Cartao.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=1,
                pagamento=pagamento,
            )
        assert excinfo.value.message == 'pedido precisa ser do tipo Pedido.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=1,
            )
        assert excinfo.value.message == 'pagamento precisa ser do tipo Pagamento.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar='1'
            )
        assert excinfo.value.message == 'autorizar precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar=1, url_retorno=1
            )
        assert excinfo.value.message == 'url_retorno precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, capturar='false'
            )
        assert excinfo.value.message == 'capturar precisa ser do tipo booleano.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, campo_livre=1
            )
        assert excinfo.value.message == 'campo_livre precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, bin='1234'
            )
        assert excinfo.value.message == 'bin precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, gerar_token='false', avs=avs
            )
        assert excinfo.value.message == 'gerar_token precisa ser do tipo booleano.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, avs=1
            )
        assert excinfo.value.message == 'avs precisa ser do tipo Avs.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=1, autorizacao=autorizacao
            )
        assert excinfo.value.message == 'autenticacao precisa ser do tipo Autenticacao.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=autenticacao, autorizacao=1,
                captura=captura
            )
        assert excinfo.value.message == 'autorizacao precisa ser do tipo Autorizacao.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=autenticacao,
                autorizacao=autorizacao, captura=1
            )
        assert excinfo.value.message == 'captura precisa ser do tipo Captura.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid=1, pan='pan', status=1
            )
        assert excinfo.value.message == 'tid precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan=1, status=1
            )
        assert excinfo.value.message == 'pan precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status='1',
                url_autenticacao='http://google.com'
            )
        assert excinfo.value.message == 'status precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1,
                url_autenticacao=1, token=token
            )
        assert excinfo.value.message == 'url_autenticacao precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1, token=1
            )
        assert excinfo.value.message == 'token precisa ser do tipo Token.'


class TestCaptura(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo='1', mensagem='mensagem',
                data_hora='2011-12-07T11:43:37', valor=10000, taxa_embarque=0
            )
        assert excinfo.value.message == 'codigo precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, taxa_embarque=0
            )
        assert excinfo.value.message == 'mensagem precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora=1,
                valor=10000, taxa_embarque=0
            )
        assert excinfo.value.message == 'data_hora precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora='2011-12-07T11:43:37',
                valor='10000', taxa_embarque=0
            )
        assert excinfo.value.message == 'valor precisa ser do tipo inteiro.'

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora='2011-12-07T11:43:37',
                valor=10000, taxa_embarque='0'
            )
        assert excinfo.value.message == 'taxa_embarque precisa ser do tipo inteiro.'


class TestXmlToObject(TestCase):

    def test_autorizacao_direta(self):
        transacao = xml_to_object(
            open(os.path.join(BASE_DIR, 'xml1.xml')).read()
        )
        self.assertEqual(transacao.tid, '100699306948372E1001')
        self.assertEqual(
            transacao.pan, 'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
        )
        self.assertEqual(transacao.status, 6)
        self.assertTrue(isinstance(transacao.pedido, Pedido))
        self.assertTrue(isinstance(transacao.pagamento, Pagamento))
        self.assertTrue(isinstance(transacao.autenticacao, Autenticacao))
        self.assertTrue(isinstance(transacao.autorizacao, Autorizacao))
        self.assertTrue(isinstance(transacao.captura, Captura))

    def test_autorizacao_direta_com_gerar_token(self):
        transacao = xml_to_object(
            open(os.path.join(BASE_DIR, 'xml3.xml')).read()
        )
        self.assertEqual(transacao.tid, '10069930694847D91001')
        self.assertEqual(
            transacao.pan, 'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
        )
        self.assertEqual(transacao.status, 6)
        self.assertTrue(isinstance(transacao.pedido, Pedido))
        self.assertTrue(isinstance(transacao.pagamento, Pagamento))
        self.assertTrue(isinstance(transacao.autenticacao, Autenticacao))
        self.assertTrue(isinstance(transacao.autorizacao, Autorizacao))
        self.assertTrue(isinstance(transacao.captura, Captura))
        self.assertTrue(isinstance(transacao.token, Token))

    def test_transacao_autenticada(self):
        transacao = xml_to_object(
            open(os.path.join(BASE_DIR, 'xml2.xml')).read()
        )
        self.assertTrue(isinstance(transacao, Transacao))
        self.assertEqual(transacao.tid, '1006993069483CE61001')
        self.assertEqual(
            transacao.pan, 'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
        )
        self.assertEqual(transacao.status, 0)
        self.assertEqual(
            transacao.url_autenticacao,
            'https://qasecommerce.cielo.com.br/web/index.cbmp?id=5a3a7c089f5299f535dcdd1f502a38ba'
        )
        self.assertTrue(isinstance(transacao.pedido, Pedido))
        self.assertTrue(isinstance(transacao.pagamento, Pagamento))
        self.assertFalse(transacao.autenticacao)
        self.assertFalse(transacao.autorizacao)
        self.assertFalse(transacao.captura)

    def test_token(self):
        token = xml_to_object(
            open(os.path.join(BASE_DIR, 'xml4.xml')).read()
        )
        self.assertTrue(isinstance(token, Token))
        self.assertEqual(
            token.codigo, 'HYcQ0MQ39fl8kn9OR7lFsTtxa+wNuM4lqQLUeN5SYZY='
        )
        self.assertEqual(token.status, 1)
        self.assertEqual(token.numero, '211141******2104')

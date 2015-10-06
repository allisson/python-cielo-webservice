# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase
import pytest
import os

from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Autenticacao, Autorizacao, Token,
    Transacao, Avs, Captura, Cancelamento, xml_to_object
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestComercial(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Comercial(numero='1234', chave='1234')
        assert 'numero precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Comercial(numero=1234, chave=1234)
        assert 'chave precisa ser do tipo string.' in str(excinfo.value)


class TestCartao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero='1234', validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert 'numero precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade='201805', indicador=1,
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert 'validade precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador='1',
                codigo_seguranca=123, nome_portador='Fulano Silva'
            )
        assert 'indicador precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca='123', nome_portador='Fulano Silva'
            )
        assert 'codigo_seguranca precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cartao(
                numero=1234, validade=201805, indicador=1,
                codigo_seguranca=123, nome_portador=123
            )
        assert 'nome_portador precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cartao(token=123)
        assert 'token precisa ser do tipo string.' in str(excinfo.value)


class TestPedido(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero=1234, valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37',
            )
        assert 'numero precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor='10000', moeda=986,
                data_hora='2011-12-07T11:43:37',
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda='986',
                data_hora='2011-12-07T11:43:37',
            )
        assert 'moeda precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora=20111207,
            )
        assert 'data_hora precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', descricao=123
            )
        assert 'descricao precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', idioma=123
            )
        assert 'idioma precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', taxa_embarque='123'
            )
        assert 'taxa_embarque precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pedido(
                numero='1234', valor=10000, moeda=986,
                data_hora='2011-12-07T11:43:37', soft_descriptor=123
            )
        assert 'soft_descriptor precisa ser do tipo string.' in str(excinfo.value)


class TestPagamento(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira=1, produto=1, parcelas=1)
        assert 'bandeira precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira='visa', produto=1, parcelas=1)
        assert 'produto precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Pagamento(bandeira='visa', produto='1', parcelas='1')
        assert 'parcelas precisa ser do tipo inteiro.' in str(excinfo.value)


class TestAutenticacao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )
        assert 'codigo precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, eci=7
            )
        assert 'mensagem precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, eci=7
            )
        assert 'data_hora precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', eci=7
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autenticacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, eci='7'
            )
        assert 'eci precisa ser do tipo inteiro.' in str(excinfo.value)


class TestAutorizacao(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo='1', mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert 'codigo precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert 'mensagem precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora=201112,
                valor=10000, lr=1, arp=1, nsu=1
            )
        assert 'data_hora precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor='10000', lr=1, arp=1, nsu=1
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr='1', arp=1, nsu=1
            )
        assert 'lr precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp='1', nsu=1
            )
        assert 'arp precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Autorizacao(
                codigo=1, mensagem='msg', data_hora='2011-12-07T11:43:37',
                valor=10000, lr=1, arp=1, nsu='1'
            )
        assert 'nsu precisa ser do tipo inteiro.' in str(excinfo.value)


class TestToken(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Token(codigo=1, status=1, numero='1234')
        assert 'codigo precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Token(codigo='code', status='1', numero='1234')
        assert 'status precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Token(codigo='code', status=1, numero=1234)
        assert 'numero precisa ser do tipo string.' in str(excinfo.value)


class TestAvs(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco=1, complemento='', numero=1, bairro='Bairro',
                cep='00000-000'
            )
        assert 'endereco precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento=1, numero=1, bairro='Bairro',
                cep='00000-000'
            )
        assert 'complemento precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero='1', bairro='Bairro',
                cep='00000-000'
            )
        assert 'numero precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero=1, bairro=1,
                cep='00000-000'
            )
        assert 'bairro precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Avs(
                endereco='Rua 1', complemento='', numero=1, bairro='Bairro',
                cep=00000000
            )
        assert 'cep precisa ser do tipo string.' in str(excinfo.value)


class TestCaptura(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo='1', mensagem='mensagem',
                data_hora='2011-12-07T11:43:37', valor=10000, taxa_embarque=0
            )
        assert 'codigo precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000, taxa_embarque=0
            )
        assert 'mensagem precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora=1,
                valor=10000, taxa_embarque=0
            )
        assert 'data_hora precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora='2011-12-07T11:43:37',
                valor='10000', taxa_embarque=0
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Captura(
                codigo=1, mensagem='mensagem', data_hora='2011-12-07T11:43:37',
                valor=10000, taxa_embarque='0'
            )
        assert 'taxa_embarque precisa ser do tipo inteiro.' in str(excinfo.value)


class TestCancelamento(TestCase):

    def test_validate(self):
        with pytest.raises(TypeError) as excinfo:
            Cancelamento(
                codigo='1', mensagem='mensagem',
                data_hora='2011-12-07T11:43:37', valor=10000,
            )
        assert 'codigo precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cancelamento(
                codigo=1, mensagem=1, data_hora='2011-12-07T11:43:37',
                valor=10000,
            )
        assert 'mensagem precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cancelamento(
                codigo=1, mensagem='mensagem', data_hora=201112, valor=10000
            )
        assert 'data_hora precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Cancelamento(
                codigo=1, mensagem='mensagem',
                data_hora='2011-12-07T11:43:37', valor='10000',
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)


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
        cancelamento = Cancelamento(
            codigo=1, mensagem='mensagem', data_hora='2011-12-07T11:43:37',
            valor=10000,
        )

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=1, cartao=cartao, pedido=pedido,
                pagamento=pagamento,
            )
        assert 'comercial precisa ser do tipo Comercial.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=1, pedido=pedido,
                pagamento=pagamento,
            )
        assert 'cartao precisa ser do tipo Cartao.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=1,
                pagamento=pagamento,
            )
        assert 'pedido precisa ser do tipo Pedido.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=1,
            )
        assert 'pagamento precisa ser do tipo Pagamento.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar='1'
            )
        assert 'autorizar precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autorizar=1, url_retorno=1
            )
        assert 'url_retorno precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, capturar='false'
            )
        assert 'capturar precisa ser do tipo booleano.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, campo_livre=1
            )
        assert 'campo_livre precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, bin='1234'
            )
        assert 'bin precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, gerar_token='false', avs=avs
            )
        assert 'gerar_token precisa ser do tipo booleano.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, avs=1
            )
        assert 'avs precisa ser do tipo Avs.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=1, autorizacao=autorizacao
            )
        assert 'autenticacao precisa ser do tipo Autenticacao.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=autenticacao, autorizacao=1,
                captura=captura
            )
        assert 'autorizacao precisa ser do tipo Autorizacao.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, autenticacao=autenticacao,
                autorizacao=autorizacao, captura=1
            )
        assert 'captura precisa ser do tipo Captura.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid=1, pan='pan', status=1
            )
        assert 'tid precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan=1, status=1
            )
        assert 'pan precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status='1',
                url_autenticacao='http://google.com'
            )
        assert 'status precisa ser do tipo inteiro.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1,
                url_autenticacao=1, token=token
            )
        assert 'url_autenticacao precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1, token=1,
                cancelamento=cancelamento
            )
        assert 'token precisa ser do tipo Token.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Transacao(
                comercial=comercial, cartao=cartao, pedido=pedido,
                pagamento=pagamento, tid='1', pan='pan', status=1,
                cancelamento=1
            )
        assert 'cancelamento precisa ser do tipo Cancelamento.' in str(excinfo.value)


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

    def test_cancelamento(self):
        transacao = xml_to_object(
            open(os.path.join(BASE_DIR, 'xml7.xml')).read()
        )
        self.assertTrue(isinstance(transacao, Transacao))
        self.assertEqual(transacao.tid, '1006993069484E8B1001')
        self.assertEqual(
            transacao.pan, 'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
        )
        self.assertTrue(isinstance(transacao.cancelamento, Cancelamento))
        self.assertEqual(transacao.cancelamento.codigo, 9)
        self.assertEqual(
            transacao.cancelamento.mensagem, 'Transacao cancelada com sucesso'
        )
        self.assertEqual(
            transacao.cancelamento.data_hora, '2015-10-06T16:45:10.547-03:00'
        )
        self.assertEqual(transacao.cancelamento.valor, 10000)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase, skip
from datetime import datetime
import pytest
import mock
import os
import uuid
from jinja2 import TemplateNotFound

from cielo_webservice.request import CieloRequest
from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Transacao, Avs, Token, Captura,
    Cancelamento
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MockedResponse(object):

    def __init__(self, data):
        self.data = data

    @property
    def text(self):
        return self.data

    @property
    def content(self):
        return self.data


def token_mocked_response(*args, **kwargs):
    data = open(os.path.join(BASE_DIR, 'xml4.xml')).read()
    return MockedResponse(data)


def capturar_mocked_response(*args, **kwargs):
    data = open(os.path.join(BASE_DIR, 'xml5.xml')).read()
    return MockedResponse(data)


def autorizar_mocked_response(*args, **kwargs):
    data = open(os.path.join(BASE_DIR, 'xml6.xml')).read()
    return MockedResponse(data)


def cancelar_mocked_response(*args, **kwargs):
    data = open(os.path.join(BASE_DIR, 'xml7.xml')).read()
    return MockedResponse(data)


class TestCieloRequest(TestCase):

    def setUp(self):
        self.comercial = Comercial(
            numero=1006993069,
            chave='25fbb99741c739dd84d7b06ec78c9bac718838630f30b112d033ce2e621b34f3'
        )
        self.cartao = Cartao(
            numero=4012001037141112, validade=201805, indicador=1,
            codigo_seguranca=123, nome_portador='Fulano Silva'
        )
        self.pedido = Pedido(
            numero='1234', valor=10000, moeda=986,
            data_hora=datetime.now().isoformat(),
        )
        self.pagamento = Pagamento(bandeira='visa', produto='1', parcelas=1)
        self.request = CieloRequest(sandbox=True)

    def test_render_template(self):
        with pytest.raises(TemplateNotFound) as excinfo:
            self.request.render_template('notfound.xml', id=str(uuid.uuid4()))
        assert 'notfound.xml' in str(excinfo.value)

    @mock.patch('requests.post', autorizar_mocked_response)
    def test_autorizar(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.autorizar('transacao')
        assert 'transacao precisa ser do tipo Transacao.' in str(excinfo.value)

        transacao = Transacao(
            comercial=self.comercial, cartao=self.cartao, pedido=self.pedido,
            pagamento=self.pagamento, autorizar=3, capturar=True
        )
        transacao = self.request.autorizar(transacao=transacao)
        self.assertTrue(isinstance(transacao, Transacao))
        self.assertEqual(transacao.tid, '1006993069484E8B1001')
        self.assertEqual(
            transacao.pan, 'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
        )

    @mock.patch('requests.post', capturar_mocked_response)
    def test_capturar(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.capturar(tid=1, comercial=self.comercial)
        assert 'tid precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            self.request.capturar(tid='tid', comercial=1)
        assert 'comercial precisa ser do tipo Comercial.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            self.request.capturar(
                tid='tid', comercial=self.comercial, valor='10000'
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        transacao = self.request.capturar(
            tid='10069930694849051001', comercial=self.comercial
        )
        self.assertTrue(isinstance(transacao, Transacao))
        self.assertTrue(isinstance(transacao.captura, Captura))

    @mock.patch('requests.post', token_mocked_response)
    def test_gerar_token(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.gerar_token(comercial=1, cartao=self.cartao)
        assert 'comercial precisa ser do tipo Comercial.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            self.request.gerar_token(comercial=self.comercial, cartao=1)
        assert 'cartao precisa ser do tipo Cartao.' in str(excinfo.value)

        token = self.request.gerar_token(
            comercial=self.comercial, cartao=self.cartao
        )
        self.assertTrue(isinstance(token, Token))

    @mock.patch('requests.post', cancelar_mocked_response)
    def test_cancelar(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.cancelar(tid=1, comercial=self.comercial)
        assert 'tid precisa ser do tipo string.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            self.request.cancelar(tid='tid', comercial=1)
        assert 'comercial precisa ser do tipo Comercial.' in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            self.request.cancelar(
                tid='tid', comercial=self.comercial, valor='10000'
            )
        assert 'valor precisa ser do tipo inteiro.' in str(excinfo.value)

        transacao = self.request.cancelar(
            tid='1006993069484E8B1001', comercial=self.comercial
        )
        self.assertTrue(isinstance(transacao, Transacao))
        self.assertTrue(isinstance(transacao.cancelamento, Cancelamento))

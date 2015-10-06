# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase
from datetime import datetime
import pytest
import mock
import os

from cielo_webservice.request import CieloRequest
from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Transacao, Avs, Token
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

    def test_autorizar(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.autorizar('transacao')
            assert excinfo.value.message == 'transacao precisa ser do tipo Transacao.'

    def test_capturar(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.capturar(tid=1, comercial=self.comercial)
            assert excinfo.value.message == 'tid precisa ser do tipo string.'

        with pytest.raises(TypeError) as excinfo:
            self.request.capturar(tid='tid', comercial=1)
            assert excinfo.value.message == 'comercial precisa ser do tipo Comercial.'

    @mock.patch('requests.post', token_mocked_response)
    def test_token(self):
        with pytest.raises(TypeError) as excinfo:
            self.request.token(comercial=1, cartao=self.cartao)
            assert excinfo.value.message == 'comercial precisa ser do tipo Comercial.'

        with pytest.raises(TypeError) as excinfo:
            self.request.token(comercial=self.comercial, cartao=1)
            assert excinfo.value.message == 'cartao precisa ser do tipo Cartao.'

        token = self.request.token(
            comercial=self.comercial, cartao=self.cartao
        )
        self.assertTrue(isinstance(token, Token))

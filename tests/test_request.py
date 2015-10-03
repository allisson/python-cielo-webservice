# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase, skip

from cielo_webservice.request import CieloRequest
from cielo_webservice.models import (
    Comercial, Cartao, Pedido, Pagamento, Transacao
)


class TestCieloRequest(TestCase):

    @skip('pass')
    def test_autorizar(self):
        comercial = Comercial(
            numero=1006993069,
            chave='25fbb99741c739dd84d7b06ec78c9bac718838630f30b112d033ce2e621b34f3'
        )
        cartao = Cartao(
            numero=4012001037141112, validade=201805, indicador=1,
            codigo_seguranca=123, nome_portador='Fulano Silva'
        )
        pedido = Pedido(
            numero='1234', valor=10000, moeda=986,
            data_hora='2011-12-07T11:43:37',
        )
        pagamento = Pagamento(bandeira='visa', produto='1', parcelas=1)
        transacao = Transacao(
            comercial=comercial, cartao=cartao, pedido=pedido,
            pagamento=pagamento,
        )
        request = CieloRequest(sandbox=True)
        request.autorizar(transacao)

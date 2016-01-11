Tutorial
=========

O python-cielo-webservice é uma biblioteca para trabalhar com a versão Webservice 1.5 da Cielo.

Funciona com as versões 2.7/3.3/3.4/3.5 do Python.

===========
Instalação
===========

Instale usando o pip::
    
    pip install python-cielo-webservice

=================
Primeiros passos
=================

Vamos começar abrindo um shell simples do Python::

    python

Fazendo os imports necessários::
    
    >>> from cielo_webservice.request import CieloRequest
    >>> from cielo_webservice.models import Comercial, Cartao, Pedido, Pagamento, Transacao
    >>> from datetime import datetime


Adicionando dados do estabelecimento comercial::

    >>> comercial = Comercial(numero=1006993069, chave='25fbb99741c739dd84d7b06ec78c9bac718838630f30b112d033ce2e621b34f3')

Adicionando dados do cartão::

    >>> cartao = Cartao(numero=4012001037141112, validade=201805, indicador=1, codigo_seguranca=123, nome_portador='Fulano Silva')

Adicionando dados do pedido::

    >>> pedido = Pedido(numero='1234', valor=10000, moeda=986, data_hora=datetime.now().isoformat())

Adicionando dados do pagamento::
    
    >>> pagamento = Pagamento(bandeira='visa', produto='1', parcelas=1)

Criando a transação::
    
    >>> transacao = Transacao(comercial=comercial, cartao=cartao, pedido=pedido, pagamento=pagamento, autorizar=3, capturar=True)

Iniciando o objeto CieloRequest::

    >>> request = CieloRequest(sandbox=True)

Autorizando a transação::

    >>> transacao_autorizada = request.autorizar(transacao=transacao)
    >>> transacao_autorizada.tid
    u'100699306900050C244A'
    >>> transacao_autorizada.pan
    u'IqVz7P9zaIgTYdU41HaW/OB/d7Idwttqwb2vaTt8MT0='
    >>> print(transacao_autorizada.autenticacao.codigo)
    6
    >>> print(transacao_autorizada.autenticacao.data_hora)
    2016-01-11T17:38:16.256-02:00
    >>> print(transacao_autorizada.autenticacao.eci)
    7
    >>> print(transacao_autorizada.autenticacao.mensagem)
    Transacao sem autenticacao
    >>> print(transacao_autorizada.autenticacao.valor)
    10000
    >>> print(transacao_autorizada.autorizacao.codigo)
    6
    >>> print(transacao_autorizada.autorizacao.mensagem)
    Transação autorizada
    >>> print(transacao_autorizada.autorizacao.data_hora)
    2016-01-11T17:38:16.260-02:00
    >>> print(transacao_autorizada.autorizacao.valor)
    10000
    >>> print(transacao_autorizada.autorizacao.lr)
    0
    >>> print(transacao_autorizada.autorizacao.arp)
    123456
    >>> print(transacao_autorizada.autorizacao.nsu)
    292612

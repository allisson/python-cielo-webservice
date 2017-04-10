# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import six
import xmltodict
from unidecode import unidecode


class Comercial(object):

    """
    Modelo para os dados comerciais da loja.
    """

    def __init__(self, numero=None, chave=None):
        self.numero = numero
        self.chave = chave
        self.validate()

    def validate(self):
        if not isinstance(self.numero, six.integer_types):
            raise TypeError('numero precisa ser do tipo inteiro.')

        if not isinstance(self.chave, six.string_types):
            raise TypeError('chave precisa ser do tipo string.')

    def __repr__(self):
        return '<Comercial(numero={}, chave={})>'.format(
            self.numero, self.chave
        )


class Cartao(object):

    """
    Modelo para os dados do cartão.
    """

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
        if self.numero is not None and not isinstance(self.numero, six.integer_types):
            raise TypeError('numero precisa ser do tipo inteiro.')

        if self.validade is not None and not isinstance(self.validade, six.integer_types):
            raise TypeError('validade precisa ser do tipo inteiro.')

        if self.indicador is not None and not isinstance(self.indicador, six.integer_types):
            raise TypeError('indicador precisa ser do tipo inteiro.')

        if self.indicador == 1 and not isinstance(self.codigo_seguranca, six.integer_types):
            raise TypeError('codigo_seguranca precisa ser do tipo inteiro.')

        if self.nome_portador is not None and not isinstance(self.nome_portador, six.string_types):
            raise TypeError('nome_portador precisa ser do tipo string.')

        if self.token is not None and not isinstance(self.token, six.string_types):
            raise TypeError('token precisa ser do tipo string.')

    def __repr__(self):
        return '<Cartao(numero={}, validade={}, indicador={}, codigo_seguranca={}, nome_portador={}, token={})>'.format(
            self.numero, self.validade, self.indicador, self.codigo_seguranca,
            self.nome_portador, self.token
        )


class Pedido(object):

    """
    Modelo para os dados do pedido.
    """

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

        if self.descricao is not None and not isinstance(self.descricao, six.string_types):
            raise TypeError('descricao precisa ser do tipo string.')

        if self.idioma is not None and not isinstance(self.idioma, six.string_types):
            raise TypeError('idioma precisa ser do tipo string.')

        if self.taxa_embarque is not None and not isinstance(self.taxa_embarque, six.integer_types):
            raise TypeError('taxa_embarque precisa ser do tipo inteiro.')

        if self.soft_descriptor is not None and not isinstance(self.soft_descriptor, six.string_types):
            raise TypeError('soft_descriptor precisa ser do tipo string.')

    def __repr__(self):
        return '<Pedido(numero={}, valor={}, moeda={}, data_hora={}, descricao={}, idioma={}, taxa_embarque={}, soft_descriptor={})>'.format(
            self.numero, self.valor, self.moeda, self.data_hora,
            self.descricao, self.idioma, self.taxa_embarque,
            self.soft_descriptor
        )


class Pagamento(object):

    """
    Modelo para os dados do pagamento.
    """

    def __init__(self, bandeira=None, produto=None, parcelas=None):
        self.bandeira = bandeira
        self.produto = produto
        self.parcelas = parcelas
        self.validate()

    def validate(self):
        if not isinstance(self.bandeira, six.string_types):
            raise TypeError('bandeira precisa ser do tipo string.')

        if not isinstance(self.produto, six.string_types):
            raise TypeError('produto precisa ser do tipo string.')

        if not isinstance(self.parcelas, six.integer_types):
            raise TypeError('parcelas precisa ser do tipo inteiro.')

    def __repr__(self):
        return '<Pagamento(bandeira={}, produto={}, parcelas={})>'.format(
            self.bandeira, self.produto, self.parcelas
        )


class Autenticacao(object):

    """
    Modelo para os dados da autenticação.
    """

    def __init__(self, codigo=None, mensagem=None, data_hora=None, valor=None,
                 eci=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.data_hora = data_hora
        self.valor = valor
        self.eci = eci
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.integer_types):
            raise TypeError('codigo precisa ser do tipo inteiro.')

        if not isinstance(self.mensagem, six.string_types):
            raise TypeError('mensagem precisa ser do tipo string.')

        if not isinstance(self.data_hora, six.string_types):
            raise TypeError('data_hora precisa ser do tipo string.')

        if not isinstance(self.valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        if not isinstance(self.eci, six.integer_types):
            raise TypeError('eci precisa ser do tipo inteiro.')

    def __repr__(self):
        return '<Autenticacao(codigo={}, mensagem={}, data_hora={}, valor={}, eci={})>'.format(
            self.codigo, self.mensagem, self.data_hora, self.valor, self.eci
        )


class Autorizacao(object):

    """
    Modelo para os dados da autorização.
    """

    def __init__(self, codigo=None, mensagem=None, data_hora=None, valor=None,
                 lr=None, arp=None, nsu=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.data_hora = data_hora
        self.valor = valor
        self.lr = lr
        self.arp = arp
        self.nsu = nsu
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.integer_types):
            raise TypeError('codigo precisa ser do tipo inteiro.')

        if not isinstance(self.mensagem, six.string_types):
            raise TypeError('mensagem precisa ser do tipo string.')

        if not isinstance(self.data_hora, six.string_types):
            raise TypeError('data_hora precisa ser do tipo string.')

        if not isinstance(self.valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        if not isinstance(self.lr, six.string_types):
            raise TypeError('lr precisa ser do tipo string.')

        if self.arp is not None and not isinstance(self.arp, six.integer_types):
            raise TypeError('arp precisa ser do tipo inteiro.')

        if not isinstance(self.nsu, six.integer_types):
            raise TypeError('nsu precisa ser do tipo inteiro.')

    def __repr__(self):
        return '<Autorizacao(codigo={}, mensagem={}, data_hora={}, valor={}, lr={}, arp={}, nsu={})>'.format(
            self.codigo, self.mensagem, self.data_hora, self.valor, self.lr,
            self.arp, self.nsu
        )


class Token(object):

    """
    Modelo para os dados do token.
    """

    def __init__(self, codigo=None, status=None, numero=None):
        self.codigo = codigo
        self.status = status
        self.numero = numero
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.string_types):
            raise TypeError('codigo precisa ser do tipo string.')

        if not isinstance(self.status, six.integer_types):
            raise TypeError('status precisa ser do tipo inteiro.')

        if not isinstance(self.numero, six.string_types):
            raise TypeError('numero precisa ser do tipo string.')

    def __repr__(self):
        return '<Token(codigo={}, status={}, numero={})>'.format(
            self.codigo, self.status, self.numero
        )


class Avs(object):

    """
    Modelo para os dados do avs (ADDRESS VERIFICATION SERVICE).
    """

    def __init__(self, endereco=None, complemento=None, numero=None,
                 bairro=None, cep=None):
        self.endereco = endereco
        self.complemento = complemento
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.validate()

    def validate(self):
        if not isinstance(self.endereco, six.string_types):
            raise TypeError('endereco precisa ser do tipo string.')

        if not isinstance(self.complemento, six.string_types):
            raise TypeError('complemento precisa ser do tipo string.')

        if not isinstance(self.numero, six.integer_types):
            raise TypeError('numero precisa ser do tipo inteiro.')

        if not isinstance(self.bairro, six.string_types):
            raise TypeError('bairro precisa ser do tipo string.')

        if not isinstance(self.cep, six.string_types):
            raise TypeError('cep precisa ser do tipo string.')

    def __repr__(self):
        return '<Avs(endereco={}, complemento={}, numero={}, bairro={}, cep={})>'.format(
            self.endereco, self.complemento, self.numero, self.bairro, self.cep
        )


class Captura(object):

    """
    Modelo para os dados da captura.
    """

    def __init__(self, codigo=None, mensagem=None, data_hora=None, valor=None,
                 taxa_embarque=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.data_hora = data_hora
        self.valor = valor
        self.taxa_embarque = taxa_embarque
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.integer_types):
            raise TypeError('codigo precisa ser do tipo inteiro.')

        if not isinstance(self.mensagem, six.string_types):
            raise TypeError('mensagem precisa ser do tipo string.')

        if not isinstance(self.data_hora, six.string_types):
            raise TypeError('data_hora precisa ser do tipo string.')

        if not isinstance(self.valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        if self.taxa_embarque is not None and not isinstance(self.taxa_embarque, six.integer_types):
            raise TypeError('taxa_embarque precisa ser do tipo inteiro.')

    def __repr__(self):
        return '<Captura(codigo={}, mensagem={}, data_hora={}, valor={}, taxa_embarque={})>'.format(
            self.codigo, self.mensagem, self.data_hora, self.valor,
            self.taxa_embarque
        )


class Cancelamento(object):

    """
    Modelo para os dados de cancelamento.
    """

    def __init__(self, codigo=None, mensagem=None, data_hora=None, valor=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.data_hora = data_hora
        self.valor = valor
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.integer_types):
            raise TypeError('codigo precisa ser do tipo inteiro.')

        if not isinstance(self.mensagem, six.string_types):
            raise TypeError('mensagem precisa ser do tipo string.')

        if not isinstance(self.data_hora, six.string_types):
            raise TypeError('data_hora precisa ser do tipo string.')

        if not isinstance(self.valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

    def __repr__(self):
        return '<Cancelamento(codigo={}, mensagem={}, data_hora={}, valor={})>'.format(
            self.codigo, self.mensagem, self.data_hora, self.valor
        )


class Erro(object):

    """
    Modelo para os dados de erro do sistema.
    """

    def __init__(self, codigo=None, mensagem=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.validate()

    def validate(self):
        if not isinstance(self.codigo, six.string_types):
            raise TypeError('codigo precisa ser do tipo string.')

        if not isinstance(self.mensagem, six.string_types):
            raise TypeError('mensagem precisa ser do tipo string.')

    def __repr__(self):
        return '<Erro(codigo={}, mensagem={})>'.format(
            self.codigo, self.mensagem
        )


class Transacao(object):

    """
    Modelo para os dados de uma transação.
    """

    def __init__(self, comercial=None, cartao=None, pedido=None,
                 pagamento=None, url_retorno=None, autorizar=None,
                 capturar=None, campo_livre=None, bin=None, gerar_token=None,
                 avs=None, autenticacao=None, autorizacao=None, captura=None,
                 token=None, cancelamento=None, tid=None, pan=None,
                 status=None, url_autenticacao=None):
        self.comercial = comercial
        self.cartao = cartao
        self.pedido = pedido
        self.pagamento = pagamento
        self.url_retorno = url_retorno
        self.autorizar = autorizar
        self.capturar = capturar
        self.campo_livre = campo_livre
        self.bin = bin
        self.gerar_token = gerar_token
        self.avs = avs
        self.autenticacao = autenticacao
        self.autorizacao = autorizacao
        self.captura = captura
        self.token = token
        self.cancelamento = cancelamento
        self.tid = tid
        self.pan = pan
        self.status = status
        self.url_autenticacao = url_autenticacao
        self.validate()

    def validate(self):
        if self.comercial is not None and not isinstance(self.comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')

        if self.cartao is not None and not isinstance(self.cartao, Cartao):
            raise TypeError('cartao precisa ser do tipo Cartao.')

        if not isinstance(self.pedido, Pedido):
            raise TypeError('pedido precisa ser do tipo Pedido.')

        if not isinstance(self.pagamento, Pagamento):
            raise TypeError('pagamento precisa ser do tipo Pagamento.')

        if self.autorizar is not None and not isinstance(self.autorizar, six.integer_types):
            raise TypeError('autorizar precisa ser do tipo inteiro.')

        if self.autorizar == 1 and not isinstance(self.url_retorno, six.string_types):
            raise TypeError('url_retorno precisa ser do tipo string.')

        if self.capturar is not None and not isinstance(self.capturar, bool):
            raise TypeError('capturar precisa ser do tipo booleano.')

        if self.campo_livre is not None and not isinstance(self.campo_livre, six.string_types):
            raise TypeError('campo_livre precisa ser do tipo string.')

        if self.bin is not None and not isinstance(self.bin, six.integer_types):
            raise TypeError('bin precisa ser do tipo inteiro.')

        if self.gerar_token is not None and not isinstance(self.gerar_token, bool):
            raise TypeError('gerar_token precisa ser do tipo booleano.')

        if self.avs is not None and not isinstance(self.avs, Avs):
            raise TypeError('avs precisa ser do tipo Avs.')

        if self.autenticacao is not None and not isinstance(self.autenticacao, Autenticacao):
            raise TypeError('autenticacao precisa ser do tipo Autenticacao.')

        if self.autorizacao is not None and not isinstance(self.autorizacao, Autorizacao):
            raise TypeError('autorizacao precisa ser do tipo Autorizacao.')

        if self.captura is not None and not isinstance(self.captura, Captura):
            raise TypeError('captura precisa ser do tipo Captura.')

        if self.token is not None and not isinstance(self.token, Token):
            raise TypeError('token precisa ser do tipo Token.')

        if self.cancelamento is not None and not isinstance(self.cancelamento, Cancelamento):
            raise TypeError('cancelamento precisa ser do tipo Cancelamento.')

        if self.tid is not None and not isinstance(self.tid, six.string_types):
            raise TypeError('tid precisa ser do tipo string.')

        if self.pan is not None and not isinstance(self.pan, six.string_types):
            raise TypeError('pan precisa ser do tipo string.')

        if self.status is not None and not isinstance(self.status, six.integer_types):
            raise TypeError('status precisa ser do tipo inteiro.')

        if self.url_autenticacao is not None and not isinstance(self.url_autenticacao, six.string_types):
            raise TypeError('url_autenticacao precisa ser do tipo string.')

    def __repr__(self):
        return '<Transacao(comercial={}, cartao={}, pedido={}, pagamento={}, url_retorno={}, autorizar={}, capturar={}, campo_livre={}, bin={}, gerar_token={}, avs={}, autenticacao={}, autorizacao={}, captura={}, token={}, cancelamento={}, tid={}, pan={}, status={}, url_autenticacao={})>'.format(
            self.comercial, self.cartao, self.pedido, self.pagamento,
            self.url_retorno, self.autorizar, self.capturar, self.campo_livre,
            self.bin, self.gerar_token, self.avs, self.autenticacao,
            self.autorizacao, self.captura, self.token, self.cancelamento,
            self.tid, self.pan, self.status, self.url_autenticacao
        )


def xml_to_object(xml):
    data = xmltodict.parse(xml)

    if 'transacao' in data:
        transacao = data['transacao']
        pedido = dict_to_pedido(transacao.get('dados-pedido')) if transacao.get('dados-pedido') else None
        pagamento = dict_to_pagamento(transacao.get('forma-pagamento')) if transacao.get('forma-pagamento') else None
        autenticacao = dict_to_autenticacao(transacao.get('autenticacao')) if transacao.get('autenticacao') else None
        autorizacao = dict_to_autorizacao(transacao.get('autorizacao')) if transacao.get('autorizacao') else None
        token = dict_to_token(transacao.get('token')) if transacao.get('token') else None
        captura = dict_to_captura(transacao.get('captura')) if transacao.get('captura') else None
        cancelamento = dict_to_cancelamento(transacao.get('cancelamentos')) if transacao.get('cancelamentos') else None
        tid = transacao.get('tid') if transacao.get('tid') else None
        pan = transacao.get('pan') if transacao.get('pan') else None
        status = int(transacao.get('status')) if transacao.get('status') else None
        url_autenticacao = transacao.get('url-autenticacao') if transacao.get('url-autenticacao') else None
        return Transacao(
            pedido=pedido,
            pagamento=pagamento,
            autenticacao=autenticacao,
            autorizacao=autorizacao,
            token=token,
            captura=captura,
            cancelamento=cancelamento,
            tid=tid,
            pan=pan,
            status=status,
            url_autenticacao=url_autenticacao,
        )

    if 'retorno-token' in data:
        retorno_token = data['retorno-token']
        return Token(
            codigo=retorno_token['token']['dados-token']['codigo-token'],
            status=int(retorno_token['token']['dados-token']['status']),
            numero=retorno_token['token']['dados-token']['numero-cartao-truncado']
        )

    if 'erro' in data:
        return Erro(
            codigo=data['erro']['codigo'],
            mensagem=data['erro']['mensagem'],
        )


def dict_to_pedido(data):
    descricao = data.get('descricao') if data.get('descricao') else None
    idioma = data.get('idioma') if data.get('idioma') else None
    taxa_embarque = int(data.get('taxa-embarque')) if data.get('taxa-embarque') else None
    soft_descriptor = data.get('soft-descriptor') if data.get('soft-descriptor') else None
    pedido = Pedido(
        numero=data.get('numero'),
        valor=int(data.get('valor')),
        moeda=int(data.get('moeda')),
        data_hora=data.get('data-hora'),
        descricao=descricao,
        idioma=idioma,
        taxa_embarque=taxa_embarque,
        soft_descriptor=soft_descriptor
    )
    return pedido


def dict_to_pagamento(data):
    pagamento = Pagamento(
        bandeira=data.get('bandeira'),
        produto=data.get('produto'),
        parcelas=int(data.get('parcelas')),
    )
    return pagamento


def dict_to_autenticacao(data):
    autenticacao = Autenticacao(
        codigo=int(data.get('codigo')),
        mensagem=unidecode(data.get('mensagem')),
        data_hora=data.get('data-hora'),
        valor=int(data.get('valor')),
        eci=int(data.get('eci')),
    )
    return autenticacao


def dict_to_autorizacao(data):
    autorizacao = Autorizacao(
        codigo=int(data.get('codigo')),
        mensagem=unidecode(data.get('mensagem')),
        data_hora=data.get('data-hora'),
        valor=int(data.get('valor')),
        lr=data.get('lr'),
        arp=int(data.get('arp')) if data.get('arp') else None,
        nsu=int(data.get('nsu')),
    )
    return autorizacao


def dict_to_captura(data):
    taxa_embarque = int(data.get('taxa-embarque')) if data.get('taxa-embarque') else None
    captura = Captura(
        codigo=int(data.get('codigo')),
        mensagem=unidecode(data.get('mensagem')),
        data_hora=data.get('data-hora'),
        valor=int(data.get('valor')),
        taxa_embarque=taxa_embarque,
    )
    return captura


def dict_to_token(data):
    token = Token(
        codigo=data['dados-token']['codigo-token'],
        status=int(data['dados-token']['status']),
        numero=data['dados-token']['numero-cartao-truncado']
    )
    return token


def dict_to_cancelamento(data):
    data = data['cancelamento']
    cancelamento = Cancelamento(
        codigo=int(data.get('codigo')),
        mensagem=unidecode(data.get('mensagem')),
        data_hora=data.get('data-hora'),
        valor=int(data.get('valor'))
    )
    return cancelamento

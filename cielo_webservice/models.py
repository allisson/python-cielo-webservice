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


class Pagamento(object):

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


class Autenticacao(object):

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


class Autorizacao(object):

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

        if not isinstance(self.lr, six.integer_types):
            raise TypeError('lr precisa ser do tipo inteiro.')

        if not isinstance(self.arp, six.integer_types):
            raise TypeError('arp precisa ser do tipo inteiro.')

        if not isinstance(self.nsu, six.integer_types):
            raise TypeError('nsu precisa ser do tipo inteiro.')


class Transacao(object):

    def __init__(self, comercial=None, cartao=None, pedido=None,
                 pagamento=None, url_retorno=None, autorizar=3, capturar=True,
                 campo_livre=None, bin=None, gerar_token=False, avs=None,
                 autenticacao=None, autorizacao=None, tid=None, pan=None,
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
        self.tid = tid
        self.pan = pan
        self.status = status
        self.url_autenticacao = url_autenticacao
        self.validate()

    def validate(self):
        if not isinstance(self.comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')

        if not isinstance(self.cartao, Cartao):
            raise TypeError('cartao precisa ser do tipo Cartao.')

        if not isinstance(self.pedido, Pedido):
            raise TypeError('pedido precisa ser do tipo Pedido.')

        if not isinstance(self.pagamento, Pagamento):
            raise TypeError('pagamento precisa ser do tipo Pagamento.')

        if not isinstance(self.autorizar, six.integer_types):
            raise TypeError('autorizar precisa ser do tipo inteiro.')

        if self.autorizar == 1 and not isinstance(self.url_retorno, six.string_types):
            raise TypeError('url_retorno precisa ser do tipo string.')

        if not isinstance(self.capturar, bool):
            raise TypeError('capturar precisa ser do tipo booleano.')

        if self.campo_livre and not isinstance(self.campo_livre, six.string_types):
            raise TypeError('campo_livre precisa ser do tipo string.')

        if self.bin and not isinstance(self.bin, six.integer_types):
            raise TypeError('bin precisa ser do tipo inteiro.')

        if not isinstance(self.gerar_token, bool):
            raise TypeError('gerar_token precisa ser do tipo booleano.')

        if self.avs and not isinstance(self.avs, six.string_types):
            raise TypeError('avs precisa ser do tipo string.')

        if self.autenticacao and not isinstance(self.autenticacao, Autenticacao):
            raise TypeError('autenticacao precisa ser do tipo Autenticacao.')

        if self.autorizacao and not isinstance(self.autorizacao, Autorizacao):
            raise TypeError('autorizacao precisa ser do tipo Autorizacao.')

        if self.tid and not isinstance(self.tid, six.string_types):
            raise TypeError('tid precisa ser do tipo string.')

        if self.pan and not isinstance(self.pan, six.string_types):
            raise TypeError('pan precisa ser do tipo string.')

        if self.status and not isinstance(self.status, six.integer_types):
            raise TypeError('status precisa ser do tipo inteiro.')

        if self.url_autenticacao and not isinstance(self.url_autenticacao, six.string_types):
            raise TypeError('url_autenticacao precisa ser do tipo string.')

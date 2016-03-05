# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import requests
import uuid
import six

from cielo_webservice.models import (
    Cartao, Transacao, Comercial, Erro, xml_to_object
)
from cielo_webservice.exceptions import CieloRequestError
from cielo_webservice.adapter import TLSv1HttpAdapter


BASE_URL = 'https://ecommerce.cielo.com.br/servicos/ecommwsec.do'
SANDBOX_BASE_URL = 'https://qasecommerce.cielo.com.br/servicos/ecommwsec.do'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class CieloRequest(object):

    """
    Objeto que vai realizar a comunicação com a api da Cielo.
    """

    def __init__(self, sandbox=False):
        self.base_url = BASE_URL
        if sandbox:
            self.base_url = SANDBOX_BASE_URL
        self.template_env = self.create_template_env()
        self.session = requests.Session()
        self.session.mount('https://', TLSv1HttpAdapter())

    def create_template_env(self):
        template_dirs = []
        template_dirs.append(os.path.join(BASE_DIR, 'templates'))
        template_env = Environment(
            loader=FileSystemLoader(template_dirs), autoescape=True
        )
        return template_env

    def render_template(self, template_name, **kwargs):
        try:
            template = self.template_env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        return template.render(kwargs)

    def autorizar(self, transacao):
        """
        Realiza uma autorização.
        """
        if not isinstance(transacao, Transacao):
            raise TypeError('transacao precisa ser do tipo Transacao.')

        xml = self.render_template(
            'transacao.xml', id=str(uuid.uuid4()), transacao=transacao
        )
        response = self.session.post(self.base_url, data={'mensagem': xml})
        object_data = xml_to_object(response.text)

        if isinstance(object_data, Erro):
            raise CieloRequestError('{0} - {1}'.format(
                object_data.codigo, object_data.mensagem)
            )

        return object_data

    def capturar(self, tid=None, comercial=None, valor=None,
                 taxa_embarque=None):
        """
        Realiza o processo de captura de uma transação.
        """
        if not isinstance(tid, six.string_types):
            raise TypeError('tid precisa ser do tipo string.')
        if not isinstance(comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')
        if valor is not None and not isinstance(valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        xml = self.render_template(
            'captura.xml', id=str(uuid.uuid4()), tid=tid, comercial=comercial,
            valor=valor, taxa_embarque=taxa_embarque
        )
        response = self.session.post(self.base_url, data={'mensagem': xml})
        object_data = xml_to_object(response.text)

        if isinstance(object_data, Erro):
            raise CieloRequestError('{0} - {1}'.format(
                object_data.codigo, object_data.mensagem)
            )

        return object_data

    def gerar_token(self, comercial=None, cartao=None):
        """
        Gera o token de um cartão de crédito.
        """
        if not isinstance(comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')

        if not isinstance(cartao, Cartao):
            raise TypeError('cartao precisa ser do tipo Cartao.')

        xml = self.render_template(
            'token.xml', id=str(uuid.uuid4()), comercial=comercial,
            cartao=cartao
        )
        response = self.session.post(self.base_url, data={'mensagem': xml})
        object_data = xml_to_object(response.text)

        if isinstance(object_data, Erro):
            raise CieloRequestError('{0} - {1}'.format(
                object_data.codigo, object_data.mensagem)
            )

        return object_data

    def cancelar(self, tid=None, comercial=None, valor=None):
        """
        Cancela uma transação.
        """
        if not isinstance(tid, six.string_types):
            raise TypeError('tid precisa ser do tipo string.')
        if not isinstance(comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')
        if valor is not None and not isinstance(valor, six.integer_types):
            raise TypeError('valor precisa ser do tipo inteiro.')

        xml = self.render_template(
            'cancelamento.xml', id=str(uuid.uuid4()), tid=tid,
            comercial=comercial, valor=valor
        )
        response = self.session.post(self.base_url, data={'mensagem': xml})
        object_data = xml_to_object(response.text)

        if isinstance(object_data, Erro):
            raise CieloRequestError('{0} - {1}'.format(
                object_data.codigo, object_data.mensagem)
            )

        return object_data

    def consultar(self, tid=None, comercial=None):
        """
        Retorna os dados de uma transação.
        """
        if not isinstance(tid, six.string_types):
            raise TypeError('tid precisa ser do tipo string.')
        if not isinstance(comercial, Comercial):
            raise TypeError('comercial precisa ser do tipo Comercial.')

        xml = self.render_template(
            'consulta.xml', id=str(uuid.uuid4()), tid=tid,
            comercial=comercial
        )
        response = self.session.post(self.base_url, data={'mensagem': xml})
        object_data = xml_to_object(response.text)

        if isinstance(object_data, Erro):
            raise CieloRequestError('{0} - {1}'.format(
                object_data.codigo, object_data.mensagem)
            )

        return object_data

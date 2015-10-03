# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import requests
import uuid

from cielo_webservice.models import Transacao


BASE_URL = 'https://ecommerce.cielo.com.br/servicos/ecommwsec.do'
SANDBOX_BASE_URL = 'https://qasecommerce.cielo.com.br/servicos/ecommwsec.do'
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class CieloRequest(object):

    def __init__(self, sandbox=False):
        self.base_url = BASE_URL
        if sandbox:
            self.base_url = SANDBOX_BASE_URL
        self.template_env = self.create_template_env()

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
        if not isinstance(transacao, Transacao):
            raise TypeError('transacao precisa ser do tipo Transacao.')
        xml = self.render_template(
            'transacao.xml', id=str(uuid.uuid4()), transacao=transacao
        )
        response = requests.post(self.base_url, data={'mensagem': xml})

    def capturar(self):
        pass

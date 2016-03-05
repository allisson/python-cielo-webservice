# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Command
import cielo_webservice

requires = [
    'requests>=2.9.1',
    'jinja2',
    'six',
    'xmltodict',
    'Unidecode',
    'mock',
]

testing_extras = [
    'pytest',
    'pytest-cov',
]


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='python-cielo-webservice',
    version=cielo_webservice.__version__,
    author=cielo_webservice.__author__,
    author_email=cielo_webservice.__author_email__,
    packages=find_packages(),
    license='MIT',
    description=cielo_webservice.__description__,
    url='https://github.com/allisson/python-cielo-webservice',
    keywords='Payment, Payment Gateway, Cielo',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
    cmdclass={'test': PyTest},
)

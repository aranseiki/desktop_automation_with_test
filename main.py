"""
from distutils.command.config import config
from time import sleep
from lib.application_utils import (
    iniciar_app, encerrar_app, digitar,
    clicar, coletar_situacao_janela, restaurar_janela,
    coletar_dados_selecao
)
from lib.python_utils import logging_msg, variavel_ambiente
from configparser import ConfigParser


config = ConfigParser()
config.read('env.ini')
config_padrao = dict(config['padrao'])
executavel = config_padrao['executavel']


app = iniciar_app(executavel)
"""


messaging = 'teste'
status = 'Ok'
level = 'critical'
filename = '.\\logs\\log.txt'
filemode = 'a'
formating = 'nivel;data;situacao;mensagem'
formater = '%(levelname)s;%(asctime)s;' + status + ';' + messaging
encoding = None
handlers = None

def formater(*args, delimitador=';'):
    lista = args
    lista_montada = ''
    for item in lista:
        # breakpoint()
        lista_montada += item + delimitador
    print(lista_montada)

formater('Ola', 'teste', 'critical', delimitador=';')

# logged = logging_msg(messaging, level, filename, filemode, encoding, formater)
# print(logged)

"""
nome_janela = 'Free Mouse Clicker'
print(coletar_situacao_janela(nome_janela))

valor = 10
caminho_campo = 'Free Mouse Clicker->Minutes'
digitar(caminho_campo, valor)
sleep(3)

caminho_campo = 'Free Mouse Clicker->Start'
clicar(caminho_campo)
sleep(1)

nome_janela = 'Free Mouse Clicker'
restaurar_janela(nome_janela)
sleep(3)

caminho_campo = 'Free Mouse Clicker->Stop'
clicar(caminho_campo)
sleep(3)

caminho_campo = 'Free Mouse Clicker->combobox'
coletar_dados_selecao(caminho_campo)

encerrar_app(executavel)
"""

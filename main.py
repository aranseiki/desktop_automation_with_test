from cgitb import handler
from distutils.debug import DEBUG
from distutils.log import ERROR, INFO, debug
from time import sleep
from lib.application_utils import (
    iniciar_app, encerrar_app, digitar,
    clicar, coletar_situacao_janela, restaurar_janela,
    coletar_dados_selecao
)
from lib.python_utils import logging_msg

executavel = U'C:\\Users\\aoalmeida2\\Documents\\\
desktop_automation_with_test\\mouseclicker.exe'

app = iniciar_app(executavel)

mensagem = '123'
message = 'teste'
level = 'debug'
filename = 'arquivo.txt'
filemode = 'a'
logged = logging_msg(message, level, filename, filemode)

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

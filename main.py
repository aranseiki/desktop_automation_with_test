import platform
from time import sleep

platform.architecture()
from lib.application_utils import (
    clicar,
    coletar_dados_selecao,
    coletar_situacao_janela,
    digitar,
    encerrar_app,
    iniciar_app,
    restaurar_janela,
)
from lib.python_utils import (
    formatar_log,
    logger,
    retornar_data_hora_atual,
    variavel_ambiente,
)

executavel = config_padrao = variavel_ambiente(nome_variavel='executavel')

variavel_ambiente_sistema = variavel_ambiente(
    nome_variavel='USERNAME', variavel_systema=True
)
print(variavel_ambiente_sistema)

app = iniciar_app(executavel)


messaging = 'teste'
status = 'Ok'
data = retornar_data_hora_atual('%d/%m/%Y')
hora = retornar_data_hora_atual('%H:%M:%S')
dataHora = data + ' - ' + hora
level = 'critical'
filename = './logs/log.txt'
filemode = 'a'
formating = formatar_log(dataHora, status, messaging)
encoding = 'utf8'

logged = logger(messaging, level, filename, filemode, encoding, formating)
print(logged)


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

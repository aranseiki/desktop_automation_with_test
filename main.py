from time import sleep
from lib.application_utils import (
    iniciar_app, encerrar_app, digitar,
    clicar, coletar_situacao_janela, restaurar_janela,
    coletar_dados_selecao
)
from lib.python_utils import (
    logging_msg, variavel_ambiente, formatar_log,
    retornar_data_hora_atual
)


executavel = config_padrao = variavel_ambiente(
    nome_variavel='executavel'
)

app = iniciar_app(executavel)


messaging = 'teste'
status = 'Ok'
data = retornar_data_hora_atual('%d/%m/%Y')
hora = retornar_data_hora_atual('%H:%M:%S')
dataHora = data + ' - ' + hora
level = 'critical'
filename = '.\\logs\\log.txt'
filemode = 'a'
formating = formatar_log(
    dataHora,
    status,
    messaging
)
encoding = 'utf8'

logged = logging_msg(
    messaging,
    level,
    filename,
    filemode,
    encoding,
    formating
)
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

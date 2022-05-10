from time import sleep

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
    abrir_arquivo_em_bytes,
    abrir_arquivo_texto,
    arquivo_existente,
    coletar_extensao_arquivo,
    coletar_nome_arquivo,
    copiar_arquivo,
    copiar_pasta,
    criar_arquivo_texto,
    criar_pasta,
    excluir_arquivo,
    excluir_pasta,
    formatar_log,
    ler_variavel_ambiente,
    logger,
    pasta_existente,
    pasta_vazia,
    recortar,
    renomear,
    retornar_arquivos_em_pasta,
    retornar_data_hora_atual,
)


def cls():
    import os
    os.system('cls')


"""

ler_variavel_ambiente(
    arquivo_config='config.ini',
    nome_bloco_config='padrao',
    nome_variavel=None,
    variavel_systema=False,
)

ler_variavel_ambiente(
    nome_variavel='USERNAME',
    variavel_systema=True
)

executavel = ler_variavel_ambiente(nome_variavel='executavel')

"""

"""
caminho = './exemplo'
pasta_existente(caminho)
criar_pasta(caminho)

pasta_vazia(caminho)

caminho = './'
nome_atual = 'exemplo'
novo_nome = 'exemplo_novo'
renomear(caminho, nome_atual, novo_nome)

caminho = './exemplo_novo'
excluir_pasta(caminho, vazia = True)

pasta = './exemplo'
caminho_destino = './exemplo2'
copiar_pasta(pasta, caminho_destino)

caminho_atual = './exemplo'
caminho_novo = './exemplo2/exemplo'
recortar(caminho_atual, caminho_novo)
"""

"""
caminho = './exemplo.txt'
arquivo_existente(caminho)
criar_arquivo_texto(caminho, data='', encoding='utf8')
excluir_arquivo(caminho)
abrir_arquivo_texto(caminho, encoding='utf8')
abrir_arquivo_em_bytes(caminho)

arquivo = './exemplo.txt'
caminho_destino = 'exemplo'
copiar_arquivo(arquivo, caminho_destino)

caminho = './exemplo.txt'
coletar_nome_arquivo(caminho)
coletar_extensao_arquivo(caminho)

caminho = './'
nome_atual = 'exemplo.txt'
novo_nome = 'exemplo_novo.txt'
renomear(caminho, nome_atual, novo_nome)

caminho_atual = './exemplo.txt'
caminho_novo = './exemplo/exemplo.txt'
recortar(caminho_atual, caminho_novo)
retornar_arquivos_em_pasta(caminho, filtro='**/*')
"""

"""
messaging = 'teste'
level = 'critical'
filename = './logs/log.txt'
filemode = 'a'
encoding = 'utf8'
status = 'Ok'
data = retornar_data_hora_atual('%d/%m/%Y')
hora = retornar_data_hora_atual('%H:%M:%S')
dataHora = data + ' - ' + hora
formating = formatar_log(dataHora, status, messaging, delimitador=';')

logger(
    messaging,
    level,
    filename=None,
    filemode=None,
    encoding=None,
    formating=None,
    handlers=None,
)
"""

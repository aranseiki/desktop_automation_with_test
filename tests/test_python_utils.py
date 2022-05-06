from pytest import mark

from lib.python_utils import (
    abrir_arquivo_texto,
    abrir_arquivo_em_bytes,
    arquivo_existente,
    criar_arquivo_texto,
    criar_pasta,
    excluir_arquivo,
    excluir_pasta,
    formatar_log,
    logger,
    pasta_existente,
    retornar_data_hora_atual,
    ler_variavel_ambiente,
)
from tests.conftest import (
    caminho_pasta_exemplo,
    caminho_pasta_exemplo_2,
    contexto_manipulacao_arquivo_criar,
    contexto_manipulacao_arquivo_excluir,
    contexto_manipulacao_pastas_cheias_criar,
    contexto_manipulacao_pastas_cheias_excluir,
    contexto_manipulacao_pastas_vazias_criar,
    contexto_manipulacao_pastas_vazias_excluir,
)

import sys


@mark.logging
def test_quando_informar_uma_mensagem_e_um_nivel_deve_retornar_os_mesmos_elementos():
    message = 'teste'
    level = 'debug'
    filename = './logs/log.txt'
    filemode = 'a'
    logged = logger(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_um_nivel_e_um_arquivo_deve_retornar_a_mensagem_e_o_nivel():
    message = 'teste'
    level = 'critical'
    filename = './logs/log.txt'
    filemode = 'a'
    logged = logger(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_personalizada_deve_retornar_log_com_mensagem_personalizada():
    messaging = 'teste'
    status = 'Ok'
    data = '%(asctime)s'
    level = 'debug'
    filename = './logs/log.txt'
    filemode = 'a'
    formating = formatar_log(data, status, messaging)
    encoding = 'utf8'
    handlers = None
    logged = logger(messaging, level, filename, filemode, encoding, formating)
    print(logged)
    assert logged == (messaging, level.upper())


@mark.logging
def test_quando_informar_os_parametros_deve_retornar_um_texto_formatado_para_log():
    status = 'Ok'
    messaging = 'teste'
    formating = formatar_log(status, messaging)
    assert formating == '%(levelname)s;Ok;teste'


@mark.pastas
def test_quando_informar_o_nome_da_pasta_ela_deve_ser_criada(
    contexto_manipulacao_pastas_vazias_excluir, caminho_pasta_exemplo
):
    caminho = caminho_pasta_exemplo
    criar_pasta(caminho)
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_da_pasta_vazia_ela_deve_ser_excluida(
    caminho_pasta_exemplo, contexto_manipulacao_pastas_vazias_excluir
):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_da_pasta_cheia_ela_deve_ser_excluida(
    caminho_pasta_exemplo, contexto_manipulacao_pastas_cheias_criar
):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho, vazia=False)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_existente_deve_retornar_true(
    contexto_manipulacao_pastas_vazias_criar, caminho_pasta_exemplo
):
    caminho = caminho_pasta_exemplo
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_nao_existente_deve_retornar_false(
    caminho_pasta_exemplo,
):
    caminho = caminho_pasta_exemplo
    if pasta_existente(caminho) == True:
        excluir_pasta(caminho)
    assert pasta_existente(caminho) == False


@mark.arquivos
def test_quando_informar_um_arquivo_de_texto_txt_deve_retornar_o_conteudo_dele():
    caminho = 'tests/arquivo_test.txt'
    conteudo = abrir_arquivo_texto(caminho)
    assert conteudo == 'arquivo de texto'


@mark.arquivos
def test_quando_informar_um_arquivo_qualquer_deve_retornar_o_conteudo_dele_em_bytes():
    caminho = 'tests/arquivo_test.xlsx'
    conteudo = abrir_arquivo_em_bytes(caminho)
    assert str(type(conteudo)) == "<class 'bytes'>"


@mark.arquivos
def test_quando_informar_um_arquivo_de_texto_txt_nao_existente_deve_criar_o_mesmo_arquivo(caminho_arquivo, contexto_manipulacao_arquivo_excluir):
    caminho = caminho_arquivo
    conteudo = criar_arquivo_texto(caminho)
    assert conteudo == True


@mark.arquivos
def test_quando_informar_um_arquivo_de_texto_txt_que_existente_deve_true(caminho_arquivo, contexto_manipulacao_arquivo_criar):
    caminho = caminho_arquivo
    assert arquivo_existente(caminho) == True


@mark.variavel_ambiente
def test_quando_informar_cabecalho_de_um_bloco_de_variavel_de_ambiente_no_arquivo_deve_retornar_um_dicionario_das_variaveis():
    bloco_teste = ler_variavel_ambiente(
        arquivo_config='tests\config_test.ini', nome_bloco_config='teste'
    )
    assert bloco_teste == {
        'variavel_teste': 'valor_teste',
        'variavel_teste2': 'valor_teste2',
    }


@mark.variavel_ambiente
def test_quando_informar_um_cabecalho_de_um_bloco_e_uma_variavel_de_ambiente_no_arquivo_deve_retornar_o_valor_correspondente():
    bloco_teste = ler_variavel_ambiente(
        arquivo_config='tests\config_test.ini',
        nome_bloco_config='teste',
        nome_variavel='variavel_teste',
    )

    assert bloco_teste == 'valor_teste'


@mark.variavel_ambiente
@mark.xfail(not sys.platform == 'win32', reason='variável de sistema do Windows')
def test_quando_informar_uma_variavel_de_ambiente_de_sistema_no_windows_deve_retornar_o_valor_correspondente():
    bloco_teste = ler_variavel_ambiente(
        nome_variavel='windir', variavel_systema=True
    )

    assert bloco_teste == 'C:\Windows'


@mark.data_hora_atual
def test_ao_informar_um_determinado_parametro_deve_retornar_a_data_atual():
    parametro = '%m/%Y'
    data_teste = retornar_data_hora_atual(parametro)
    assert data_teste == '05/2022'


@mark.data_hora_atual
def test_ao_informar_um_determinado_parametro_deve_retornar_a_hora_atual():
    parametro = '%H'
    data_teste = retornar_data_hora_atual(parametro)
    assert data_teste == '15'

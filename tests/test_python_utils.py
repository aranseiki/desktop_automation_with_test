from pytest import mark
from lib.python_utils import (
    logging_msg, criar_pasta, criar_pasta_v2,
    excluir_pasta, pasta_existente
)
from tests.conftest import (
    contexto_manipulacao_pastas_vazias_criar, caminho_pasta_exemplo,
    contexto_manipulacao_pastas_vazias_excluir, caminho_pasta_exemplo_2,
    contexto_manipulacao_pastas_cheias_criar,
    contexto_manipulacao_pastas_cheias_excluir
)


@mark.logging
def test_quando_informar_uma_mensagem_e_um_nivel_deve_retornar_os_mesmos_elementos():
    message = 'teste'
    level = 'debug'
    filename = '.\\logs\\log.txt'
    filemode = 'a'
    logged = logging_msg(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_um_nivel_e_um_arquivo_deve_retornar_a_mensagem_e_o_nivel():
    message = 'teste'
    level = 'critical'
    filename = '.\\logs\\log.txt'
    filemode = 'a'
    logged = logging_msg(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_personalizada_deve_retornar_log_com_mensagem_personalizada():
    messaging = 'teste'
    level = 'critical'
    filename = '.\\logs\\log.txt'
    filemode = 'a'
    logged = logging_msg(messaging, level, filename, filemode, format='%(levelname)s:%(asctime)s')
    print(logged)
    assert logged == (messaging, level.upper())


@mark.pastas
def test_quando_informar_o_nome_da_pasta_ela_deve_ser_criada(contexto_manipulacao_pastas_vazias_excluir, caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    criar_pasta(caminho)
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_da_pasta_ela_deve_ser_criada_v2(contexto_manipulacao_pastas_vazias_excluir, caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    criar_pasta_v2(caminho)
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_da_pasta_vazia_ela_deve_ser_excluida(caminho_pasta_exemplo, contexto_manipulacao_pastas_vazias_excluir):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_da_pasta_cheia_ela_deve_ser_excluida(caminho_pasta_exemplo, contexto_manipulacao_pastas_cheias_criar):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho, vazia = False)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_existente_deve_retornar_true(contexto_manipulacao_pastas_vazias_criar, caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    assert pasta_existente(caminho) == True

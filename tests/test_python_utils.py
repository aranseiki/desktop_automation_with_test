from lib.python_utils import logging_msg, create_path


def test_quando_informar_uma_mensagem_e_um_nivel_deve_retornar_os_mesmos_elementos():
    message = 'teste'
    level = 'debug'
    filename = '.\\logs\\log.txt'
    filemode = 'a'
    logged = logging_msg(message, level, filename, filemode)
    assert logged == (message, level.upper())


def test_quando_informar_uma_mensagem_um_nivel_e_um_arquivo_deve_retornar_a_mensagem_e_o_nivel():
    message = 'teste'
    level = 'critical'
    filename = '.\\logs\\log.txt'
    filemode = 'a'
    logged = logging_msg(message, level, filename, filemode)
    assert logged == (message, level.upper())


def test_quando_informar_o_nome_da_pasta_ela_deve_ser_criada():
    return create_path('exemplo')

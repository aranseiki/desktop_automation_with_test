from lib.python_utils import logging_msg


def test_quando_informar_uma_mensagem_e_um_nivel_deve_retornar_os_mesmos_elementos():
    message = ''
    level = 'debug'
    logged = logging_msg(message, level, filename=None, filemode=None, encoding=None, format=None, handlers=None)
    assert logged == (message, level.upper())


def test_quando_informar_uma_mensagem_um_nivel_e_um_arquivo_deve_retornar_os_mesmos_elementos_e_gravalos_no_arquivo_informado():
    message = 'teste'
    level = 'debug'
    filename = 'arquivo.txt'
    filemode = 'a'
    logged = logging_msg(message, level, filename, filemode)
    assert logged == (message, level.upper())

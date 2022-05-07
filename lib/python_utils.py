def logger(
    messaging,
    level,
    filename=None,
    filemode=None,
    encoding=None,
    formating=None,
    handlers=None,
):
    # import logging resources
    from logging import (
        CRITICAL,
        DEBUG,
        ERROR,
        INFO,
        WARNING,
        basicConfig,
        critical,
        debug,
        error,
        info,
        warning,
    )

    # define level
    level = level.upper()

    # define basic config
    basicConfig(
        level=level,
        filename=filename,
        filemode=filemode,
        encoding=encoding,
        format=formating,
    )

    # run logging command
    if level == 'DEBUG':
        debug(messaging)
    elif level == 'INFO':
        info(messaging)
    elif level == 'WARNING':
        warning(messaging)
    elif level == 'ERROR':
        error(messaging)
    elif level == 'CRITICAL':
        critical(messaging)
    else:
        return 'Level parameter invalid. Please, Inform this correctly.'

    return (messaging, level)


def criar_pasta(caminho):
    from pathlib import Path

    caminho_interno = Path(caminho)
    caminho_interno.mkdir(parents=True)
    return True


def excluir_pasta(caminho, vazia: bool = True):
    if vazia == True:
        from pathlib import Path

        caminho_interno = Path(caminho)
        if caminho_interno.exists():
            caminho_interno.rmdir()
    elif vazia == False:
        from shutil import rmtree

        rmtree(caminho)
    return True


# falta testar
def excluir_arquivo(caminho):
    from pathlib import Path

    arquivo = Path(caminho)
    if arquivo.exists():
        arquivo.unlink()

    return True


def pasta_existente(caminho):
    from pathlib import Path

    return Path(caminho).exists()


def arquivo_existente(caminho):
    from pathlib import Path

    if Path(caminho).is_file() == True:
        return Path(caminho).exists()


def abrir_arquivo_texto(caminho, encoding='utf8'):
    from pathlib import Path

    arquivo = Path(caminho).read_text(encoding=encoding)
    return arquivo


def abrir_arquivo_em_bytes(caminho):
    from pathlib import Path

    arquivo = Path(caminho).read_bytes()
    return arquivo


def criar_arquivo_texto(caminho, data='', encoding='utf8'):
    from pathlib import Path

    arquivo = Path(caminho).write_text(encoding=encoding, data=data)
    return True


# copiar pasta
# recortar pasta
# copiar arquivo
# recortar arquivo


def ler_variavel_ambiente(
    arquivo_config='config.ini',
    nome_bloco_config='padrao',
    nome_variavel=None,
    variavel_systema: bool = False,
):
    import os
    from configparser import ConfigParser

    if variavel_systema == False:
        config = ConfigParser()
        config.read(arquivo_config)
        if not nome_variavel == None:
            bloco = dict(config[nome_bloco_config])
            return bloco[nome_variavel]
        else:
            return dict(config[nome_bloco_config])
    else:
        return os.environ.get(nome_variavel)


def formatar_log(*args, delimitador=';'):
    lista = list(args)
    lista_montada = ''
    lista.reverse()
    while len(lista) > 0:
        item = lista.pop()
        # breakpoint()
        if len(lista) == 0:
            lista_montada += item
        else:
            lista_montada += item + delimitador
    return '%(levelname)s;' + lista_montada


def retornar_data_hora_atual(parametro):
    import datetime

    return datetime.datetime.now().strftime(parametro)

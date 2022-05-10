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


def excluir_arquivo(caminho):
    from pathlib import Path

    arquivo = Path(caminho)
    if arquivo.exists():
        arquivo.unlink()

    return True


def pasta_existente(caminho):
    from pathlib import Path

    return Path(caminho).exists()


def pasta_esta_vazia(caminho):
    from pathlib import Path
    lista_arquivos_pastas = list(Path(caminho).glob('**/*')) 
    if len(lista_arquivos_pastas) == 0:
        return True
    else:
        return False


def arquivo_existente(caminho):
    from pathlib import Path

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


def coletar_nome_arquivo(caminho):
    from pathlib import Path
    if Path(caminho).exists() == True:
        arquivo = Path(caminho).stem
    return arquivo


def coletar_extensao_arquivo(caminho):
    from pathlib import Path
    if Path(caminho).exists() == True:
        arquivo = Path(caminho).suffix
    return arquivo


def retornar_arquivos_em_pasta(caminho, filtro='**/*'):
    from pathlib import Path

    arquivo = list(Path(caminho).glob(filtro))
    return arquivo


def renomear(caminho, nome_atual, novo_nome):
    from pathlib import Path

    nome_atual = Path(caminho) / nome_atual
    novo_nome = Path(caminho) / novo_nome
    if not novo_nome.exists() == True:
        novo_nome = nome_atual.rename(novo_nome)
    else:
        return False
    return novo_nome


def recortar(caminho_atual, caminho_novo):
    from pathlib import Path

    caminho_atual = Path(caminho_atual)
    caminho_novo = Path(caminho_novo)
    if not caminho_novo.exists() == True:
        caminho_novo = caminho_atual.rename(caminho_novo)
    else:
        return False
    return caminho_novo


def copiar_arquivo(arquivo, caminho_destino):
    from pathlib import Path

    arquivo = Path(arquivo)
    if arquivo.exists() == True:
        arquivo = arquivo.absolute()
    else:
        return False
    caminho_destino = Path(caminho_destino)
    if caminho_destino.exists() == True:
        from shutil import copy2

        caminho_destino = copy2(arquivo, caminho_destino)
        # caminho_destino = copytree(arquivo, caminho_destino) # para pastas
    else:
        return False
    return caminho_destino


def copiar_pasta(pasta, caminho_destino):
    from pathlib import Path

    pasta_var_interna = Path(pasta)
    if pasta_var_interna.exists() == True:
        caminho_destino_var_interna = Path(caminho_destino)
        if caminho_destino_var_interna.exists() == True:
            from shutil import copytree

            caminho_destino = copytree(
                pasta, caminho_destino_var_interna / pasta
            )
        else:
            return False
    else:
        return False

    return caminho_destino


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
        if len(lista) == 0:
            lista_montada += item
        else:
            lista_montada += item + delimitador
    return '%(levelname)s;' + lista_montada


def retornar_data_hora_atual(parametro):
    import datetime

    return datetime.datetime.now().strftime(parametro)

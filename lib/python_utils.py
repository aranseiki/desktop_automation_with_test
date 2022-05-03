def logging_msg(
    messaging, level, filename=None,
    filemode=None, encoding=None, formating='',
    handlers=None
):
    # import logging resources
    from logging import (
        basicConfig, debug, info,
        warning, error, critical,
        DEBUG, INFO, WARNING,
        ERROR, CRITICAL
    )
    
    # define level
    level = level.upper()

    # define basic config
    basicConfig(
        level = level,
        filename = filename,
        filemode = filemode,
        encoding = encoding,
        format = formating
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
    caminho_interno.mkdir(parents = True)
    return True


def criar_pasta_v2(caminho):
    from pathlib import Path
    for caminho_iteravel in list(Path(caminho).absolute().parents):
        if not caminho_iteravel.exists():
            caminho_iteravel.mkdir()
    Path(caminho).mkdir()
    return True


def excluir_pasta(caminho, vazia : bool = True):
    if vazia == True:
        from pathlib import Path
        caminho_interno = Path(caminho)
        if caminho_interno.exists():
            caminho_interno.rmdir()
    elif vazia == False:
        from shutil import rmtree
        rmtree(caminho)
    return True


def pasta_existente(caminho):
    from pathlib import Path
    return Path(caminho).exists()


def variavel_ambiente(nome_variavel):
    import os
    return os.environ.get(nome_variavel)

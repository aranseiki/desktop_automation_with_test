from pytest import fixture

from lib.application_utils import (
    aplicacao,
    capturar_texto,
    clicar,
    coletar_dado_selecionado,
    coletar_dados_selecao,
    coletar_situacao_janela,
    digitar,
    encerrar_app,
    esta_visivel,
    fechar_janela,
    iniciar_app,
    localiza_elemento,
    maximizar_janela,
    minimizar_janela,
    restaurar_janela,
    selecionar_em_campo_selecao,
    selecionar_menu,
)
from lib.python_utils import (
    arquivo_existente,
    criar_arquivo_texto,
    criar_pasta,
    excluir_arquivo,
    excluir_pasta,
)


@fixture
def aplicacao_test():
    return aplicacao()


@fixture
def executavel_mouseclicker():
    executavel_path = 'tests/mouseclicker.exe'
    return executavel_path


@fixture
def executavel_notepad():
    executavel_path = 'notepad'
    return executavel_path


@fixture
def caminho_campo():
    caminho_campo = 'Free Mouse Clicker->Start'
    return caminho_campo


@fixture
def valor():
    valor = 5
    return valor


@fixture
def iniciar_app_test(executavel_mouseclicker):
    return iniciar_app(executavel_mouseclicker)


@fixture
def encerrar_app_test(executavel_mouseclicker):
    encerrar_app(executavel_mouseclicker)
    return True


@fixture
def contexto_mouseclicker(executavel_mouseclicker):
    app = iniciar_app(executavel_mouseclicker)
    yield app
    encerrar_app(executavel_mouseclicker)
    return app


@fixture
def contexto_notepad(executavel_notepad):
    app = iniciar_app(executavel_notepad)
    yield app
    encerrar_app(executavel_notepad)
    return app


@fixture
def digitar_test(caminho_campo, valor):
    return digitar(caminho_campo, valor)


@fixture
def localiza_elemento_estaticoo_test(caminho_campo):
    return localiza_elemento(caminho_campo, estatico=True)


@fixture
def localiza_elemento_dinamico_test(caminho_campo):
    return localiza_elemento(caminho_campo, estatico=False)


@fixture
def capturar_texto_test(caminho_campo):
    capturar_texto(caminho_campo)


@fixture
def clicar_test(caminho_campo):
    return clicar(caminho_campo)


@fixture
def esta_visivel_test():
    nome_janela = 'Free Mouse Clicker'
    return esta_visivel(nome_janela)


@fixture
def coletar_situacao_janela_normal_test():
    nome_janela = 'Free Mouse Clicker'
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_minimizada_test():
    nome_janela = 'Free Mouse Clicker'
    minimizar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_maximizada_test():
    nome_janela = 'Free Mouse Clicker'
    maximizar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def coletar_situacao_janela_restaurada_test():
    nome_janela = 'Free Mouse Clicker'
    maximizar_janela(nome_janela)
    restaurar_janela(nome_janela)
    return coletar_situacao_janela(nome_janela)


@fixture
def minimizar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return minimizar_janela(nome_janela)


@fixture
def maximizar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return maximizar_janela(nome_janela)


@fixture
def restaurar_janela_test():
    nome_janela = 'Free Mouse Clicker'
    return restaurar_janela(nome_janela)


@fixture
def coletar_dados_selecao_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    return coletar_dados_selecao(caminho_campo)


@fixture
def coletar_dado_selecionado_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    return coletar_dado_selecionado(caminho_campo)


@fixture
def selecionar_em_campo_selecao_test():
    caminho_campo = 'Free Mouse Clicker->combobox'
    item = 'Single Click'
    return selecionar_em_campo_selecao(caminho_campo, item)


@fixture
def selecionar_menu_test():
    nome_janela = 'Sem título - Bloco de Notas'
    caminho_menu = '&Arquivo->Abrir'
    return selecionar_menu(nome_janela, caminho_menu)


@fixture
def fechar_janela_test():
    nome_janela = 'Sem título - Bloco de Notas'
    return fechar_janela(nome_janela)


@fixture
def caminho_pasta_exemplo():
    caminho = 'exemplo'
    return caminho


@fixture
def caminho_pasta_exemplo_2():
    caminho = 'exemplo/exemplo2'
    return caminho


@fixture
def contexto_manipulacao_pastas_vazias_excluir(caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    yield excluir_pasta(caminho)


@fixture
def contexto_manipulacao_pastas_vazias_criar(caminho_pasta_exemplo):
    caminho = caminho_pasta_exemplo
    yield criar_pasta(caminho)


@fixture
def contexto_manipulacao_pastas_cheias_criar(caminho_pasta_exemplo_2):
    caminho = caminho_pasta_exemplo_2
    yield criar_pasta(caminho)


@fixture
def contexto_manipulacao_pastas_cheias_excluir(caminho_pasta_exemplo_2):
    caminho = caminho_pasta_exemplo_2
    yield excluir_pasta(caminho, vazia=False)


@fixture
def caminho_arquivo():
    caminho = 'tests/novo_arquivo_test.txt'
    return caminho


@fixture
def excluir_arquivo_test(caminho_arquivo):
    excluir_arquivo(caminho_arquivo)


@fixture
def contexto_manipulacao_arquivo_excluir(caminho_arquivo):
    caminho = caminho_arquivo
    if arquivo_existente == True:
        excluir_arquivo(caminho)
    yield
    excluir_arquivo(caminho)


@fixture
def contexto_manipulacao_arquivo_criar(caminho_arquivo):
    caminho = caminho_arquivo
    if not arquivo_existente == True:
        criar_arquivo_texto(caminho)
    yield
    excluir_arquivo(caminho)

from lib.application_utils import (
    aplicacao, iniciar_app, encerrar_app,
    digitar, localiza_elemento, capturar_texto,
    clicar, esta_visivel, coletar_situacao_janela,
    minimizar_janela, maximizar_janela, restaurar_janela,
    coletar_dados_selecao, coletar_dado_selecionado,
    selecionar_em_campo_selecao, selecionar_menu, fechar_janela
)
from lib.python_utils import excluir_pasta, criar_pasta
from pytest import fixture


@fixture
def aplicacao_test():
    return aplicacao()


@fixture
def executavel():
    executavel_path = U'C:\\Users\\aoalmeida2\\Documents\\'\
        + 'desktop_automation_with_test\\mouseclicker.exe'
    return executavel_path


@fixture
def executavel_mouseclicker():
    executavel_path = U'C:\\Users\\aoalmeida2\\Documents\\'\
        + 'desktop_automation_with_test\\mouseclicker.exe'
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
def iniciar_app_test(executavel):
    return iniciar_app(executavel)


@fixture
def encerrar_app_test(executavel):
    encerrar_app(executavel)
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
    caminho_menu = "&Arquivo->Abrir"
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

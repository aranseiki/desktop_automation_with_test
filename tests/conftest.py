from application_library import aplicacao, iniciar_app, encerrar_app, digitar, localiza_elemento, capturar_texto, clicar, esta_visivel
from pytest import fixture


@fixture
def aplicacao_test():
    return aplicacao()

@fixture
def executavel():
    executavel_path = U'C:\\Users\\aoalmeida2\\Documents\\desktop_automation_with_test\\mouseclicker.exe'
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
def contexto(executavel):
    app = iniciar_app(executavel)
    yield app
    encerrar_app(executavel)
    return app

@fixture
def digitar_test(caminho_campo, valor):
    return digitar(caminho_campo, valor)

@fixture
def localiza_elemento_estatico_test(caminho_campo):
    return localiza_elemento(caminho_campo, static=True)

@fixture
def localiza_elemento_dinamico_test(caminho_campo):
    return localiza_elemento(caminho_campo, static=False)

@fixture
def capturar_texto_test(caminho_campo):
    capturar_texto(caminho_campo)

@fixture
def clicar_test(caminho_campo):
    return clicar(caminho_campo)

@fixture
def esta_visivel_test():
    return esta_visivel()

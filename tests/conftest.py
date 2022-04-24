from application_library import aplicacao, iniciar_app, encerrar_app, digitar, localiza_elemento, capturar_texto, clicar
from pytest import fixture


@fixture
def aplicacao_test():
    return aplicacao()

@fixture
def executavel():
    executavel_path = U'D:\\OneDrive - 5t2tj5\\Documents\\Computacao e tecnologia\\Development\\desktop_automation_with_test\\mouseclicker.exe'
    return executavel_path 

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
def digitar_test():
    valor = 5
    caminho_campo = 'Free Mouse Clicker->Minutes'
    return digitar(caminho_campo, valor)

@fixture
def localiza_elemento_test():
    caminho_campo = 'Free Mouse Clicker->Minutes'
    return localiza_elemento(caminho_campo)

@fixture
def capturar_texto_test():
    caminho_campo = 'Free Mouse Clicker->Minutes'
    capturar_texto(caminho_campo)

@fixture
def clicar_test():
    caminho_campo = 'Free Mouse Clicker->Minutes'
    return clicar(caminho_campo)

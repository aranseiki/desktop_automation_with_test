from application_library import iniciar_app, encerrar_app, click_interval_minutes
from pytest import fixture


@fixture
def executavel():
    executavel_path = U'C:\\Users\\aoalmeida2\\Documents\\desktop_automation_with_test\\mouseclicker.exe'
    return executavel_path 

@fixture
def iniciar_app_test(executavel):
    return iniciar_app(executavel)

@fixture
def encerrar_app_test(executavel):
    return encerrar_app(executavel)

@fixture
def contexto(executavel):
    app = iniciar_app(executavel)
    yield app
    encerrar_app(executavel)
    return app

@fixture
def click_interval_minutes_test():
    numero = 5
    caminho_campo = 'FreeMouseClicker.Minutes'
    return click_interval_minutes(caminho_campo, numero)

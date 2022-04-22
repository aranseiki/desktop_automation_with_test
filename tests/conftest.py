from application_library import iniciar_app, encerrar_app
from pytest import fixture


@fixture
def executavel():
    executavel_path = U'D:\\OneDrive - 5t2tj5\\Programs\\Infraestructure\\System Access Control\\mouseclicker.exe'
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

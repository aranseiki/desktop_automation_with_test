from time import sleep
from pywinauto import Application, application
from tests.conftest import executavel as executavel, contexto as contexto
# from application_library import click_interval_minutes_test

def test_quando_a_aplicacao_iniciar_deve_retornar_um_objeto_tipo_application(contexto):
    app_esperado = type(Application())
    app = contexto
    app_test = type(app)
    assert app_test == app_esperado

def test_quando_a_aplicacao_iniciar_o_caminho_do_objeto_application_deve_ser_igual_ao_informado(executavel, contexto):
    caminho = executavel
    app = contexto
    assert application.process_module(app.process) == caminho

def test_quando_o_campo_minutes_receber_um_valor_o_mesmo_campo_deve_guardar_o_valor_informado(contexto, click_interval_minutes_test):
    valor = 5
    campo_minutes = click_interval_minutes_test
    assert campo_minutes == valor

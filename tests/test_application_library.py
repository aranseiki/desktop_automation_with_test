from pywinauto import Application, application
from tests.conftest import aplicacao_test, executavel, contexto, localiza_elemento, clicar_test


def test_quando_o_objeto_application_for_iniciado_o_mesmo_deve_retornar_um_objeto_tipo_application(aplicacao_test):
    app_esperado = type(Application())
    app = aplicacao_test
    app_test = type(app)
    assert app_test == app_esperado

def test_quando_a_aplicacao_iniciar_deve_retornar_um_objeto_tipo_application(contexto):
    app_esperado = type(Application())
    app = contexto
    app_test = type(app)
    assert app_test == app_esperado

def test_quando_a_aplicacao_iniciar_o_caminho_do_objeto_application_deve_ser_igual_ao_informado(executavel, contexto):
    caminho = executavel
    app = contexto
    assert application.process_module(app.process) == caminho

def test_quando_a_aplicacao_encerrar_deve_finalizar_o_processo(iniciar_app_test, encerrar_app_test):
    app_iniciado = iniciar_app_test
    app_encerrado = encerrar_app_test
    assert app_encerrado == True

def test_quando_procurar_por_um_elemento_deve_retornar_um_elemento_estatico(contexto, localiza_elemento_test):
    elemento_localizado = localiza_elemento_test
    elemento_localizado_test = str(elemento_localizado.wrapper_object()).__contains__('Static')
    assert elemento_localizado_test == True

def test_quando_o_campo_minutes_receber_um_valor_o_mesmo_campo_deve_retornar_o_valor_informado(contexto, digitar_test):
    valor = 5
    campo_minutes = digitar_test
    assert campo_minutes == valor

def test_quando_clicar_em_um_botao_deve_retornar_verdadeiro(contexto, clicar_test):
    retorno_clique = clicar_test
    assert retorno_clique == True

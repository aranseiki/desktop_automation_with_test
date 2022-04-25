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

def test_quando_procurar_por_um_elemento_deve_retornar_um_elemento_estatico(caminho_campo, contexto, localiza_elemento_estatico_test):
    elemento_localizado = localiza_elemento_estatico_test
    caminho = caminho_campo
    campo = caminho.split('->')
    ultimo_campo = campo[-1]
    ultimo_campo = ultimo_campo.split()
    if ultimo_campo == elemento_localizado.texts():
        elemento_localizado_test = True
    assert elemento_localizado_test == True

def test_quando_procurar_por_um_elemento_deve_retornar_um_elemento_dinamico(caminho_campo, contexto, localiza_elemento_dinamico_test):
    elemento_localizado = localiza_elemento_dinamico_test
    caminho = caminho_campo
    campo = caminho.split('->')
    ultimo_campo = campo[-1]
    ultimo_campo = ultimo_campo.split()
    if ultimo_campo != elemento_localizado.texts():
        elemento_localizado_test = True
    assert elemento_localizado_test == True

def test_quando_o_campo_minutes_receber_um_valor_o_mesmo_campo_deve_retornar_o_valor_informado(contexto, digitar_test):
    valor = 5
    campo_minutes = digitar_test
    assert campo_minutes == valor

def test_quando_clicar_em_um_botao_deve_retornar_verdadeiro(contexto, clicar_test):
    retorno_clique = clicar_test
    assert retorno_clique == True

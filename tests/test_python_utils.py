import sys

from pytest import mark

from lib.python_utils import (
    abrir_arquivo_em_bytes,
    abrir_arquivo_texto,
    arquivo_existente,
    coletar_extensao_arquivo,
    coletar_nome_arquivo,
    copiar_arquivo,
    copiar_pasta,
    criar_arquivo_texto,
    criar_pasta,
    excluir_arquivo,
    excluir_pasta,
    formatar_log,
    ler_variavel_ambiente,
    logger,
    pasta_esta_vazia,
    pasta_existente,
    recortar,
    renomear,
    retornar_arquivos_em_pasta,
    retornar_data_hora_atual,
)
from tests.conftest import (
    arquivo_exemplo,
    arquivo_exemplo_2,
    caminho_pasta_exemplo,
    caminho_pasta_exemplo_2,
    caminho_raiz,
    contexto_manipulacao_arquivo_criar,
    contexto_manipulacao_arquivo_excluir,
    contexto_manipulacao_pastas_cheias_criar,
    contexto_manipulacao_pastas_cheias_excluir,
    contexto_manipulacao_pastas_vazias_criar,
    contexto_manipulacao_pastas_vazias_excluir,
)


@mark.logging
def test_quando_informar_uma_mensagem_e_um_nivel_deve_retornar_os_mesmos_elementos():
    message = 'teste'
    level = 'debug'
    filename = './logs/log.txt'
    filemode = 'a'
    logged = logger(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_um_nivel_e_um_arquivo_deve_retornar_a_mensagem_e_o_nivel():
    message = 'teste'
    level = 'critical'
    filename = './logs/log.txt'
    filemode = 'a'
    logged = logger(message, level, filename, filemode)
    assert logged == (message, level.upper())


@mark.logging
def test_quando_informar_uma_mensagem_personalizada_deve_retornar_log_com_mensagem_personalizada():
    messaging = 'teste'
    status = 'Ok'
    data = '%(asctime)s'
    level = 'debug'
    filename = './logs/log.txt'
    filemode = 'a'
    formating = formatar_log(data, status, messaging)
    encoding = 'utf8'
    handlers = None
    logged = logger(messaging, level, filename, filemode, encoding, formating)
    print(logged)
    assert logged == (messaging, level.upper())


@mark.logging
def test_quando_informar_os_parametros_deve_retornar_um_texto_formatado_para_log():
    status = 'Ok'
    messaging = 'teste'
    formating = formatar_log(status, messaging)
    assert formating == '%(levelname)s;Ok;teste'


@mark.pastas
def test_quando_informar_o_nome_da_pasta_ela_deve_ser_criada(
    contexto_manipulacao_pastas_vazias_excluir, caminho_pasta_exemplo
):
    caminho = caminho_pasta_exemplo
    criar_pasta(caminho)
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_da_pasta_vazia_ela_deve_ser_excluida(
    caminho_pasta_exemplo, contexto_manipulacao_pastas_vazias_excluir
):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_da_pasta_cheia_ela_deve_ser_excluida(
    caminho_pasta_exemplo, contexto_manipulacao_pastas_cheias_criar
):
    caminho = caminho_pasta_exemplo
    excluir_pasta(caminho, vazia=False)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_existente_deve_retornar_true(
    contexto_manipulacao_pastas_vazias_criar, caminho_pasta_exemplo
):
    caminho = caminho_pasta_exemplo
    assert pasta_existente(caminho) == True


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_nao_existente_deve_retornar_false(
    caminho_pasta_exemplo,
):
    caminho = caminho_pasta_exemplo
    if pasta_existente(caminho) == True:
        excluir_pasta(caminho)
    assert pasta_existente(caminho) == False


@mark.pastas
def test_quando_informar_uma_pasta_existente_deve_renomear_para_o_novo_nome_informado(
    caminho_raiz,
    caminho_pasta_exemplo_3,
    caminho_pasta_exemplo_4,
    contexto_manipulacao_pastas_renomear,
):
    from pathlib import Path

    caminho_raiz = caminho_raiz
    nome_atual = caminho_pasta_exemplo_3
    nome_novo = caminho_pasta_exemplo_4
    pasta_renomeada = renomear(caminho_raiz, nome_atual, nome_novo)
    assert pasta_renomeada == Path(caminho_raiz + nome_novo)


@mark.pastas
def test_quando_informar_uma_pasta_existente_deve_recortar_e_colar_no_caminho_informado(
    caminho_pasta_exemplo_4,
    caminho_pasta_exemplo_5,
    contexto_manipulacao_pastas_recortar,
):
    from pathlib import Path

    caminho_atual = caminho_pasta_exemplo_4
    caminho_novo = caminho_pasta_exemplo_5
    arquivo_recortado = recortar(caminho_atual, caminho_novo)
    assert arquivo_recortado == Path(caminho_novo)


@mark.pastas
def test_quando_informar_uma_pasta_existente_deve_copiar_e_colar_no_caminho_informado(
    caminho_arquivo,
    caminho_pasta_exemplo,
    caminho_pasta_exemplo_3,
    contexto_manipulacao_pasta_copiar,
):
    from pathlib import Path

    pasta = caminho_pasta_exemplo
    caminho_destino = caminho_pasta_exemplo_3
    arquivo_copiado = copiar_pasta(pasta, caminho_destino)
    assert arquivo_copiado == Path(caminho_destino) / pasta


@mark.pastas
def test_quando_informar_uma_pasta_existente_deve_retornar_os_arquivos_dentro_desta_pasta(
    caminho_pasta_exemplo,
    arquivo_exemplo_2,
    contexto_manipulacao_pasta_mostar_arquivos,
):
    from pathlib import Path

    caminho = caminho_pasta_exemplo
    primeiro_arquivo = arquivo_exemplo_2
    # filtro = caminho_pasta_exemplo_3
    arquivo_copiado = retornar_arquivos_em_pasta(caminho)
    assert arquivo_copiado[0] == Path(caminho_pasta_exemplo) / primeiro_arquivo


@mark.pastas
def test_quando_informar_uma_pasta_existente_e_um_filtro_de_pesquisa_deve_retornar_os_arquivos_dentro_desta_pasta_correspondentes_ao_filtro(
    caminho_pasta_exemplo,
    arquivo_exemplo_2,
    contexto_manipulacao_pasta_mostar_arquivos,
):
    from pathlib import Path

    caminho = caminho_pasta_exemplo
    primeiro_arquivo = arquivo_exemplo_2
    # filtro = caminho_pasta_exemplo_3
    arquivo_copiado = retornar_arquivos_em_pasta(caminho, filtro='*renomeado*')
    assert arquivo_copiado[0] == Path(caminho_pasta_exemplo) / primeiro_arquivo


@mark.pastas
def test_quando_informar_o_nome_de_uma_pasta_vazia_deve_retornar_true(
    contexto_manipulacao_pastas_vazias_criar, caminho_pasta_exemplo
):
    caminho = caminho_pasta_exemplo
    assert pasta_esta_vazia(caminho) == True


@mark.arquivos
def test_quando_informar_um_arquivo_de_texto_txt_deve_retornar_o_conteudo_dele():
    caminho = 'tests/arquivo_test.txt'
    conteudo = abrir_arquivo_texto(caminho)
    assert conteudo == 'arquivo de texto'


@mark.arquivos
def test_quando_informar_um_arquivo_qualquer_deve_retornar_o_conteudo_dele_em_bytes():
    caminho = 'tests/arquivo_test.xlsx'
    conteudo = abrir_arquivo_em_bytes(caminho)
    assert str(type(conteudo)) == "<class 'bytes'>"


@mark.arquivos
def test_quando_informar_um_arquivo_de_texto_txt_nao_existente_deve_criar_o_mesmo_arquivo(
    caminho_arquivo, contexto_manipulacao_arquivo_excluir
):
    caminho = caminho_arquivo
    conteudo = criar_arquivo_texto(caminho)
    assert conteudo == True


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_true(
    caminho_arquivo, contexto_manipulacao_arquivo_criar
):
    caminho = caminho_arquivo
    assert arquivo_existente(caminho) == True


@mark.arquivos
def test_quando_informar_um_arquivo_existente_o_mesmo_arquivo_deve_ser_excluido(
    caminho_arquivo, contexto_manipulacao_arquivo_criar
):
    caminho = caminho_arquivo
    excluir_arquivo(caminho)
    assert arquivo_existente(caminho) == False


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_retornar_o_nome_dele(
    caminho_arquivo, contexto_manipulacao_arquivo_criar
):
    caminho = caminho_arquivo
    nome_arquivo = coletar_nome_arquivo(caminho)
    assert nome_arquivo == 'novo_arquivo_test'


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_retornar_a_extensao_dele(
    caminho_arquivo, contexto_manipulacao_arquivo_criar
):
    caminho = caminho_arquivo
    extensao_arquivo = coletar_extensao_arquivo(caminho)
    assert extensao_arquivo == '.txt'


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_renomear_para_o_novo_nome_informado(
    caminho_raiz,
    arquivo_exemplo,
    arquivo_exemplo_2,
    contexto_manipulacao_arquivo_criar_2,
):
    from pathlib import Path

    caminho = caminho_raiz
    nome_arquivo = arquivo_exemplo
    novo_nome = arquivo_exemplo_2
    arquivo_renomeado = renomear(caminho, nome_arquivo, novo_nome)
    assert arquivo_renomeado == Path(caminho_raiz + novo_nome)


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_recortar_e_colar_no_caminho_informado(
    caminho_arquivo, caminho_arquivo_2, contexto_manipulacao_arquivo_criar_3
):
    from pathlib import Path

    caminho_atual = caminho_arquivo
    caminho_novo = caminho_arquivo_2
    arquivo_recortado = recortar(caminho_atual, caminho_novo)
    assert arquivo_recortado == Path(caminho_novo)


@mark.arquivos
def test_quando_informar_um_arquivo_existente_deve_copiar_e_colar_no_caminho_informado(
    caminho_arquivo, caminho_pasta_exemplo, contexto_manipulacao_arquivo_copiar
):
    from pathlib import Path

    arquivo = caminho_arquivo
    caminho_destino = caminho_pasta_exemplo
    arquivo_copiado = copiar_arquivo(arquivo, caminho_destino)
    assert Path(arquivo_copiado) == Path(caminho_destino) / arquivo


@mark.variavel_ambiente
def test_quando_informar_cabecalho_de_um_bloco_de_variavel_de_ambiente_no_arquivo_deve_retornar_um_dicionario_das_variaveis():
    bloco_teste = ler_variavel_ambiente(
        arquivo_config='tests/config_test.ini', nome_bloco_config='teste'
    )
    assert bloco_teste == {
        'variavel_teste': 'valor_teste',
        'variavel_teste2': 'valor_teste2',
    }


@mark.variavel_ambiente
def test_quando_informar_um_cabecalho_de_um_bloco_e_uma_variavel_de_ambiente_no_arquivo_deve_retornar_o_valor_correspondente():
    bloco_teste = ler_variavel_ambiente(
        arquivo_config='tests/config_test.ini',
        nome_bloco_config='teste',
        nome_variavel='variavel_teste',
    )

    assert bloco_teste == 'valor_teste'


@mark.variavel_ambiente
@mark.xfail(
    not sys.platform == 'win32', reason='variável de sistema do Windows'
)
def test_quando_informar_uma_variavel_de_ambiente_de_sistema_no_windows_deve_retornar_o_valor_correspondente():
    bloco_teste = ler_variavel_ambiente(
        nome_variavel='windir', variavel_systema=True
    )

    assert bloco_teste.upper() == 'C:\WINDOWS'


@mark.data_hora_atual
def test_ao_informar_um_determinado_parametro_deve_retornar_a_data_atual():
    parametro = '%m/%Y'
    data_teste = retornar_data_hora_atual(parametro)
    assert data_teste == '05/2022'


@mark.data_hora_atual
def test_ao_informar_um_determinado_parametro_deve_retornar_a_hora_atual():
    parametro = '%H'
    hora_teste = retornar_data_hora_atual(parametro)
    assert hora_teste == '11'

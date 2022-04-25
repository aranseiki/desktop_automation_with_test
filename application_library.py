from pywinauto import Application


def aplicacao():
    # define app como global
    global APP

    # instancia o objeto application
    APP = Application()

    # retorna o objeto application instanciado
    return APP

def iniciar_app(executavel):
    
    # instancia o objeto application
    APP = aplicacao()

    # inicia o processo de execução do aplicativo passado como parâmetro
    APP.start(executavel)

    # retorna o objeto application instanciado com o processo iniciado
    return APP

def encerrar_app(executavel):
    # importa app para o escopo da função
    global APP

    # encerra o aplicativo em execução
    APP.kill(executavel)

    # retorna o objeto application com o processo encerrado
    return APP

def localiza_elemento(caminho_campo, static=True):
    # importa app para o escopo da função
    global APP
    app_interno = APP

    # trata o caminho da árvore de parantesco do app
    campo = caminho_campo.split('->')
    index = 0

    # localiza o elemento até o final da árvore de parantesco do app: 
    while index < len(campo):
        
        # Se index for igual ao primeiro elemento
        if index == 0:
            app_interno = app_interno.window(title=campo[0])
        
        # Se index for igual ao último elemento
        elif (index == (len(campo) - 1)) and (static == False):
            
            # coleta o elemento informado e concatena 'Edit' no final
            app_interno = app_interno[campo[index] + 'Edit']

        # Se o index não for igual ao primeiro elemento nem o index for igual ao último elemento
        else:

            # coleta o elemento informado e concatena 'Edit' no final
            app_interno = app_interno[campo[index]]

        # lógica para a condicional    
        index = index + 1

    # retorna o elemento encontrado
    return app_interno

def digitar(caminho_campo, valor):
    # Define liberação para digitar
    static=False

    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = localiza_elemento(caminho_campo, static)
    
    # digita o valor no campo localizado
    app_interno.type_keys(valor)

    # trata o valor capturado conforme o tipo do valor de entrada
    valor_retornado = type(valor)(capturar_texto(caminho_campo, static))
    
    # retorna o valor capturado e tratado
    return valor_retornado

def capturar_texto(caminho_campo, static=True):
    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = localiza_elemento(caminho_campo, static)
        
    #captura o texto do campo localizado
    valor_capturado = app_interno.texts()[0]
    
    # retorna o valor capturado
    return valor_capturado

def clicar(caminho_campo):
    # localiza o elemento até o final da árvore de parantesco do app
    app_interno = localiza_elemento(caminho_campo)

    # digita o valor no campo localizado
    app_interno.click()
    
    # retorna o valor capturado e tratado
    return True

def coletar_situacao_janela(nome_janela):
    
    # importa app para o escopo da função
    global APP
    app_interno = APP

    # coleta a situacao atual da janela
    situacao = app_interno[nome_janela].get_show_state()
    
    breakpoint()

    # 1 - Normal
    if situacao == 1:
        situacao = 'normal'
    # 2 - Minimizado
    elif situacao == 2:
        situacao = 'minimizado'
    # 3 - Maximizado
    elif situacao == 3:
        situacao = 'maximizado'
    # Caso não encontre as situações normal, ninimizado e maximizado
    else:
        # define um valor padrão
        situacao = 'não identificado'

    # retorna a situação da janela
    return situacao
    
def esta_visivel(nome_janela):
    
    # coleta a situação atual da janela
    situacao = coletar_situacao_janela(nome_janela)
    
    # define visível para situação 'maximizado' ou 'normal'
    if situacao == 'maximizado' or situacao == 'normal':
        situacao = 'visivel'
    # define não visível para situação 'minimizado'
    elif situacao == 'minimizado':
        situacao = 'não visível'
    # Caso não encontre as situações normal, ninimizado e maximizado
    else:
        # define um valor padrão
        situacao = 'não identificado'
    
    # retorna a situação da janela
    return situacao

def esta_com_foco(nome_janela):
    
    # importa app para o escopo da função
    global APP
    app_interno = APP

    # coleta a situacao atual de foco da janela
    foco = app_interno[nome_janela].has_focus()

    # retorna a situação coletada
    return foco

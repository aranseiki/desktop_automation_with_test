from pywinauto import Application


def aplicacao():
    global app
    app = Application()
    return app

def iniciar_app(executavel):
    app = aplicacao()
    app.start(executavel)
    return app

def encerrar_app(executavel):
    app.kill(executavel)
    return app

def localiza_elemento(caminho_campo, static=True):
    # importa app para o escopo da função
    global app
    app_interno = app

    #trata o caminho da árvore de parantesco do app
    campo = caminho_campo.split('->')
    index = 0

    # localiza o elemento até o final da árvore de parantesco do app
    while index < len(campo):
        if index == 0:
            app_interno = app_interno.window(title=campo[0])
        elif (index == (len(campo) - 1)) and (static == False):
            app_interno = app_interno[campo[index] + 'Edit']
        else:
            app_interno = app_interno[campo[index]]
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

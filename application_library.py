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

def click_interval_minutes(caminho_campo, numero):
    campo = caminho_campo.split('.')
    index = 0
    conjunto = set()
    while index < len(campo):
        conjunto.add(campo[index])
        index = index + 1
    breakpoint()
    app['FreeMouseClicker']['Minutes:Edit'].type_keys(numero)
    return numero

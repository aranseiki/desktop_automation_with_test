from pywinauto import Application


app = Application()

def iniciar_app(executavel):
    global app
    app = Application().start(executavel)
    return app

def encerrar_app(executavel):
    global app
    app = app.kill(executavel)
    return app

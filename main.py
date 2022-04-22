from time import sleep
from application_library import iniciar_app, encerrar_app


executavel = U'D:\\OneDrive - 5t2tj5\\Programs\\Infraestructure\\System Access Control\\mouseclicker.exe'

app = iniciar_app(executavel)

sleep(3)

encerrar_app(executavel)
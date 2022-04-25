from time import sleep
from application_library import iniciar_app, encerrar_app, digitar, clicar

executavel = U'C:\\Users\\aoalmeida2\\Documents\\desktop_automation_with_test\\mouseclicker.exe'

app = iniciar_app(executavel)

valor = 10
caminho_campo = 'Free Mouse Clicker->Minutes'
digitar(caminho_campo, valor)

sleep(3)
caminho_campo = 'Free Mouse Clicker->Start'
clicar(caminho_campo)

sleep(3)
caminho_campo = 'Free Mouse Clicker->Stop'
clicar(caminho_campo)

sleep(3)
encerrar_app(executavel)

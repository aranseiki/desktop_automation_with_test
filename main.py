from time import sleep
from application_library import iniciar_app, encerrar_app, click_interval_minutes


executavel = U'C:\\Users\\aoalmeida2\\Documents\\desktop_automation_with_test\\mouseclicker.exe'

app = iniciar_app(executavel)

numero = 10
click_interval_minutes(numero)

sleep(3)

encerrar_app(executavel)

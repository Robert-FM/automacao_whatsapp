import webbrowser
import time
import pyautogui as pg

# Lista de números
numeros = [
    "5581997835416",
    "558183620749",
    "558187064167"
]

# Configura pausa entre os comandos do PyAutoGUI
pg.PAUSE = 1

for numero in numeros:
    link = f"https://web.whatsapp.com/send?phone={numero}"
    webbrowser.open(link)
    time.sleep(10)  # Aguardar tempo suficiente para carregar o WhatsApp Web

    # CLICKS - ajustados para sua interface
    pg.click(x=657, y=983)
    time.sleep(2)
    pg.click(x=639, y=683)
    time.sleep(2)
    pg.click(x=218, y=192)
    time.sleep(2)
    pg.click(x=753, y=611)
    time.sleep(2)
    pg.click(x=1866, y=966)
    time.sleep(2)
    pg.click(x=785, y=992)
    time.sleep(2)
    pg.click(x=839, y=999)

    # Escrita da mensagem
    pg.write("Apenas testando um negócio!")
    time.sleep(2)

    # Enviar (pressiona botão de envio)
    pg.click(x=1877, y=985)

    # Espera antes de passar para o próximo número
    time.sleep(4)

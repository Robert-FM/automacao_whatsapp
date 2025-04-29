# project_zap

Abrir o WhatsApp Web no Chrome

Escanear o QR Code (só na primeira vez)

Iterar sobre uma lista de números

Abrir o link https://wa.me/<numero> e enviar a mensagem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Lista de números com DDI + DDD + número (sem espaços ou sinais)
numeros = [
    "5581999999999", 
    "5581988888888"
]

mensagem = "Olá! Esta é uma mensagem automática enviada via WhatsApp Web com Selenium."

# Configurar o navegador (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=./profile")  # Mantém login após o primeiro QR code
driver = webdriver.Chrome(options=options)

# Função para enviar mensagem
def enviar_mensagem(numero):
    link = f"https://wa.me/{numero}"
    driver.get(link)
    time.sleep(3)
    
    try:
        # Clicar no botão para abrir o chat
        botao_abrir = driver.find_element(By.XPATH, '//a[contains(@href,"web.whatsapp.com/send")]')
        botao_abrir.click()
        time.sleep(5)

        # Enviar mensagem
        caixa_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        caixa_mensagem.click()
        caixa_mensagem.send_keys(mensagem)
        caixa_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)

        print(f"Mensagem enviada para: {numero}")
    except Exception as e:
        print(f"Erro com {numero}: {e}")

# Iterar sobre os números
for numero in numeros:
    enviar_mensagem(numero)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Lista de números para envio
numeros = [
    "5581997835416"
]

mensagem = "Olá! Esta é uma mensagem com imagem automática via WhatsApp Web."
caminho_imagem = os.path.abspath("imagem.jpg")  # Verifique se o arquivo existe

# Configuração do Chrome com perfil de usuário (mantém login no WhatsApp Web)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/Robert Fernandes/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options)

def esperar_elemento(by, valor, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, valor)))

def enviar_mensagem(numero):
    try:
        link = f"https://web.whatsapp.com/send?phone={numero}&text&app_absent=0"
        print(f"[INFO] Abrindo link: {link}")
        driver.get(link)

        print("[INFO] Aguardando botão de clipe...")
        esperar_elemento(By.XPATH, "//div[@title='Anexar']", timeout=30)
        time.sleep(2)

        print("[INFO] Clicando no botão de clipe")
        driver.find_element(By.XPATH, "//div[@title='Anexar']").click()
        time.sleep(2)

        print("[INFO] Enviando imagem...")
        input_img = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        input_img.send_keys(caminho_imagem)
        time.sleep(3)

        print("[INFO] Inserindo legenda...")
        legenda = esperar_elemento(By.XPATH, '//div[@contenteditable="true" and @data-tab]')
        legenda.click()
        legenda.send_keys(mensagem)
        time.sleep(1)

        print("[INFO] Clicando no botão de envio...")
        botao_enviar = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        botao_enviar.click()
        print(f"✅ Mensagem com imagem enviada para {numero}")
        time.sleep(3)

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")

# Enviar mensagem para cada número
for numero in numeros:
    enviar_mensagem(numero)

driver.quit()

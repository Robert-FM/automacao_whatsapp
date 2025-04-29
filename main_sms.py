from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import pandas as pd

# Lista de números com DDI + DDD + número (sem espaços ou sinais)
arquivo_csv = "contatos.csv"

# Carrega os números do CSV
df = pd.read_csv(arquivo_csv)
numeros = df['numero'].astype(str).tolist()

mensagem = 'Caro educador(a), no dia 03/06/2025, teremos nossa a formação presencial do curso "Educação Híbrida para Docentes: da Compreensão à Prática Pedagógica", promovido pelo Ministério da Educação (MEC) em parceria com o Núcleo de Excelência em Tecnologias Sociais (NEES) da Universidade Federal de Alagoas (UFAL). Para garantir sua presença é necessário que até a próxima sexta-feira (02.05.2025) você realize sua inscrição pelo link: https://www.even3.com.br/encontro-presencial-curso-educacao-hibrida-para-docentes-551307/. Qualquer dúvida, estamos à disposição! Um forte abraço da Equipe RIEH.'

# Configurar o Chrome com perfil salvo (evita ter que escanear QR code toda vez)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/Users/Robert Fernandes/AppData/Local/Google/Chrome/User Data")  # Caminho do perfil do seu usuário do Windows
options.add_argument("--profile-directory=Default")  # Substitua por outro se usar perfil secundário
driver = webdriver.Chrome(options=options)

# Função para enviar mensagem
def enviar_mensagem(numero):
    try:
        texto_codificado = quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto_codificado}"
        driver.get(link)
        time.sleep(7)  # Tempo para carregar o chat

        # Localiza a caixa de mensagem (o campo ativo com o texto já preenchido)
        caixa_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        caixa_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)

        print(f"✅ Mensagem enviada para: {numero}")
    except Exception as e:
        print(f"❌ Erro com {numero}: {e}")

# Enviar para todos os números
for numero in numeros:
    enviar_mensagem(numero)

driver.quit()

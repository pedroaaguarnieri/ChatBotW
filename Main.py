import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

n = 0

# Dados para mensagem 04
hoje = datetime.now()
Dia = hoje.day
Mes = hoje.month
Ano = hoje.year
Semana = hoje.weekday() #0 é segunda e 6 domingo
Hora = hoje.hour
Minutos = hoje.minute

if Semana == 0:
    Semana = "Segunda-Feira"
elif Semana == 1:
    Semana = "Terça-Feira"
elif Semana == 2:
    Semana = "Quarta-Feira"
elif Semana == 3:
    Semana = "Quinta-Feira"
elif Semana == 4:
    Semana = "Sexta-Feira"
elif Semana == 5:
    Semana = "Sábado"
else:
    Semana = "Domingo"


# Mensagens - Devem ser escritas corrido.
msg01 = "🚨 *RELATÓRIO DE MUDAS PRONTAS:* Líderes, atualizem o relatório de mudas prontas. Quem já atualizou, mandar um positivo aqui para mim. Obrigado."

msg02 = '⚠️ *RELATÓRIO DE ESTOQUE:* Mantenham as planilhas atualizadas, semanalmente irei pedir os relatórios de estoque. Obrigado.'

msg03 = '⚠️ *BIPEs:* Líderes, não deixem os BIPEs para lançamento no dia posterior, a chance de errar é maior.'

msg04 = (f'☀️ Bom dia a todos! Que Deus abençoe o dia de vocês. {Semana}, {Dia}/{Mes}/{Ano}.')



# Abre o Google
pg = webdriver.Chrome()
pg.get("https://web.whatsapp.com")


# Contagem Regressiva para Fazer Login
t = 90
print('Faça o Login no Whats.')
while t > 0:
    print(f'Iniciando em {t} segundos...')
    t -= 1
    time.sleep(1)

# Localiza o usuário que irá enviar a mensagem
pg.find_element(By.XPATH, '//span[@title="Pedro (CE)"]').click()
time.sleep(3)


while True:

    # Número de Repetição
    n += 1

    hoje = datetime.now()
    Dia = hoje.day
    Mes = hoje.month
    Ano = hoje.year
    Semana = hoje.weekday() #0 é segunda e 6 domingo
    Hora = hoje.hour
    Minutos = hoje.minute

    if Semana == 0:
        Semana = "Segunda-Feira"
    elif Semana == 1:
        Semana = "Terça-Feira"
    elif Semana == 2:
        Semana = "Quarta-Feira"
    elif Semana == 3:
        Semana = "Quinta-Feira"
    elif Semana == 4:
        Semana = "Sexta-Feira"
    elif Semana == 5:
        Semana = "Sábado"
    else:
        Semana = "Domingo"

    # Condições e mensagens

    # Mensagem 01 - Segunda-Quarta-Sexta
    if hoje.weekday() == 0 and Hora == 8 and Minutos == 15:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg01)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 2 and Hora == 8 and Minutos == 15:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg01)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 4 and Hora == 8 and Minutos == 15:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg01)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)

    #Mensagem 02 - Terça-Quinta
    elif hoje.weekday() == 1 and Hora == 15 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg02)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 3 and Hora == 15 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg02)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)

    # Mensagem 03 - Todos os dias úteis
    elif hoje.weekday() == 0 and Hora == 16 and Minutos == 30:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg03)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 1 and Hora == 16 and Minutos == 30:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg03)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 2 and Hora == 16 and Minutos == 30:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg03)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 3 and Hora == 16 and Minutos == 30:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg03)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 4 and Hora == 16 and Minutos == 30:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg03)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)

    # Mensagem 04 - Todos os dias úteis
    elif hoje.weekday() == 0 and Hora == 7 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg04)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 1 and Hora == 7 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg04)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 2 and Hora == 7 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg04)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 3 and Hora == 7 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg04)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)
    elif hoje.weekday() == 4 and Hora == 7 and Minutos == 00:
        pg.find_element(By.CLASS_NAME, '_3Uu1_').send_keys(msg04)
        pg.find_element(By.XPATH, '//span[@data-testid="send"]').click()
        time.sleep(60)

    else:
        time.sleep(1)
        print(f'Código rodando normalmente.')
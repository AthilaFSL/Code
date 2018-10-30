from selenium import webdriver
import datetime
import csv
import os

driver = webdriver.Chrome("C:\\Users\\athd1\\Downloads\\chromedriver_win32\\chromedriver")
UrlMoedas = 'https://m.investing.com/crypto/'

#Acessa URL configurada
driver.get(UrlMoedas)

#Lista as moedas do site
listaMoedas = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr')

#Guarda a data com format determinado
hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

#Varre a lista de moedas
for i in range(0, len(listaMoedas) + 1):
    
    #Recupera a posição ro ranking em formato String
    ranking = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[1]').text
    # print(ranking)
    
    #Recupera o nome da moeda em formato String
    nomeMoeda = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[2]').text
    # print(nomeMoeda)
    
    #Recupra o valor da moeda em formato String
    valorMoeda = str(driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[3]').text).replace(',', '')
    # print(valorMoeda)

    #Criar arquivo para ser escrito
    existente = os.path.isfile("criptomoedas.csv")
    with open("Cripto.csv", 'a', newline='') as entrada:
        
        #Determina o cabeçalho para arquivo .CSV
        cabecalho = ['Posição no ranking', 'Nome', 'Valor(Dolar)', 'Hora']
        arquivo = csv.DictWriter(entrada, delimiter=';', lineterminator='\n', fieldnames=cabecalho)
        
        #Valida a existência do arquivo
        if not existente:
            
            #Escreve o cabeçalho determinado
            arquivo.writeheader()
            
            #Escreve as linhas 
            arquivo.writerow({'Posição no ranking': ranking, 'Nome': nomeMoeda, 'Valor(Dolar)': valorMoeda, 'Hora': hora})

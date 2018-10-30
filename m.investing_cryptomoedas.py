from selenium import webdriver
import datetime
import csv
import os

driver = webdriver.Chrome("C:\\Users\\athd1\\Downloads\\chromedriver_win32\\chromedriver")

UrlMoedas = 'https://m.investing.com/crypto/'

driver.get(UrlMoedas)
listaMoedas = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr')
hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

for i in range(0, len(listaMoedas) + 1):
    ranking = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[1]').text
    # print(ranking)
    nomeMoeda = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[2]').text
    # print(nomeMoeda)
    valorMoeda = str(driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div/div/table/tbody/tr[' + str(i) + ']/td[3]').text).replace(',', '')
    # print(valorMoeda)

    existente = os.path.isfile("criptomoedas.csv")
    with open("Cripto.csv", 'a', newline='') as entrada:

        cabecalho = ['Posição no ranking', 'Nome', 'Valor(Dolar)', 'Hora']
        arquivo = csv.DictWriter(entrada, delimiter=';', lineterminator='\n', fieldnames=cabecalho)
        if not existente:
            arquivo.writeheader()
            arquivo.writerow({'Posição no ranking': ranking, 'Nome': nomeMoeda, 'Valor(Dolar)': valorMoeda, 'Hora': hora})

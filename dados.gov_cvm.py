from selenium import webdriver
import os


driver = webdriver.Chrome("C:\\Users\\athd1\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://dados.gov.br/dataset?_organization_limit=0&organization=comissao-de-valores-mobiliarios-cvm")

#Recupera lista de conjuntos de dados 
conjuntos = driver.find_elements_by_xpath(
    '//*[@id="content"]/div[3]/div/section[1]/div/ul/li/div/h3/a')
#print(len(conjuntos))

#Varre a lista de conjuntos pelo tamanho da própria lista
for i in range(1, len(conjuntos) + 1):
    
    #Clica no elemento do conjunto de dados
    driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/section[1]/div/ul/li['+str(i)+']/div/h3/a').click()
    #Captura o nome do conjunto
    nomeConjunto = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/article/div/h1').text.replace(":", " ")
    
    #Cria o diretorio para conjunto
    caminho = "D:\CVM\\" + nomeConjunto
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        
    #Conjunto de dados (pertence ao conjunto em que se encontra)
    conjuntoDados = driver.find_elements_by_xpath('//*[@id="dataset-resources"]/ul/li/a')
    
    #Varre o conjunto de dados pelo tamanho da própria lista
    for j in range(1, len(conjuntoDados) + 1):
        
        #Captura o link do arquivo pelo elementeo HTML(href)
        link = driver.find_element_by_xpath('//*[@id="dataset-resources"]/ul/li['+str(j)+']/div/ul/li[2]/a').get_attribute("href")
        print(link)
        
        #Escreve o link no arquivo (resulta em um arquivo para cada conjunto de links)
        with open("D:\CVM\\" + nomeConjunto + "\\" + nomeConjunto + ".txt", "a") as text_file:
        text_file.write(link + "\n")
    driver.back()

    #Acessa o wget
    os.system('wget -i "D:\CVM\\{}\\{}.txt" -P "D:\CVM2\\{}\\{}"'.format(nomeConjunto, nomeConjunto, nomeConjunto, nomeConjunto))

    dir = 'D:\\CVM\\{}\\{}'.format(nomeConjunto, nomeConjunto)
    os.chdir(dir)
    for item in os.listdir(dir):
        if item.endswith('.zip'):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(dir)
            zip_ref.close()
            
driver.quit()
































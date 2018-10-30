import sys
import re

#Funções base para o calculo
def som(num1, num2):
    return print(num1 + num2)

def sub(num1, num2):
    return print(num1 - num2)

def mul(num1, num2):
    return print(num1 * num2)

def div(num1, num2):
    return print(num1 / num2)

#Determina o calculo de acordo com o operador
def calculo():
    if parametro[0][1] == '+':
        som(num1, num2)
    elif parametro[0][1] == '-':
        sub(num1, num2)
    elif parametro[0][1] == 'x':
        mul(num1, num2)
    elif parametro[0][1] == '/':
        div(num1, num2)

#Valida a entrada de caracteres
padrao = r'(-?\d+)([-+x/])(-?\d+)'


parametro = (''.join(sys.argv[1:]))
try:

    #Recarrega o parametro com a comparação do padrão e o próprio parametro
    parametro = re.findall(padrao, parametro)

    # Determina num1 e num2 pela posição dentro da string
    num1 = int(parametro[0][0])
    num2 = int(parametro[0][2])

    # Realiza calculo com retorno
    calculo()

except:
    print('Caracter inválido!')
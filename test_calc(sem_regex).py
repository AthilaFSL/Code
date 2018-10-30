import sys

def som(num1, num2):
    return print(num1 + num2)

def sub(num1, num2):
    return print(num1 - num2)

def div(num1, num2):
    return print(num1 / num2)

def mul(num1, num2):
    return print(num1 * num2)

if __name__ == '__main__':

    var = ""
    for param in sys.argv[1]:
        var += param
    # print(var)

if not var.find('+') == -1:
    n1 = int(var[0:var.find('+')])
    n2 = int(var[var.find('+') + 1:])
    print(som(n1, n2))

elif not var.find('-') == -1:
    n1 = int(var[0:var.find('-')])
    n2 = int(var[var.find('-') + 1:])
    print(sub(n1, n2))

elif not var.find('/') == -1:
    n1 = int(var[0:var.find('/')])
    n2 = int(var[var.find('/') + 1:])
    print(div(n1, n2))

elif not var.find('*') == -1:
    n1 = int(var[0:var.find('*')])
    n2 = int(var[var.find('*') + 1:])
    print(mul(n1, n2))



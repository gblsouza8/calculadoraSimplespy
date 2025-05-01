def pegarNumeros():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    return num1, num2

def Calculos(num1, num2):
    print("Subtração:",num1 - num2)
    print("Soma:",num1+num2)
    print("Multiplicação",num1*num2)

    if num2 == 0:
        print("Divisão: [ERRO] Não é possível dividir por 0")
    else:
        print("Divisão:",num1/num2)

def __init__():
    num1, num2 = pegarNumeros()
    Calculos(num1, num2)

__init__()
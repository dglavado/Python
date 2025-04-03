#Função ou procedimento é sempre declarado como def
def isNumeric(valor: str): #Não é obrigatório declarar tipo do parâmetro
    return str(valor).replace(".", "").replace("-", "").isnumeric()

def getNumber():
    num = ""
    while not isNumeric(num):
        num = input('Digite um número: ')
    return num

#A chamada da função deve estar sempre depois da declaração...

#Na chamada de função tem que colocar () - caso contrário atribui a função a variável (não executa)
num1 = getNumber()
num2 = getNumber()
num3 = getNumber()

soma = float(num1) + float(num2)+ float(num3)

print(f'A soma de {num1}, {num2} e {num3} é {soma}')
#A soma de 5.1 e 3.8 é 8.899999999999999
#A soma de -5.1 e 3.8 é -1.2999999999999998
#A soma de 3.5, 2.1 e -1.3 é 4.3
#Erro -5..2
#A soma de 2.1, 3.5 e 1.27 é 6.869999999999999

print('A soma de {:.2f}, {:.2f} e {:.2f} é {:.2f}'.format(float(num1), float(num2), float(num3),soma))
#A soma de 2.10, 3.50 e 1.27 é 6.87

print('Fim')
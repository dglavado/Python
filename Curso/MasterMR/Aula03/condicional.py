#Montar uma calculadora com as operações básicas solicitando 2 numeros e a operação.
def ehNumero(valor):
    return str(valor).replace('.','').replace('-','').isnumeric()

def pegaNumeroReal():
    num = ''
    while not ehNumero(num):
        num = input('Digite número (Real): ')
    return float(num)

operacao = ''
while operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/' and operacao != 'D' and operacao != 'M' and operacao != 'P' and operacao != 'R':
    operacao = input('Digite operação (valores aceitos: +, -, *, /, D, M, P, R): ')

num1 = pegaNumeroReal()
num2 = pegaNumeroReal()


if operacao == '+':
    resultado = num1 + num2
elif operacao == '-': #elif = Else if
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
elif operacao == 'D': #Divisao inteira
    resultado = num1 // num2
elif operacao == 'M': #Resto da divisão inteira
    resultado = num1 % num2
elif operacao == 'P': #Potência
    resultado = num1 ** num2
elif operacao == 'R': #Raiz enésima
    resultado = num1 ** (1 / num2)
else:
    resultado = 'Operação inválida'

match operacao:
    case '+': resultado = num1 + num2
    case '-': resultado = num1 + num2
    case '*': resultado = num1 + num2
    case '/': resultado = num1 + num2
    case _: resultado = "Operação Inválida" #case else


if operacao == '+' or operacao == '-': resultado = 'Soma ou subtração'
elif operacao == '*' or operacao == '/': resultado = 'Multiplicação ou divisão'
else: resultado = 'Operação Inválida'


print(5 > 3 and 5 < 8) #True



print(f'O resultado da operação {operacao}, com os valores: {num1} e {num2} é: {resultado}')
print('Fim')
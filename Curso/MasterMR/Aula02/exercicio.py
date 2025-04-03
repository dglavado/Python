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

print(f'O resultado da operação {operacao}, com os valores: {num1} e {num2} é: {resultado}')
print('Fim')
#O resultado da operação D, com os valores: 5.0 e 2.0 é: 2.0
#O resultado da operação M, com os valores: 5.0 e 2.0 é: 1.0
#O resultado da operação D, com os valores: 5.1 e 2.5 é: 2.0
#O resultado da operação /, com os valores: 5.1 e 2.5 é: 2.04
#O resultado da operação D, com os valores: 5.1 e 2.9 é: 1.0
#O resultado da operação D, com os valores: 5.9 e 2.9 é: 2.0
#O resultado da operação D, com os valores: 5.6 e 2.0 é: 2.0
#O resultado da operação D, com os valores: 5.9 e 2.1 é: 2.0
#O resultado da operação D, com os valores: 6.0 e 2.0 é: 3.0
#O resultado da operação D, com os valores: 5.0 e 2.9 é: 1.0



#num1 = 5
#num2 = 3
# == comparação
# != diferente
# = atribuição
#operacao = ''
#1.6666666666666667


#if operacao == '+':
#    resultado = num1 + num2
#elif operacao == '-': #elif = Else if
#    resultado = num1 - num2
#elif operacao == '*':
#    resultado = num1 * num2
#elif operacao == '/':
#    resultado = num1 / num2
#else:
#    resultado = 'Operação inválida'

#print(resultado)

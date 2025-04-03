#Criar um código com os 7 dias da semana numa tupla e solicitar ao usuário 7 sabores para rechear um pão no café da manhã
#
#Criar um método que solicite o dia da semana e o sabor e print no console um passo a passo que ensine uma criança a preparar o café da manhã. Exemplo de saída:
#
#1) Pegar o pão
#2) Pegar a faca e colher
#3) Cortar o pão usando a faca
#4) Utilizar a colher para passar {manteiga, requeijão, doce de leite, etc} no pão
#5) Fechar o pão
#6) Comer o pão com {manteiga, requeijão, doce de leite, etc}

def mid(str, posicao, tamanho):
    return str[posicao:posicao+tamanho]

def left(str, tamanho):
    return str[:tamanho]

def right(str, tamanho):
    return str[-tamanho:]

sabores = []

diasDaSemana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

for i in range(7):
    sabores.append(input(f"Digite o sabor {i+1} de 7:"))

for i in diasDaSemana: print(i)


print(f'Sabores do pão nos dias da semana:')
for i in range(7):
    print(f'{diasDaSemana[i]}: {sabores[i]}')

#Sabores do pão nos dias da semana:
#Segunda-feira: manteiga
#Terça-feira: margarina
#Quarta-feira: maionese
#Quinta-feira: goiabada
#Sexta-feira: nutella
#Sábado: patê
#Domingo: doce de leite

strSabores = str(sabores)

strSabores = strSabores.replace('[','').replace(']','').replace("'","")

#qtd = strSabores.count(',')
#posicao = 0
#for _ in range(qtd):
#    posicao = strSabores.index(',', posicao + 1)
#    posicao += 1 
#posicao -=1

#como substituir a última vírgula por e?

tamanho = len(strSabores)
posicao = strSabores.rfind(',')

strSabores = left(strSabores, posicao) + ' e' + right(strSabores, tamanho - posicao - 1)


print(f'Instruções:')
print(f'1) Pegar o pão')
print(f'2) Pegar a faca e colher')
print(f'3) Cortar o pão usando a faca')
print(f'4) Utilizar a colher para passar {strSabores} no pão')
print(f'5) Fechar o pão')
print(f'6) Comer o pão com {strSabores}')
#Comer o pão com manteiga, margarina, maionese, patê, azeite e sal, goiabada e nutella

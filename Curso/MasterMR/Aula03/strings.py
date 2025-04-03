#Toda string é uma iterável
#Iterar é pegar cada elemento de um conjunto
#No Python todo índice começa com 0
#No Python tudo que for iterável, eu consigo pegar um determinado elemento pelo index utilizando []
#Em Python, sempre começa com índice 0 e o final é exclusivo, ou seja, o número de index que iformei como final, não vai entrar
#[start:end:step] - [início:final:pularDeTantoEmTanto]


def removeAccents (text: str):
    return text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')


nome = "Márcio Ribeiro"
print(nome)

primeiroNome = nome[0:6]
print(primeiroNome) #Marcio

print(nome[0:6:2]) #Mri

print(nome[5:-1:-1]) #Erro
print(nome[5:0:-1]) #oicra

print(nome[0:-4]) #Marcio Rib

nome = nome.capitalize() #Deixa só a primeira letra do texto em maiúscula
nome = nome.lower()
nome = nome.upper()
nome = nome.title()

#F5 Executa
#F10 por linha
#debug Console
#O Python é case sensitive

nome.index('o') #5
nome.index('o', 6) #13

qtde = nome.count('o')
posicao = 0

for i in range(qtde): #Stop - para minha varável de interação (i) no meu intervalo (in range)
    posicao = nome.index('o', posicao + 1)
    print(posicao)
    posicao += 1 #posicao = posicao + 1

posicao = 0
for _ in range(qtde): #_ não armazena o valor de i
    posicao = nome.index('o', posicao + 1)
    print(posicao)
    posicao += 1 #posicao = posicao + 1

for letra in nome:
    print(letra)

print('Ribeiro' in nome) #True
print('ribeiro' in nome) #False

print('ribeiro' in nome.lower()) #True

print(len(nome))

nome.lower().startswith('m')  #True
nome.lower().endswith('o')  #True

print('marcio' in removeAccents(nome.lower()))


nome = 'Márcio Alves Ribeiro'
nomes = nome.split() #Quebra texto em vetor - delimitador padrão é espaço

primeiroNome = nomes[0]
ultimoNome = nomes[-1] #Último ítem (-1) nome

print(' '.join(nomes)) #Ao contrário de split

nome = '   Marcio Ribeiro    '
print(nome.strip())
print(nome.lstrip())
print(nome.rstrip())


cod = 1234 #0000001234
cod = str(cod).zfill(10) #completa com 0 a esquerda


print('Fim')
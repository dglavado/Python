#Exercício: Receber uma Lista e fazer 2 funções:
#Retornar a maior palavra da lista e retornar a menor palavra da lista.

#Retorna a maior palavra a aparecer primeiro na lista.
def maiorPalavra(lista):
    maior = lista[0]
    #Acho estranho um for assim, mas foi a IA que gerou.
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

#Retorna a menor palavra a aparecer primeiro na lista.
def menorPalavra(lista):
    menor = lista[0]
    #Acho estranho um for assim, mas foi a IA que gerou.
    for palavra in lista:
        if len(palavra) < len(menor):
            menor = palavra
    return menor

def palavrasMesmoTamanho(lista, tamanho):
    listaIgual = []
    for i in range(len(lista)):
        if len(lista[i]) == tamanho:
            listaIgual.append(lista[i])
    return listaIgual


# Programa principal
print('Digite uma lista de palavras, separadas por vírgula. Se estiver com preguiça, digite Enter e use uma lista padrão: ')
lista = input()

if len(lista) == 0:
    lista = ['carro', 'casa', 'fé', 'paralelepípedo', 'às', 'anticonstitucionalissimamente', 'as', 'pneumoultramicroscopicossilicovulcanoconiótico', 'banana', '1234567890123456789012345678901234567890123446' ]
else:
    lista = lista.split(',')
    #Deixa a lista sem espaços em branco - Difícil entender um for assim.
    lista = [palavra.strip() for palavra in lista]

print(f'Lista de palavras: {lista}')

palavra = maiorPalavra(lista)
tamanho = len(palavra)
print(f'A maior palavra da lista (a aparecer primeiro) é: {palavra}, com {tamanho} letras.')

palavrasTamIgual = palavrasMesmoTamanho(lista, tamanho)
if palavrasTamIgual != []:
    print(f'Existem palavras do mesmo tamanho que a maior palavra: {palavrasTamIgual}')

palavra = menorPalavra(lista)
tamanho = len(palavra)
print(f'A menor palavra da lista (a aparecer primeiro) é: {palavra}, com {len(palavra)} letras.')

palavrasTamIgual = palavrasMesmoTamanho(lista, tamanho)
if palavrasTamIgual != []:
    print(f'Existem palavras do mesmo tamanho que a menor palavra: {palavrasTamIgual}')

#Lista é mutável e flexível
#Cria a lista com colchetes []


nomes = ['Bruno Gonçalves', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Jorge', 'Luis', 'Marcos', 'Mauricio', 'Paulo']

nomes[0] = 'Bruno'
nomes.append('Marcio') #adiciona registro na última posição da lista
nomes.remove('Marcio') #retira a primeira ocorrência do registro pelo valor

nomes.append(nomes.pop(1)) #.pop remove pela posição (e .append joga para o final)


nomes = ['Jorge', 'Paulo', 'Luis', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Marcos', 'Bruno Gonçalves', 'Mauricio' ]

nomes[nomes.index('Bruno Gonçalves')] = 'Bruno G.'
nomes[nomes.index('Bruno Schambeck')] = 'Bruno S.'

nomes.reverse()




nomes.sort() #Ordena A-Z nomes.sort(reverse=False)
nomes.sort(reverse=True) #ordem decrescente Z-A

nomes.clear() #Limpa a lista

nomes = ['Jorge', 'Paulo', 'Luis', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Marcos', 'Bruno Gonçalves', 'Mauricio' ]

nomes.count('Jorge') #1

nomes.insert(0, 'Marcio') #insere na posição passada

nomes.append('Felipe Figueira')
nomes.append('Paola')

nomes2 = ['Felipe Figueira', 'Paola']

nomes.append(nomes2) #Adiciona no fim a lista (não colocará cada elemento da lista)

nomes = ['Jorge', 'Paulo', 'Luis', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Marcos', 'Bruno Gonçalves', 'Mauricio', 'Marcio' ]


nomes.extend(nomes2) #Adiciona cada elemento no final da lista

nomes2 = nomes #Iguala as 2 listas, qq alteração em uma, altera a outra / Ficam linkados

nomes2.sort() #A ordenação afeta as 2 listas

nomes2 = nomes.copy() #Cria uma nova variável, recebendo a cópia da lista (nomes)



nomes2.remove('Marcio')
nomes2.sort(reverse=True) #com o .copy, as listas ficam independentes


nome = 'Marcio'


for nome in nomes:
    print(nome)

for i in range(0,len(nomes)): #o início 0, não é obrigatório
    print(nomes[i])




print('fim')
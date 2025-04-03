#Lista é mutável e flexível
#Cria a lista com colchetes []


nomes = ['Bruno Gonçalves', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Jorge', 'Luis', 'Marcos', 'Mauricio', 'Paulo']

nomes[0] = 'Bruno'
nomes.append('Marcio') #adiciona registro na última posição da lista
nomes.remove('Marcio') #retira a primeira ocorrência do registro pelo valor

nomes.append(nomes.pop(1)) #Pop remove pela posição (e joga para o final)

nomes.sort() #Ordena
nomes.sort(reverse=True) #ordem decrescente

print('fim')
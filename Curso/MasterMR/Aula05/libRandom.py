import random as rd

#gera número aleatório entre 0 e 1
print(rd.random())
print(rd.random())
print(rd.random())
print(rd.random())
print(rd.random())
print(rd.random())
print('-' * 100)

#gerar aleatório entre 2 números
print(rd.randrange(1, 100))#fim é exclusivo, não vai até o 100
print(rd.randrange(1, 100)) #começa
print(rd.randrange(1, 100))
print(rd.randrange(1, 100))
print('-' * 100)

#gera números pares aleatórios entre 0 e 100
print(rd.randrange(0, 100, 2)) #step 2 - começando em 0 (par)
print(rd.randrange(0, 100, 2)) #step 2
print(rd.randrange(0, 100, 2)) #step 2
print(rd.randrange(0, 100, 2)) #step 2
print('-' * 100)

#gera números ímpares aleatórios entre 1 e 99 
print(rd.randrange(1, 100, 2)) #step 2 - começando em 1 (ímpar)
print(rd.randrange(1, 100, 2)) #step 2
print(rd.randrange(1, 100, 2)) #step 2
print(rd.randrange(1, 100, 2)) #step 2
print('-' * 100)

#Gerar números com 2 casas decimais aleatórios entre 1 e 99
print(rd.randrange(100, 10000, 2)/100) 
print(rd.randrange(100, 10000, 2)/100) 
print(rd.randrange(100, 10000, 2)/100) 
print(rd.randrange(100, 10000, 2)/100) 
print('-' * 100)

#Gerar números com 1 casa decimais aleatórios entre 1 e 100
print(rd.randrange(10, 1010, 2)/10) 
print(rd.randrange(10, 1010, 2)/10) 
print(rd.randrange(10, 1010, 2)/10) 
print(rd.randrange(10, 1010, 2)/10) 
print('-' * 100)


nomes = ['Bruno Gonçalves', 'Bruno Schambeck', 'Felipe Araujo', 'Felipe Figueira', 'Gabriel', 'Jorge', 'Marcos', 'Mauricio', 'Paola', 'Paulo']

rd.shuffle(nomes) #embarala a lista

g1 = nomes[:5] #de 0 a 4
g2 = nomes[5:] #de 5 até o fim


nomes = ['Bruno Gonçalves', 'Bruno Schambeck', 'Felipe Araujo', 'Felipe Figueira', 'Gabriel', 'Jorge', 'Marcos', 'Mauricio', 'Paola', 'Paulo']
print(rd.choice(nomes))
print(rd.choice(nomes))

for i in range(3):
    print(f'O {i+1}º sorteado foi: {rd.choice(nomes)}')
#O 1º sorteado foi: Bruno Schambeck
#O 2º sorteado foi: Bruno Schambeck
#O 3º sorteado foi: Felipe Figueira    
print('-' * 100)


for i in range(1, 4): #faz o range começar de 1 em vez de 0 como no anterior
    sorteado = rd.choice(nomes) #removendo para não repetir
    nomes.remove(sorteado)
    print(f'O {i}º sorteado foi: {sorteado}')
print('-' * 100)

#participantes = nomes #dessa forma fica linkado
participantes = nomes.copy() #para gerar cópia (não link)
for i in range(1, 4): 
    sorteado = rd.choice(participantes) #removendo para não repetir
    participantes.remove(sorteado)
    print(f'O {i}º sorteado foi: {sorteado}')


print('fim')
#tupla é imutável, uma vez criada não pode ser alterada
#Como qq outra variáve no Python pode ser recriada até com outro tipo a qq momento
#não é possível adicionar novos registros, alterar ou eliminar
#tupla cria utilizando parênteses

nomes = ('Bruno Gonçalves', 'Bruno Schambeck', 'Eric', 'Gabriel', 'Jorge', 'Luis', 'Marcos', 'Mauricio', 'Paulo')


#nomes[8] = 'Paulo Marins' #erro
#nomes[9] = 'Marcio' #erro


nomes = ('Bruno', 'Bruno', 'Eric', 'Gabriel', 'Jorge', 'Luis', 'Marcos', 'Mauricio', 'Paulo', 'Marcio')

print(nomes.count('Eric')) #1
print(nomes.count('Bruno')) #2
print(nomes.index('Jorge')) #4

for i in range(len(nomes)): #len = 10 mas o limite é exclusivo ou seja não precisa fazer -1 não há estouro
    print(nomes[i])


for nome in nomes:
    print(nome)

print('fim')
nomes = ('Bruno Gonçalves', 'Bruno Schambeck', 'Eric', 'Felipe Araujo', 'Felipe Figueira', 'Gabriel', 'Jorge', 'Marcos', 'Mauricio', 'Paola', 'Paulo')

pizzas = list()
#pizzas = []

for nome in nomes:
    pizzas.append(input(f'{nome} - Pizza favorita: '))

for i in range(len(nomes)):
    print(f'A pizza favorita de {nomes[i]} é {pizzas[i]}')

for index, nome in enumerate(nomes): #(0, 'Bruno Gonçalves'), (1, Bruno Schambeck').... - enumerate gera índices
    print(f'A pizza favorita de {nome} é {pizzas[index]}')

#VBA
#cont = 0
#for Each nome in nomes
#    cont = cont + 1
#    Debug.print("A pizza favorita de " & nome & " é " pizzas(cont))
#next

#for i = 1 to Ubound(nomes)
#    Debug.Print("A pizza favorita de " & nomes(i) & " é " & pizzas(i))
#Next

#(0, 'Bruno Gonçalves'), (1, Bruno Schambeck')
#index, nome, teste = (0, 'Bruno Gonçalves', 'abc') -> Joga em cada uma

#A piza favorita de Bruno Gonçalves é Peperoni
#A piza favorita de Bruno Schambeck é Filé
#A piza favorita de Eric é Frango com Catupiry
#A piza favorita de Felipe Araujo é queijo
#A piza favorita de Felipe Figueira é calabresa
#A piza favorita de Gabriel é Baiana
#A piza favorita de Jorge é Portuguesa
#A piza favorita de Marcos é Marguerita
#A piza favorita de Mauricio é Portuguesa
#A piza favorita de Paola é Marguerita
#A piza favorita de Paulo é Chocolate

print('Fim')

#https://docs.python.org/3/library/index.html


nomes = ['Bruno Gonçalves', 'Bruno Schambeck', 'Eric', 'Felipe Araujo', 'Felipe Figueira', 'Gabriel', 'Jorge', 'Marcos', 'Mauricio', 'Paola', 'Paulo', 'Luiz Gustavo']

pizzas = ['Peperoni', 'Filé', 'Frango com Catupiry', 'Queijo', 'Calabresa', 'Baiana', 'Portuguesa', 'Marguerita', 'Portuguesa', 'Marguerita', 'Chocolate', 'Marguerita']


pizzasFavoritas = list(zip(nomes, pizzas)) #juntar
pizzasFavoritas.sort() #ordenar

nomes, pizzas = zip(*pizzasFavoritas) #com zip - Separar (ordenado)

nomes = [] #zerando para usar o código abaixo
pizzas = []

nomes, pizzas = [[nome for nome, pizzas in pizzasFavoritas], [pizza for nome, pizza in pizzasFavoritas]] #com list comprehension
#pizzasFavoritas (tupla)
#monta uma lista, sem precisar fazer o loop


nomes, pizzas = [[nome for nome, _ in pizzasFavoritas], [pizza for _, pizza in pizzasFavoritas]] #com list comprehension
# _ substituindo a variável que não será utilizada - por esse motivo a variável pizzas fica "cinza" no primeiro bloco e nome no segundo bloco for


print('Fim')
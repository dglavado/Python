#def smallerWord(words: list): #Força ser uma lista
def smallerWord(words):
#	if not words:
	if len(words) == 0:
		return None #Null, nil, void

    #if type(words) not list:
	if type(words) != list:
        #raise Exception('words is not a list')
		return None

	if len(words) == 1:
		return words[0]

	ret = words[0]
	
	for w in words[1:]:
		print(f'Comparando {ret} com {w}')
		if len(ret) > len(w):
#		if len(ret) >= len(w): #Pega a última
			print(f'{ret} é maior {w}')  #Place holder {variável}
			ret = w
	return ret


def largestWord(words):
	if len(words) == 1:
		return words[0]

#	if not words:
	if len(words) == 0:
		return None #Null, nil, void

	ret = words[0]
	
	for w in words[1:]:
		print(f'Comparando {ret} com {w}')
		if len(ret) < len(w):
			print(f'{ret} é maior {w}')  #Place holder {variável}
			ret = w
	return ret



list1 = ['macaco', 'girafa', 'Fino', 'elefante', 'Pedro', 'paz', 'palavra', 'paralelepípedo', 'sol']

print(f'Para a lista:\n{list1}\nA menor palavra eh: {smallerWord(list1)}')

list2 = ['arroz']
print(smallerWord(list2)) #não entra no for

list3 = []
print(smallerWord(list3)) #Dá Erro

list4 = 'palavra'
print(smallerWord(list4)) #Traz a primeira letra (considera uma string uma lista)


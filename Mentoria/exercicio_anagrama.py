#Desafio 1 -> Reverso
#Desafio 2 -> Dada uma palavra, dizer se é paríndromo (ana, ovo, arara, asa, A MANCHA NA CHAMA )
#Desafio 3 -> Descobrir se 2 palavras são anagramas (mesmas letras -> Roma amor - Pedra, padre - TRETA, ateRt: True)

def retReverse(word):
	#Retornando o reverso da palavra
	return word[::-1]

def isPalindrome(word):
	#Convertendo para maiúsculo para comparar
	word = word.upper()
	#Retorno antigo, só funciona com palavra (não com frases) - gerado por IA:
	#return word == retReverse(word)

	lenth = len(word)
	revWord = lenth-1
	#Fazendo a comparação letra a letra pois a comparação direta não aceita uma frase
	for i in range(lenth):
		#Se o caractere for espaço, não faz a comparação
		if not (word[i] == ' ' or word[revWord] == ' '):
			if word[i] == word[revWord]:
				bPalindrome = True
			else:
				bPalindrome = False
		revWord -= 1
	return bPalindrome

def isAnagram(word1, word2):
	#Convertendo para maiúsculo para comparar
	word1 = word1.upper()
	word2 = word2.upper()

	#Solução fácil, gerada por IA:
	#Comparando as letras ordenadas e retornando o resultado
	#return sorted(word1) == sorted(word2)

	#Solução mais difícil, mas que não usa o sorted:
	#Considerando que tem que ter a mesma quantidade de letras (ex.: casa e asa não são anagramas)
	if len(word1) != len(word2):
		return False
	for i in range(len(word1)):
		if word1.count(word1[i]) != word2.count(word1[i]):
			return False
	return True

	

print("Digite uma palavra ou frase para obter seu reverso e verificar se trata-se de um palíndromo: ")
word = input()

if word == '':
	word = 'Socorram-me, subi no ônibus em Marrocos'
	print(f'Como não foi digitado nada, vou considerar o maior palíndromo da língua Portuguesa: {word}')

rWord = retReverse(word)
print(f'O reverso da palavra é: {rWord}')

if isPalindrome(word):
	print(f'A palavra ou frase: {word} é um palíndromo - {rWord}')
else:
	print(f'A palavra ou frase: {word} NÃO é um palíndromo - {rWord}')


print("Digite duas palavras separadas por espaço para verificar se são anagramas:")
words = input()
if len(words.split()) != 2 or words == '':
	word1 = 'pedra'
	word2 = 'padre'
	print(f'Como a entrada não foi válida, vou considerar as palavras: {word1} e {word2}')
else:
	word1, word2 = words.split()


if isAnagram(word1, word2):
	print(f'As palavras {word1} e {word2} são anagramas')
else:
	print(f'As palavras {word1} e {word2} NÃO são anagramas')

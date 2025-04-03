#converte para inteiro, mas dá erro se não for ex.: 10.
#num1 = int(input('Digite um número: '))
#num2 = int(input('Digite um número: '))

#Concatena as variáveis pois padrão é str
#soma = num1 + num2


num1 = ""
while not num1.isnumeric(): #isnumero(ficará em loop enquanto não for numérico) // Não existe Do While, deve-se "forçar" a entrada no loop (num1="")
    num1 = input('Digite um número: ') #indentação obrigatória
#ficará dentro do loop até que se digite um valor numérico - 15.0 não é numérico

num2 = ""
while not num2.isnumeric(): # : é obrigatório para o loop
    num2 = input('Digite um número: ') 

#Convertendo str para int
num1 = int(num1)

soma = int(num1) + int(num2)

#Gera erro pois num2 é string (conversão feita apenas para a soma), e soma é inteiro
#print('A soma de ' + num1 + ' e ' + num2 + ' é ' + soma)
print('A soma de ' + str(num1) + ' e ' + num2 + ' é ' + str(soma))

#Sem erro
print(f'A soma de {num1} e {num2} é {soma}')




num3 = ""
while not num3.replace(".", "").replace("-", "").isnumeric(): # replace vai tirar o . e - apenas para a validação do isnumeric, sem alterar a variável
    num3 = input('Digite um número: ') 

num4 = ""
while not num4.replace(".", "").replace("-", "").isnumeric(): 
    num4 = input('Digite um número: ')     

soma = float(num3) + float(num4)

print(f'A soma de {num3} e {num4} é {soma}')

print('Fim')
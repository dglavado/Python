# Padrões do Python
# snack case
# este_eh_um_exemplo_de_utilizacao_de_snack_case = ''

# camel case
# esteEhUmExemploDeUtilizacaoDeCamelCase = ''

# Nomes de variáveis, módulos e funções iniciando com letra minúscula
# Nomes de classe iniciando com letra Maiúscula

# Ctrl + ; Inclui ou retira comentário
# Ctrl + " Abre o terminal
# F5 Depurar ou debugar o código
# Ctrl + F5 - Executa

#Execução em linha de comando: python.exe comandosIniciais.py
#python --version
#Python 3.13.1
#pip --version
#pip 24.3.1

#No prompt digite python e digite comandos diretamente


# Imprime no terminal - texto em aspas simples ou aspas duplas
#print('Seja bem vindo, "Marcio" !!!')

#F5 - Debug -> Executa tudo até o Breakpoint
#Ctrl + F5 -> Ignora os breakpoints
#F11 - Executa linha a linha entrando nas funções
#F10 - Executa a linha a linha, sem entrar nas funções (executando diretamente)
#Debug Console -> type(<nomeDaVariavel>) -> mostra o tipo da variável

#Tipagem dinâmica - e altamente tipavel
#Retorno de input é sempre String (str)

nome = input("Digite seu nome: ")
idade = 41
meses = '12'

qtdeMeses = idade * meses
#qtdeMeses = '1212121212121212121212121212121212121212121212121212121212121212121212121212121212' - Repete a str 12, 41x
#Não dá pra somar variáveis de tipos diferentes idade + meses dá erro

print("Seja Bem vindo, " + nome + "!!!")

#f - formated strings
print(f"seja bem vindo, {nome}!!!")


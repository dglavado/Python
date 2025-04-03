#Tratamento de Erros/Exceções
#No try eu sou obrigado a ter pelo menos o try e mais uma das opçpões abaixo
#Except
#Finally


import os, subprocess


print(os.getenv('username'))
print(os.getenv('userdomain'))
print(os.getenv('path'))
#no DOS é SET

#subprocess.run('wmic bios get serialnumber')
#subprocess.Popen()
subprocess.run('calc')



def getNumber():
    while True: #Loop infinito
        try:
            num = float(input('Digite um número: '))
            
            break #Sai do loop
        except:
            pass #O pass não faz nada... Serve apenas para ter uma linha no Except
    return num #Sem a linha do return, não funciona


a = 5

b = 6

#if resultado


try:
    resultado = a + b
except: #Se der erro, entra aqui
    #print(f'Se você está lendo esta mensagem significa que deu tudo certo e o resultado é: {resultado}')
    #variável mensagem com erro, pois não tenho o resultado (que está no try)
    #similar a verificar uma variável (em if por exemplo), antes de calcular ou definir
    print(f'Se você está lendo esta mensaqgem significa que deu ruim!!!')
else:   #Se não der erro entra aqui
    print(f'Se você está lendo esta mensagem significa que deu tudo certo e o resultado é: {resultado}')
finally: #VAi executar dando erro ou não
    print('Finalizado!!! Esta msg irá aparecer independente de dar certo ou não!!!')


print('-' * 100)
b = '6'

try: #Tentar
    resultado = a + b


except: #Exceção
    print('Não é possível fazer esta conta, verifique as variáveis.')

def soma(num1, num2):
    #resultado = num1 + num2
    #return resultado
    return num1 + num2
#44:53

num1 = getNumber()
num2 = getNumber()
resultado = soma(num1, num2) #sem retrun, o resultado é None

print(soma(num1, num2))


print('Fim')



#Exemplo VBA
#Function getNumber()
#    On Error Resume next
#        Do
#            Err.Clerar
#            num = CDbl(InputBox("Digite um número:"))]
#        Loop While CBool(Err)
#    On Error GoTo 0
#    getNumber = num
#End Function

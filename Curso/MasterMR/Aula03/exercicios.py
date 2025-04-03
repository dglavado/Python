#Montar um função que retorne o conceito à partir de uma nota de 0 a 10:
#Se Nota >=7 >>> Aprovado
#Se Nota entre 5 e <7 >>> Exame
#Se nota <5 >>> Reprovado





#Cria lista vazia
sabores = []
sabores = list()

def isNumero(valor: str): #para não aceitar decimal
    return str(valor).isnumeric()

def getNota():
    num = ""
    while not isNumero(num): 
        num = input('Digite a Nota: ')
    return num

def resultado(nota: int):
    if      nota > 10 or nota < 0:      return "Nota Inválida"
    elif    nota >= 7:                  return "Aprovado"
    elif    nota >  5:                  return "Exame" #para forçar erro caso nota = 5 (sem else)
    elif    nota <  5:                  return "Reprovado"
    #else :                              return "Erro"
    
nota = getNota() #Nota 5 sem else e sem >= >> none

print(resultado(int(nota)))



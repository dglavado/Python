#Exercício 01 - Gerar 5 funções que calculem o perímetro e a área de um triângulo e de um quadrilátero, além de uma função que verifique se o quadrilátero é um quadrado ou não.
#Código Refeito com as correções e entendimentos.

#Converte uma String para um array de inteiros.
def convertToInt(valores):
    valores = valores.split(',')
    for i in range(len(valores)):
        valores[i] = int(valores[i])
    return valores


def perTriangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

#Perímetro supondo que o quadrilátero é um retângulo ou quadrado.
def perQuadrilatero(lado1, lado2):
    return 2 * lado1 + 2 *  lado2

#Área do triângulo. KISS - Keep It Simple Stupid
def areaTrianguloKiss(base, altura):
    return base * altura / 2

#Área do triângulo. KICK - Keep It Complicated Karayo
def areaTrianguloKick(lado1, lado2, lado3):
    #Fórmula de Heron
    s = (lado1 + lado2 + lado3) / 2
    area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
    return area


#Área supondo que o quadrilátero é um retângulo ou quadrado.
def areaQuadrilatero(lado1, lado2):
    return lado1 * lado2

def ehQuadrilatero(lados, angulos):
    #Deve ter 4 lados e 4 ângulos.
    if len(lados) == 4 and len(angulos) == 4:
        #A soma dos Ângulos deve ser 360 graus.
        if (angulos[0] + angulos[1] + angulos[2] + angulos[3]) == 360:
            return True
    else:
        return False

def ehQuadrado(lados, angulos):
    #Deve ser um quadrilátero.
    if ehQuadrilatero(lados, angulos):
        #Deve ter todos os lados iguais e todos os ângulos iguais a 90 graus.
        if (lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3]) and (angulos[0] == angulos[1] and angulos[1] == angulos[2] and angulos[2] == angulos[3] and angulos[3] == 90):
            return True
    else:
        return False

def ehRetangulo(lados, angulos):
    if ehQuadrilatero(lados, angulos):
        #Se todos os ângulos não forem iguais a 90 graus, não é retângulo. Pode ser um trapézio, losango ou polígono irregular.
        if angulos[0] == angulos[1] and angulos[1] == angulos[2] and angulos[2] == angulos[3] and angulos[3] == 90:
            #Se todos os lados forem iguais, não é retângulo. É um quadrado.
            if lados[0] == lados[1] and lados[1] == lados[2] and lados[2] == lados[3]:
                return False

            #Se houver 2 pares de lados iguais, é retângulo.
            #Tentei fazer com for, mas ficou complicado...
            elif lados[0] == lados[1] and lados[2] == lados[3]:
                return True
            elif lados[0] == lados[2] and lados[1] == lados[3]:
                return True
            elif lados[0] == lados[3] and lados[1] == lados[2]:
                return True
            #Se não houver 2 pares de lados iguais, não é retângulo.
            else:
                return False
        else:
            return False
    #Se não for quadrilátero, não é retângulo.
    else:
        return False

#Função principal
print(f'Qual função você deseja utilizar? - Importante o Sistema só aceita números inteiros positivos, não está implementado tratamento de erros!')
print(f'1 - Perímetro do Triângulo, 2 - Perímetro do Quadrilátero, 3 - Área do Triângulo, 4 - Área do Triângulo informando os lados, 5 - Área do Quadrilátero, 6 - É quadrilátero?, 7 - É quadrado?, 8 - É retângulo?')
opcao = int(input())

if opcao == 1:
    print('Digite o lado 1: ')
    lado1 = int(input())
    print('Digite o lado 2: ')
    lado2 = int(input())
    print('Digite o lado 3: ')
    lado3 = int(input())
    print(f'O perímetro do triângulo é {perTriangulo(lado1, lado2, lado3)}')
elif opcao == 2:
    print('Digite o lado 1: ')
    lado1 = int(input())
    print('Digite o lado 2: ')
    lado2 = int(input())
    print(f'O perímetro do quadrilátero é {perQuadrilatero(lado1, lado2)}')
elif opcao == 3:
    print('Digite a base: ')
    base = int(input())
    print('Digite a altura: ')
    altura = int(input())
    print(f'A área do triângulo é {areaTrianguloKiss(base, altura)}')
elif opcao == 4:
    print('Digite lado1: ')
    lado1 = int(input())
    print('Digite lado2: ')
    lado2 = int(input())
    print('Digite lado3: ')
    lado3 = int(input())
    print(f'A área do triângulo é {areaTrianguloKick(lado1, lado2, lado3)}')
elif opcao == 5:
    print('Digite o lado 1: ')
    lado1 = int(input())
    print('Digite o lado 2: ')
    lado2 = int(input())
    print(f'A área do quadrilátero é {areaQuadrilatero(lado1, lado2)}')
elif opcao == 6:
    print('Digite os Lados do Quadrilátero separados por vírgula: ')
    lados = convertToInt(str(input()))
    print('Digite os Ângulos do Quadrilátero separados por vírgula: ')
    angulos = convertToInt(str(input()))
    if ehQuadrilatero(lados, angulos):
        print(f'A figura é um Quadrilátero!')
    else:
        print(f'A figura não é um Quadrilátero!')
elif opcao == 7:
    print('Digite os Lados do Quadrado separados por vírgula: ')
    lados = convertToInt(str(input()))
    print('Digite os Ângulos do Quadrado separados por vírgula: ')
    angulos = convertToInt(str(input()))
    if ehQuadrado(lados, angulos):
        print(f'A figura é um Quadrado!')
    else:
        print(f'A figura não é um Quadrado!')
elif opcao == 8:
    print('Digite os Lados do Retângulo separados por vírgula: ')
    lados = convertToInt(str(input()))
    print('Digite os Ângulos do Retângulo separados por vírgula: ')
    angulos = convertToInt(str(input()))
    if ehRetangulo(lados, angulos):
        print(f'A figura é um Retângulo!')
    else:
        print(f'A figura não é um Retângulo!')        

else:
    print('Opção inválida')

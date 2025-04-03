#Exercício 01 - Gerar 5 funções que calculem o perímetro e a área de um triângulo e de um quadrilátero, além de uma função que verifique se o quadrilátero é um quadrado ou não.
#Código gerado por IA (praticamente todo).

def perTriangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def perQuadrilatero(lado1, lado2):
    return 2 * lado1 + 2 *  lado2

def areaTriangulo(base, altura):
    return base * altura / 2

def areaQuadrilatero(lado1, lado2):
    return lado1 * lado2

print(f'Qual função você deseja utilizar? 1 - Perímetro do Triângulo, 2 - Perímetro do Quadrilátero, 3 - Área do Triângulo, 4 - Área do Quadrilátero, 5 - É quadrado?')
opcao = int(input())

if opcao == 1:
    print('Digite o lado 1: ')
    lado1 = float(input())
    print('Digite o lado 2: ')
    lado2 = float(input())
    print('Digite o lado 3: ')
    lado3 = float(input())
    print(f'O perímetro do triângulo é {perTriangulo(lado1, lado2, lado3)}')
elif opcao == 2:
    print('Digite o lado 1: ')
    lado1 = float(input())
    print('Digite o lado 2: ')
    lado2 = float(input())
    print(f'O perímetro do quadrilátero é {perQuadrilatero(lado1, lado2)}')
elif opcao == 3:
    print('Digite a base: ')
    base = float(input())
    print('Digite a altura: ')
    altura = float(input())
    print(f'A área do triângulo é {areaTriangulo(base, altura)}')
elif opcao == 4:
    print('Digite o lado 1: ')
    lado1 = float(input())
    print('Digite o lado 2: ')
    lado2 = float(input())
    print(f'A área do quadrilátero é {areaQuadrilatero(lado1, lado2)}')
elif opcao == 5:
    print('Digite o lado 1: ')
    lado1 = float(input())
    print('Digite o lado 2: ')
    lado2 = float(input())
    if lado1 == lado2:
        print('É um quadrado')
    else:
        print('Não é um quadrado')
else:
    print('Opção inválida')

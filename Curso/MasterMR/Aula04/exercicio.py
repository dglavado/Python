import operator

calculo = dict()
calculo['+'] = operator.add
calculo['-'] = operator.sub
calculo['*'] = operator.mul
calculo['/'] = operator.truediv

a = 5
b = 2

resultado = calculo['+'](5,2)

print(calculo['+'](5,2))
print(calculo['-'](5,2))
print(calculo['*'](5,2))
print(calculo['/'](5,2))


print('fim')


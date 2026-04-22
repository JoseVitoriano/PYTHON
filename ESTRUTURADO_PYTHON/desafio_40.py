'''Programa de Fatorial'''

print('Programa de Fatorial, Vamos la ?')
print('~' * 80)

num = int(input('Informe o numero para calculo do fatorial: '))

contagem = 1
for c in range(contagem, num + 1):
    contagem *= c
    print('x',c,end=' ')
print('=',contagem)

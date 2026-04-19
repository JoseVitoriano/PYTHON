'''Programa de analise de numeros'''

print('Programa de analise de maior e menor entre numeros, Vamos la?')
print('~' * 80)

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

print('~' * 80)

if num1 > num2 and num1 > num3:
    print('O maior numero entre os numeros informados e: {}.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior numero entre os numeros informados e: {}'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O maior numero entre os numeros informados e: {}'.format(num3))
else:
    print('Os numeros sao iguais...')
    
    
if num1 < num2 and num1 < num3:
    print('O menor numero entre os numeros informados e: {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor numero entre os numeros informados e: {}'.format(num2))
elif num3 < num1 and num3 < num2:
    print('O menor numero entre os numeros informados e: {}'.format(num3))
else:
    print('Os numeros sao iguais...')

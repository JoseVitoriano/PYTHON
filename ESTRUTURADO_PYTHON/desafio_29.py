'''Programa comparando numeros'''

print('Programa analisara dois numeros, Vamos la ?')
print('~' * 80)

num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

if num1 > num2:
    print('O primeiro numero e MAIOR {}.'.format(num1))
elif num1 < num2:
    print('O segundo numero e MAIOR {}'.format(num2))
else:
    print('Os numeros sao iguais...')
    
    
'''Programa de Par ou Impar'''

print('Programa analisara se um numero e PAR ou IMPAR, Vamos la ?')
print('~' * 80)

num = int(input('Informe um numero inteiro: '))

print('~' * 80)

analise = num % 2

if analise == 0:
    print('O numero informado e PAR...')
    
else:
    print('O numero informado e IMPAR...')
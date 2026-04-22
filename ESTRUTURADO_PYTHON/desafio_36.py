'''Calculadora'''

from time import sleep

print('Programa de tabuada de multiplicacao, Vamos la ?')
print('~' * 80)

num = int(input('Informe a tabuada que deseja analisar: '))
print('Analisando...')
sleep(5)
print('Tabuada de {}.'.format(num))

for c in range(1, 11):    
    print('{} x {} = {}'.format(num, c, (num * c)))
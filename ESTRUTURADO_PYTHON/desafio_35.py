'''Programa de contagem de numeros pares'''

from time import sleep

print('Programa analisara a contagem de numeros pares entre numeros, Vamos la ?')
print('~' * 80)

num = int(input('Informe o limite de analise de numeros pares: '))
print('Analisando...')
sleep(5)

for c in range (0, num, 2):
    par = c % 2
    print(c)
'''Programa de analisa a soma de total os numeros multiplos de tres'''

from time import sleep

print('Programa que analisa os multiplos de tres, Vamos la ?')
print('~' * 80)

print('Analisando...')
sleep(5)

soma = 0
for c in range(1, 501, 2):
    print(c)
    if c % 3 == 0:
        soma += c
print('A soma dos valores que sao multiplos de 3 sao: {}'.format(soma))
        
    
    
    
    
    
    
    

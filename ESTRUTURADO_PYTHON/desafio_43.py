'''Programa que possui um flag de parada'''

from time import sleep

print('Programa possui um flag de parada, Vamos la ?')
print('~' * 80)

soma = cont = 0

while True:
    
    num = int(input('Informe um numero: '))
    
    if num  == 999:
        break
    
    cont += 1
    soma += num

print('~' * 80)

print('Carregando resultado...')
sleep(5)

print('~' * 80)    

print(f'Voce digitou {cont} valores.')
print(f'A soma total dos valores sao : {soma}.')
    
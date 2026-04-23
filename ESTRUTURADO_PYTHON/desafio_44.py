'''Programa jogo de Impar e Par'''

from random import randint
from time import sleep

print('Programa jogo de impar ou par contra a maquina, Vamos la ?')
print('~' * 80)

vitorias = cont = 0
while True:
    
    num = int(input('Informe um numero '))
    
    cpu = randint(1, 20)
    cpu_analise = cpu % 2
    
    
    jogador = num % 2
    
    cont += 1
    
    if jogador == cpu_analise:
        
        print('EMPATARAM, TENTE NOVAMENTE.')
    
    elif jogador > cpu_analise:
        
        print('VOCE PERDEU!, TENTE NOVAMENTE.')
        print('Encerrado o jogo...')
        sleep(5)
        print('Jogo encerrado.')
        break
    
    elif jogador < cpu_analise:
        
        print('VOCE VENCEU!, PARABENS.')
        vitorias += 1

print('~' * 80)
print(f'Voce jogou {cont} rodadas, Parabens.')
print(f'Quantidades de vitorias seguidas {vitorias}.')
    
    

    
    
    
    

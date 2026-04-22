'''Programa de adivinhação'''

from time import sleep
from random import randint

print('Programa jogo de adivinhacao, Vamos la ?')
print('~' * 80)

cpu = randint(1, 10)


print('Ola jogador preparado para o jogo, Vamos la!')
print('Pensando em um numero...')
sleep(5)
print('Ja sei! Sera que voce vai acertar ?')
print('~' * 80)

acertou = False

palpites = 0

while not acertou:
       
    jogador = int(input('Informe seu numero: '))
    palpites += 1
    
    
    if cpu == jogador:
        acertou = True
        
print('Voce precisou de {} tentativas para me vencer, Parabens.'.format(palpites))
    
    


        
    
    
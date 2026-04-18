'''Programa que simula um jogo de advinhação'''

print('Programa que simula o jogo de advinhacao de maquina, Vamos la ?')
print('~' * 80)

'''Importação da biblioteca'''

from random import randint
from time import sleep

'''Variaveis'''

cpu = randint(1,10)

print('Olá Jogador , preparado estou pensando em um numero...')
print('Carregando...')
sleep(9)
print('Pronto já sei, informe o seu será que voce vai acertar o que eu pensei ?...')

print('~' * 80)

jogador = int(input('Sua vez !, Informe um número inteiro: '))

print('~' *80)

'''Resultado'''

if jogador == cpu:
    print('Parabens, jogador voce me venceu !')
else:
    print('Nao foi dessa vez, eu venci voce !')
    





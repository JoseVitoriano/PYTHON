'''Programa simula um jogo JOKEPO'''

import random
from time import sleep

print('Programa que simula um jogo de JOKEPO, Vamos la ?')
print('~' * 80)

'''1- Papel
   2- tesoura
   3- Pedra'''

lista = [1, 2, 3]

cpu = random.choice(lista)

print('''        
     1. Papel...
     2. Tesousa...
     3. Pedra...
      
    ''')

escolha = int(input('Escolha sua opcao: '))

print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO !')
sleep(2)
print('Resultado...')
print('~' * 80)

if escolha == 1 and cpu == 2:
    print('CPU VENCEU - Tesoura corta Papel...')
elif escolha == 1 and cpu == 3:
    print('VOCE VENCEU - Papel embulha Pedra...')
elif escolha == 1 and cpu == 1:
    print('EMPATE !')
elif escolha == 2 and cpu == 1:
    print('VOCE VENCEU - Tesoura corta Papel...')
elif escolha == 2 and cpu == 2:
    print('EMPATE !')
elif escolha == 2 and cpu == 3:
    print('CPU VENCEU - Pedra quebra Tesoura...')
elif escolha == 3 and cpu == 1:
    print('CPU VENCEU - Papel embulha Pedra...')
elif escolha == 3 and cpu == 2:
    print('VOCE VENCEU - Pedra quebra Tesoura...')
elif escolha == 3 and cpu == 3:
    print('EMPATE !')
else:
    print('Escolha uma opcao valida.')


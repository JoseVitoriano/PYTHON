'''Programa de contagem regressiva'''

from time import sleep

print('Programa realizara uma contagem regressiva, Vamos la ?')
print('~' * 80)

print('''
      
      1. Realizar a contagem regressiva...
      2. Sair...
      
    ''')

escolha = int(input('Informe a opcao desejada: '))

if escolha == 1:
    
    for c in range(10, 0, -1):
        print(c)
        sleep(2)
    print('BOOOOOOOOM!')
    
        
else:
    print('Saindo do sistema...')
    sleep(3)
    print('Programa finalizado.')
        
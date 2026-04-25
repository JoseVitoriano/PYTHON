'''Programa de analise de numeros'''

from time import sleep

print('Programa analisa uma sequencia de numeros, Vamos la ?')
print('~' * 80)

while True: 
    
    print('~' * 80)
        
    números = list()
        
    n = int(input('Informe o numero desejado: '))
        
    if n not in números:
        números.append(n)
        print('Valor cadastrado com sucesso!')
    else:
        print('Valor duplicado, nao irei cadastrar...')            
    r = str(input('Deseje continuar [S/N]: '))
            
    if r in 'Nn':
        break

print('Programa encerrado.')
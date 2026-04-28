'''Programa de Contagem'''

from time import sleep

def contador (inicio, fim, passo):
    cont = 0
    for cont in range(inicio, fim, passo):        
        print(f'{cont}', end=' ')
        
        
        
        
def contador_text(inicio, fim, passo):
    print('~' * 50)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}.')
    contador(inicio=inicio, fim=fim, passo=passo)
    print()
    print('~' * 50)
    




inicio = int(input('Informe o primeiro numero: '))
fim = int(input('Informe o ultimo numero: '))
passo =int(input('Informe o passo: '))

contador_text(inicio=inicio, fim=fim, passo=passo)

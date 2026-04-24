'''Programa que analisa uma Tupla'''

print('Programa realizara uma analise de uma Tupla, Vamos la?')

from time import sleep

while True:
    
    num_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','deseseis','desesete','dezoito','dezenove', 'vinte')   
    
    
    print('''
          
          1. Analisando a Tupla...
          2. Sair do programa...    
        
        ''')
    
    selecao = int(input('Informe a opcao desejada: '))
    
    print('~' * 80)
    print('Carregando selecao...')
    sleep(6)
    
    if selecao == 1:
        
        num = int(input('Digite um numero entre [0 a 20]: '))
        print(f'O numero selecionado em extenso e: {num_extenso[num]}')
        print('~' * 80)
        
    else:
        
        print('Finalizando o programa...')
        sleep(6)
        break
    
print('Programa finalizado com sucesso!')

        
        
        
        
    
    
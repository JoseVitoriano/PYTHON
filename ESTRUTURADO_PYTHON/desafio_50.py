'''Programa de analise de lista'''

from time import sleep

 
print('Programa analisara informacoes em uma lista, Vamos la ?')
print('~' * 80)

while True:
    
    print('''
          
          1. Realizar o cadastro...
          2. Sair do programa...
          
        ''')
    
    selecao = int(input('Informe a opcao desejada: '))
    
    if selecao == 1:
        
        lista = []
        maior = 0
        menor = 0
        
        for c in range(0,5):
            
            lista.append(int(input(f'Digite o numero desejado para a posicao {c}: ')))  
            
            if c == 0:
                
                maior = menor = lista[c]
                
            else:
                if lista[c] > maior:
                    maior = lista[c]
                if lista[c] < menor:
                    menor = lista[c]
            
        print('~' * 80) 
        print('Carregando analise...')
        sleep(5)       
            
        print(f'O Maior valor digitado e: {maior}.')
        print(f'O Menor valor digitado e: {menor}.')
        
    else:
        
        print('~' * 80)
        print('Encerrando o programa...')
        sleep(5)
        break

print('Programa encerrado com sucesso !')
            
        
        
            
       
            
        
            
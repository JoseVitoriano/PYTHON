'''Contando Vogais'''

print('Programa analisara uma Tupla de palavras, Vamos la ?')
print('~' * 80)

from time import sleep

palavras = ('Karine', 'Amor', 'Jose', 'Pai', 'Mae','Julia','Jessica','Oliver','Joabe')

print('~~~~~~~~~~~ Programa Palavras Aleatorias ~~~~~~~~' )


while True:
    
    print('~' * 80)    
    selecao = str(input('Deseja iniciar a analise das palavras [S/N]: ')).strip().upper()    
    
    
    if selecao == 'S':
        
        print('~' * 80)
        print('Carregando a analise...')
        sleep(5)
                
        for p in palavras:
            
            print(f'\nNa palavra {p} temos as vogais: ',end='')
            
            for letra in p:
                
                if letra.lower() in 'aeiou':
                    
                    print(letra, end='')
                    
    if selecao == 'N':
        
        print('~' * 80)
        print('Encerrando o programa...')
        sleep(5)
        break
    
print('Programa encerrado com sucesso !')
        



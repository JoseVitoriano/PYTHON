'''Analisando o programa de matriz 53'''

print('Melhorando o programa realizado 53, Vamos la?')
print('~' * 80)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

spar = maior = scol = 0


for l in range(0, 3):
    for c in range(0, 3):
        matriz [l] [c] = int(input(f'Informe um valor das posicoes {[l]} e {[c]}: '))
        
print('~' * 80)

for l in range(0, 3):
    for c in range(0, 3):
        
        print(f'{matriz [l] [c] :^5}', end='')
        
        if matriz [l][c] % 2 == 0:
            spar += matriz[l][c]         
    
    print('')    
        
print('~' * 80)
print(f'O resultado de todos os numeros PARES sao: {spar}.')

for l in range(0, 3):
    
    scol += matriz[l][2]
    
print(f'A soma dos valores da terceira coluna e: {scol}.')


for c in range(0, 3):
    
    if c == 0:
        
        maior = matriz [1][c]
        
    elif matriz [1][c] > maior:
        
        maior = matriz[1][c]
      
print(f'O maior numero da coluna 1 e: {maior}.')  

    
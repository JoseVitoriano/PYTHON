'''Programa de analise de valores'''

print('Programa de analise de numeros')

soma = quant = maior = menor = media = 0
resp = 'S'
while resp in 'Ss':
    
    num = int(input('Informe um valor'))
    quant += 1
    soma += num
    
    resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
        
print('~' * 80)
print('A media dos valores informados e: {}.'.format((soma / quant)))
print('O maior valor foi {} e o menor valor {}.'.format(maior, menor))
    
    
    
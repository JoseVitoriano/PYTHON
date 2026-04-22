'''Programa de analise de fibonaci'''

print('Programa de progressao aritmetica, Vamos la ?')
print('~' * 80)

print('Sequencia de fibonaci')

num = int(input('Informe a quantidade de termos para analise: '))
t1 = 0
t2 = 1
print('~' * 80)

print('{} - {}'.format(t1, t2), end='')

contador = 3

while contador <= num:
    
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
        
print(' Analise concluida...')
    
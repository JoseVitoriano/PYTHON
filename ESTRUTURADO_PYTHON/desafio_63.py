'''Analise de numeros para conhecer os fatoriais'''

print('Programa analisarar o numero fatorial de um numero, Vamos la ?')

def fatorial(num, show=False):
    
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f += c
    return f
        
        
# Programa Principal

numero = int(input('Informe um numero para analisarmos o seu fatorial: '))

print(fatorial(numero, show=False))        
        
        


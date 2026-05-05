'''Programa de analise de tratamento de erro'''


def leiaInt(msg):
    
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um numero valido...\033[m')
            continue
        else:
            return n
        
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor digite um numero valido...\033[m')
        else:
            return n
        
        
# Programa pricipal

n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um valor em real: ')

print(f'O numero no formato inteiro foi {n1} e em real foi {n2}.')
                
        
            
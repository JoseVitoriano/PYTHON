from funcao import fatorial, dobro

num = int(input('Informe um numero para analise: '))
fat = fatorial(num)
print(f'O fatorial do numero informado {num} e {fat:.2f}')
print(f'O dobro do numero informado {num} e {dobro(num)}')
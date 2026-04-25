'''Programa com Matriz'''

print('Programa que analisa a Matriz, Vamos la ?')
print('~' * 80)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for l in range(0, 3):
    for c in range(0, 3):
        matriz [l] [c] = int(input(f'Informe um valor das posicoes {[l]} e {[c]}: '))
        
print('~' * 80)

for l in range(0, 3):
    for c in range(0, 3):
        
        print(f'{matriz [l] [c] :^5}', end='')
        
    print()

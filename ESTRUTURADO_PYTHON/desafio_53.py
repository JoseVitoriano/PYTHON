'''Criando uma Matriz'''

print('Programa que analisa e cadastra as informacoes em Matriz, Vamos la ?')
print('~' * 80)

peca = []
bd = []
soma = 0

while True:
    
    peca.append(int(input('Informe o codigo da peca: ')))
    peca.append(str(input('Informe a descricao da peca: ')).strip().upper())
    peca.append(float(input('Informe o valor da peca: ')))
    
    bd.append(peca[:])
    peca.clear()
    
    print('~' * 80)
    
    resp = str(input('Deseja continuar [S/N]: ').strip().upper())
    
    if resp in 'Nn':
        break
    
    
print('Programa Finalizado...\nTabela 3X3...')


for p in bd:
    
    soma += p[2]
    
    print(f'Codigo: {p[0]} | Descricao: {p[1]} | Valor da paca: R${p[2]}. ')
    print('-' * 80)
print(f'A soma total da coluna de preco e: {soma}.')
    

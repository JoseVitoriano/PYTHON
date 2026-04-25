'''Programa que analisa duas listagens'''

print('Programa que analisam duas listagem, Vamos la?')
print('~' * 80)

dados = []
bd = []

pesomaior = pesomenor = 0

while True:
    
    dados.append(str(input('Informe o nome: ')).strip().upper())
    dados.append(float(input('Informe o peso: ')))
    
    if len(bd) == 0:
                
        pesomaior = pesomenor = dados[1]
    else:
        
        if dados[1] > pesomaior:
            pesomaior = dados[1]
            
        if dados[1] < pesomenor:
            pesomenor = dados[1]       
    
    bd.append(dados[:])
    dados.clear()    
    
    print('~' * 80)
    
    resp = str(input('Deseja continuar [S/N]: '))
    
    print('~' * 80)
    if resp in 'Nn':
        
        break
    
print('~' * 80)
print(f'As informacoes no banco de dados foram: {bd}.')
print(f'O total de pessoas cadastradas foram: {len(bd)}')
print(f'O maior peso foi {pesomaior} kg, Peso de ', end='')

for p in bd:
    
    if p[1] == pesomaior:
        
        print(f'[{p[0]}]', end='')

print()
print(f'O menor peso foi {pesomenor} kg, Peso de ', end='')

for p in bd:
    
    if p[1] == pesomenor:
        
        print(f'[{p[0]}]',end='')
    
    
    
    
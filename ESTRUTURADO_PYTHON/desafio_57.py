'''Programa que analisa o contrato'''

print('Programa a analisara o perfil de trabalho de um colaborador, Vamos la ?')
print('~' * 80)

cadastro = dict()

cadastro['nome'] = str(input('Informe o Nome do Colaborador: ').strip().upper())
cadastro['ano'] = int(input('Informe o ano de Nascimento:'))
cadastro['carteira'] = int(input('Carteira de Trabalho (0 nao tem): '))

if cadastro['carteira'] == 0:
    
    for k, v in cadastro.items():
        
        print(f'{k} tem o valor {v}.')
        
elif cadastro['carteira'] >= 1:
    
    cadastro['contratacao'] = int(input('Informe o Ano de Contratacao: '))
    cadastro['salario'] = float(input('Informe o seu salario: R$ '))
    cadastro['servico'] = 65 - (cadastro['contratacao'] - cadastro['ano'])
    
    for k, v in cadastro.items():
        
        print(f'{k} tem o valor {v}.')
        
else:
    
    print('Informe dados validos...')
    
    
    


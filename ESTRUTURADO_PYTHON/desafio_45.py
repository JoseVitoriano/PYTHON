'''Programa de cadastro de colaboradores'''
from time import sleep

print('Programa de cadastro de pessoas, Vamos la ?')
print('~' * 80)

pessoas = masculino = feminino = 0 

while True:
    
    pessoas += 1
    
    nome = str(input('Digite o nome: ')).strip().upper()
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    idade = int(input('Informe a idade: '))
    print('~' * 80)
    print('Efetuando o cadastro...')
    sleep(5)
    print('Cadastro efetuado com sucesso.')
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    print('~' * 80)    
    
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        feminino += 1
    
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    
print(f'Quantidades de pessoas cadastradas: {pessoas}.\nQuantidades do sexo feminino: {feminino}.\nQuantidade do sexo masculino:{masculino}.')

    

    
    
    
        
    
    

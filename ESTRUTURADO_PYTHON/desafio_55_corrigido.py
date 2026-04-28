'''Correção do desafio 55'''

aluno = dict()

aluno['nome'] = str(input('Informe o nome do aluno: ').strip().upper())
aluno['media'] = float(input(f'Informe a media de {aluno["nome"]}: '))

if aluno['media'] >= 7.0:
    
    aluno['situacao'] ='Aprovado'

elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
    
else:
    aluno['situacao'] = 'Reprovado'
    
print('~' * 80)

print(f'BD: {aluno}')

print('~' * 80)

for k, v in aluno.items():
    
    print(f'{k} e igual {v}')



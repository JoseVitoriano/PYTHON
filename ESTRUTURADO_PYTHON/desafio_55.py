'''Programa de analise de notas dos alunos'''

print('Programa de analise de media, Vamos la ?')
print('~' * 80)

dados = {}
alunos = []

for c in range(0, 1):
    
    dados['nome'] = str(input('Informe o nome: ').strip().upper())
    dados['media'] = float(input('Informe a media: '))
    
    alunos.append(dados.copy())
    
resultado = dados["media"]

print('~' * 80)

for e in alunos:
    for n, m in e.items():
        
        print(f'A media de {dados["nome"]} e igual a {dados["media"]}...')
        
    if resultado >= 6:
        print('O aluno esta Aprovado...')
    else:
        print('O aluno esta Reprovado...')
            
        



    



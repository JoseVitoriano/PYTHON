'''Programa de analise de string'''

print('Programa de analise de string, Vamos la ?')
print('~' * 80)

nome = str(input('Informe o nome desejado para analise: ').strip().upper())

print('~' * 80)

'''Variaveis'''

analise_nome = nome.split()
primeiro_nome = analise_nome[0]
ultimo_nome = analise_nome[4]

'''Resultado'''

print('Resultado.\nNome completo: {}.\nPrimeiro nome: {}.\nÚltimo nome: {}.\n'.format(nome, primeiro_nome,ultimo_nome))

'''Programa de analise de nome'''

print('Programa de analise de nome de uma pessoa, Vamos la ?')
print('~' * 80)

nome = str(input('Informe o nome desejado para analise: ').strip().upper())

print('~' * 80)

'''Variaveis'''

qtde_vezes = nome.count('A')
incio_nome = nome.find('A')
fim_nome = nome.rfind('A')

'''Resultado'''

print('Resultado.\nQuantas vezes a letra (a) aparece: {}.\nA letra (a) aparece em qual posicao de inicio: {}.\nA letra (a) aparece em qual posicao de fim; {}.'.format(qtde_vezes, incio_nome, fim_nome))

'''Programa de analise do nome da cidade'''

print('Programa de analise do nome da cidade se contem SANTO, Vamos la ?')
print('~' * 80)

cidade = str(input('Infome o nome da cidade que deseja analisar: ').strip())

print('~' * 80)

'''Variaveis'''

nome_cidade = cidade.split()
resultado_cidade = nome_cidade[0]


'''Resultado'''

if resultado_cidade == 'SANTO' or 'santo' or 'Santo':
    print('Nome da Cidade encontrado')
else:
    print('Não encontrado')
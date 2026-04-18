'''Programa de analise do nome de uma pessoa'''


print('Programa de analise de nome de uma pessoa, Vamos la ?')
print('~' * 80)

nome = str(input('Informe o seu nome completo: ').strip().upper())

print('~' * 80)

'''Variaveis'''

analise_nome = nome.find('SILVA')

'''Resultado'''


if analise_nome >= 1:
    
    print('Possui registro nesse nome com SILVA !')
    
else:
    
    print('Não possui registro de SILVA neste nome !')
'''Programa ano Bissexto'''

print('Programa analisara se o ano informado e um ano BISSEXTO ou NAO, Vamos la ?')
print('~' * 80)

ano = int(input('informe um ano para analise: '))

analise = ano % 4

if analise == 0:
    print('O ano informado e BISSEXTO!')
    
else:
    print('O nao informado NAO e BISSEXTO!')
    
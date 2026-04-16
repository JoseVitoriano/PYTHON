'''Programa que analisa a média aritmetica'''

print('Analisaremos a media de notas do aluno informado...')
print('~' * 70)
print('Analisaremos o primeiro Semestre...')
print('~' * 70)

'''Variaveis'''
nome = str(input('Informe o nome do aluno: '))
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))

media_aritmetica = (nota1 + nota2 + nota3 + nota4) / 4

'''Resultado'''
print('~' * 70)
if media_aritmetica >= 6.0 :
    print('Resultado: A sua média foi: {:.2f}.\nParabens {} voce esta APROVADO!'.format(media_aritmetica, nome))
elif media_aritmetica < 6.0:
    print('Resultado: A sua média foi: {:.2f}.\nInfelizmente {} voce esta REPROVADO!'.format(media_aritmetica, nome))
else: 
    print('Programa encerrado !')



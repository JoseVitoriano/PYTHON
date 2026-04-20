'''Programa que analisa o perfil da delegação'''

from time import sleep

print('Programa que analisa o perfil da delegação de natacao, Vamos la?')
print('~' * 80)

idade = int(input('Informe sua idade, atleta: '))

print('Analisando o seu perfil...')
sleep(5)
print('~' * 80)

if idade <= 9:
    print('Resultado:\nSua categoria e: MIRIM...')
elif idade > 9 and idade <= 14:
    print('Resultado:\nSua categoria e: INFANTIL...')
elif idade > 14 and idade <= 19:
    print('Resultado:\nSua categoria e: JUNIOR...')
elif idade > 19 and idade <= 20:
    print('Resultado:\nSua categoria e: SENIOR...')
else:
    print('Resultado:\nSua categoria e: MASTER...')
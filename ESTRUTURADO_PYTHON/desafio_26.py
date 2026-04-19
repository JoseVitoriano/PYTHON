'''Programa de analise os perfils de salarios'''

from time import sleep

print('Programa que analisa os perfis de salarios e calcula o percentual de aumento, Vamos la?')
print('~' * 80)

salario = float(input('Informe o seu salario: R$ '))
salario_superior = 0.10
salarios_inferior = 0.15
print('~' * 80)
print('Analisando, Aguarde ...')

sleep(9)
print('Analise concluida.')
print('~' * 80)

if salario >= 1250.0:
    print('Salario analisado: R$ {:.2f}.\nPercentual pelo perfil: {:.3f}%.\nAumento: R$ {:.2f}.\nNovo Salario: R$ {:.2f}'.format(salario, salario_superior, ((salario * 10)/100),(salario + ((salario * 10)/100))))

else:
    print('Salario analisado: R$ {:.2f}.\nPercentual pelo perfil: {:.3f}%.\nAumento: R$ {:.2f}.\nNovo Salario: R$ {:.2f}.'.format(salario, salarios_inferior,((salario * 15)/100), (salario + ((salario * 15)/100))))
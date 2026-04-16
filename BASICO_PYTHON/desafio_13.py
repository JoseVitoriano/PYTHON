'''Programa de analise salarial'''

print('Programa de analise salarial, Vamos la ?')
print('~' * 80)

'''Variaveis'''

salario = float(input('Informe seu salario atual R$: '))
aumento = float(input('Informe o percentual de aumento estipulado %: '))

percentual_final = aumento / 100

aumento_salarial = salario + (salario * percentual_final)
percentual_aumento = salario * percentual_final

'''Resultado'''

print('~' * 80)

print('Resultado:\nSalario atual informado: {:.2f}R$.\nPercentual informado: {:.1f}%.\nAumento definido: {:.2f}R$.\nNovo salario base: {:.2f}R$...'. format(salario, aumento, percentual_aumento, aumento_salarial))
print('Programa encerrado...')
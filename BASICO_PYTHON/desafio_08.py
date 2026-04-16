'''Programa de conversão de metragem'''

print('Analisaremos um numero em metros e analise os metodos de comprimento, Vamos la?')
print('~' * 80)

'''Variaveis'''
m = float(input('Informe a metragem em metros para analise... : '))

centimetros = m * (10 * 10)
milimetros = m * (10 * 10 * 10)

'''Resultado'''
print('~' * 80)
print('Apos a analise do valor informado {}mm, temos o seguinte resultado....\nCentimetros: {}.\nMilimetros: {}.'.format(m, centimetros, milimetros))

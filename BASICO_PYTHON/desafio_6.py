'''Programa de analise doblo, triplo e potencia'''
print('Analise o Dobro, Triplo e a Potencia do numero inteiro informado, Vamos la ?')
print('-' * 60)
num = int(input('Informe um numero inteiro: '))

'''Calculo das variaveis'''
dobro = num * 2
triplo = num * 3
potencia = pow(num,2)

'''Resultado'''

print('O resultado da analise do numero e:\nDobro: {}.\nTriplo: {}.\nPotencia: {}.'.format(dobro, triplo, potencia))


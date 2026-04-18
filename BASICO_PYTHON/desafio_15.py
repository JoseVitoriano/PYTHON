'''Programa de analise Unidades'''

print('Programa de analise de unidades, dezenas, centenas e milhar, Vamos la ?')
print('~' * 80)

num = input('Informe um numero de [0 a 9999]: ')

'''Variaveis'''

unidade = num[3:4]
dezena = num[2:3]
centena = num[1:2]
milhar = num[0:1]

print('~' * 80)

'''Resultado'''
print('Resultado.\nUnidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}.'.format(unidade, dezena, centena, milhar))
print('Programa Finalizado com Sucesso')
'''Programa de calculo de metragem de tinta'''

print('Programa realizara um suporte para a equipe de pintura, Vamos la ?')
print('~' * 80)

'''Variaveis'''

comprimento = float(input('Informe o comprimento da parede [mm]: '))
altura = float(input('Informe a largura da parede [mm]: '))

analise_area = comprimento * altura
analise_tinta = (comprimento * altura)  / 2

'''Resultado'''
print('~' * 80)
print('Resultado:\nComforme a analise do comprimento {:.2f}mm e altura {:.2f}mm ...\nSabemos que sua area quadrada e igual a {:.2f}m².\nDessa forma a quantidade de tinta necessarios para a conclusao da pintura desta parede e {:.2f}litros.'.format(comprimento, altura, analise_area, analise_tinta))
'''Programa que calcula o IMC'''

from time import sleep

print('Programa que calcula o IMC, Vamos la ?')
print('~' * 80)

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
calculo = peso/(altura * altura)
print('~' * 80)
print('Analisando seu IMC...')
print('Aguarde o resultado...')
sleep(5)
print('~' * 80)


'''Variavel'''

if calculo <= 18.5:
    print('Resultado:\nIMC: {:.1f}.\nClassificao: Abaixo do peso...'.format(calculo))
elif calculo > 18.5 and calculo <= 25.0:
    print('Resultado:\nIMC {:.1f}.\nClassificacao: Peso ideal...'.format(calculo))
elif calculo > 25.0 and calculo <= 30.0:
    print('Resultado:\nIMC: {:.1f}.\nClassificacao: Sobre peso... '.format(calculo))
elif calculo > 30.0 and calculo <= 40.0:
    print('Resultado:\nIMC: {:.1f}.\nClassificacao: Obesidade...'.format(calculo))
else:
    print('Resultado:\nIMC: {:.1f}.\nClassificacao: Morbida...')    



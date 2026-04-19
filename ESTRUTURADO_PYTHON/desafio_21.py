'''Programa que simula penalidade de velocidade'''

print('Programa que simula, penalidades graves de velocidade, Vamos la ?')
print('~' * 80)

'''Variaveis'''

velocidade =  int(input('Informe a velocidade percorrida km/h: '))
limite = 80

'''Resultado'''

if velocidade > limite:
    
    diferenca = (velocidade - limite) * 7
    print('Excedido o limite de velocidade, voce foi penalizado e o valor da multa e R$ {:.2f}.'.format(diferenca))
    
else: 
    
    print('Limite nao excedido, voce esta liberado.')
    
    
    
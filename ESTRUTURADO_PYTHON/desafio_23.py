'''Programa de analise de distancia e preço'''

print('Programa analisar o ticket a ser pago pela distancia percorrida, Vamos la ?')
print('~' * 80)

local = str(input('Informe o seu destino: ').strip().upper())
distancia = float(input('Informe a quantidade de km a ser percorrido: '))

print('~' * 80)
maior_km = 0.45
menor_km = 0.50

if distancia > 200:
    print('Destino: {}.\nQuilometragem percorrida: {}.\nTicket: R$ {:.2f}.'.format(local, distancia, (distancia * maior_km)))
    
else:
    print('Destino: {}.\nQuilometragem percorrida: {}.\nTicket: R$ {:.2f}.'.format(local, distancia, (distancia * menor_km)))
    
    
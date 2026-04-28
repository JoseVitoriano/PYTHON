'''Analisando valores'''

def analise(lst):
    print('Analisando os valores passados...')
    print(f'{lst} Foram informados {len(lst)} valores ao todo.')
    
    pesomaior = 0
    
    if len(lst) == 0:
        pesomaior = lista['num']
    else:
        if lista['num'] > pesomaior:
            pesomaior = lista['num']
            print(f'O maior valor informado e {pesomaior}...')




lista = dict()
geral = list()

for c in range(0, 10):
    lista ['num'] = int(input('Informe um numero: '))
    
    geral.append(lista.copy())
    
analise(lst=geral)
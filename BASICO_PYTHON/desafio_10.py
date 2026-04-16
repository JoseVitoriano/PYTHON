'''Programa de conversão de moeda'''

print('Neste programa realizaremos uma conversao de valores de moeda, Vamos la ?')
print('~' * 80)

'''Variaveis'''

print('''
      
    1. U$$ para R$...
    2. R$ para U$$...      
      
    ''')

selecao = int(input('Informe a opcao desejada [1 ou 2]: '))

if selecao == 1:
    
    print('A opcao selecionada foi {}(U$$ para R$)...'.format(selecao))
    dolar = float(input('Informe o valor em U$$_Dolar: '))
    valor_dolar = 4.99
    print('~' * 80)
    print('Resultado:\nR$_Reais disponiveis para compra: {:.2f}R$.'.format(dolar / valor_dolar))

elif selecao == 2:
    
    print('A opcao selecionada foi {}(R$ para U$$)...'.format(selecao))
    real = float(input('Informe o valor em R$_Real: '))
    valor_real =  0.200
    print('~' * 80)
    print('Resultado:\nU$$_Dolares disponiveis para compra: {:.2f}U$$.'.format(real * valor_real))
    
else:
    
    print('Programa encerrado, selecione uma das opcoes validas...')
    
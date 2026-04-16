'''Programa de analise de salario com desconto'''

print('Neste programa analisaremos os descontos de produtos, Vamos la ?')
print('~' * 80)

'''Variaveis'''

produto = float(input('informe o preco do produto: '))
desconto = float(input('Informe o percentual de desconto: '))

desconto_final = desconto / 100

print('''
    
    Selecione a opcao desejada...
    
    1. Adicionar o desconto no produto...
    2. Desconsiderar o desconto estipulado...  
      
    ''')

selecao = int(input('Informe a opcao desejada: '))

if selecao == 1:
    print('~' * 80)
    print('O desconto estipulado foi de {:.1f}%.\nCom isso desconto estipulado no produto e: {:.2f}R$.\nPreco final do produto e: {:.2f}R$ ...'. format(desconto, (produto * desconto_final), (produto - (produto * desconto_final))))
    
elif selecao == 2:
    print('~' * 80)
    print('O valor do produto sem desconto e: {:.2f}'. format('produto'))
    
else:
    print('Programa finalizado, selecione uma opcao valida....')
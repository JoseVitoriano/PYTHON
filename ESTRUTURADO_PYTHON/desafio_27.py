'''Programa de analise de credito'''

from time import sleep

print('Programa analisa a situacao de credito imobiliario, Vamos la ?')
print('~' * 80)

print('''
      
      Menu do Programa\n 1. Analise de credito...\n 2. Sair do programa...      
      
    ''')

opcao = int(input('Informe a opcao desejada: '))
print('Carregando...')
sleep(5)

print('~' * 80)

if opcao == 1:
        
    valor_casa = float(input('Informe o valor da casa: R$ '))
    salario = float(input('Informe o rendimento mensal: R$ '))
    meses = int(input('Informe quantidade de meses: '))
    calculo_casa = valor_casa / meses
    calculo_salario = (calculo_casa / salario) * 100
    print('Analisando...')
    sleep(5)
    
    if calculo_salario >= 30:
        
        print('Resultado:\nConforme analisa a prestacao da casa ultrapassa 30%, CREDITO NEGADO!'.format(calculo_salario))
        
    else:
        
        print('Resultado:\nConforme analise a prestação da casa não ultrapassa 30%, CREDITO APROVADO!'.format(calculo_salario))


elif opcao == 2:
    print('Finalizando programa...')
    sleep(5)
    print('Voce saiu do programa.')
    
    

        
    
    
    
    
    
    
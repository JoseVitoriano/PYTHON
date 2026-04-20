'''Programa simula o resultado de boletim'''

from time import sleep

print('Programa analisa as notas do aluno, Vamos la ?')
print('~' * 80)

print('''
      
    MENU DE ANALISE
    
    1. Bimestre...
    2. Trimestre...
    3. Nota Final...
      
    ''')

escolha = int(input('Informe a opcao desejada: '))
print('Carregando...')
sleep(5)
print('~' * 80)


if escolha == 1:
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    resultado = (nota1 + nota2) / 2
    print('Carregando resultado...')
    sleep(5)
    print('~' * 80)
    
    if resultado <= 5.0:
        print('Media abaixo ou igual a 5.0, REPROVADO !')        
    elif resultado > 5.1 and resultado <= 6.9:
        print('Media entre 5.0 e 6.9, RECUPERACAO ! ')    
    elif resultado >= 7.0:
        print('media superior ou igual a 7.0, APROVADO !')
    
elif escolha == 2:
    
    
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))
    resultado = (nota1 + nota2 + nota3) / 3
    print('Carregando resultado...')
    sleep(5)
    print('~' * 80)
    
    if resultado <= 5.0:
        print('Media abaixo ou igual a 5.0, REPROVADO !')        
    elif resultado > 5.1 and resultado <= 6.9:
        print('Media entre 5.0 e 6.9, RECUPERACAO ! ')    
    elif resultado >= 7.0:
        print('media superior ou igual a 7.0, APROVADO !')

elif escolha  == 3:
    
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))
    nota4 = float(input('Informa a quarta nota: '))
    resultado = (nota1 + nota2 + nota3 + nota4) / 4
    print('Carregando resultado...')
    sleep(5)
    print('~' * 80)
    
    if resultado <= 5.0:
        print('Media abaixo ou igual a 5.0, REPROVADO !')        
    elif resultado > 5.1 and resultado <= 6.9:
        print('Media entre 5.0 e 6.9, RECUPERACAO ! ')    
    elif resultado >= 7.0:
        print('media superior ou igual a 7.0, APROVADO !')
          
else:
    
    print('Informe uma opcao valida.')
    print('Encerrando...')
    sleep(5)
    print('Encerramento concluido.')

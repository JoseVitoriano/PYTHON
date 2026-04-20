'''Programa analisa o alistamento militar'''

from time import sleep

print('Programa simulara o prazo do alistamento militar, Vamos la ?')
print('~' * 80)

print('''      
    ESCOLHA O SEU GENERO
    
    1. Masculino
    2. Feminino   
    
    ''')

escolha = int(input('Escolha o seu genero: '))
print('~' * 80)

nome = str(input('Informe o seu nome: ').strip().upper())
idade = int(input('Informe sua idade: '))
ano = int(input('Informe o ano de seu nascimento: '))

'''Variaveis '''
if escolha == 1:
    print('~' * 80)
    print('Genero : Masculino...')
    print('Carregando analise, aguarde...')
    sleep(5)
    print('~' * 80)
    
    if idade < 18:
        print('Ola {}.\nIdade inferior para alistar.\nFalta {} anos, aliste-se no ano de {}...'. format(nome, (18 - idade),(2026 + (18 - idade))))

    elif idade == 18:
        print('Ola {}.\nEsta na hora de se alistar.\nFalta {} anos, aliste-se no ano de {}...'.format(nome, (18 - idade), (2026 + (18 - idade))))
    
    else:
       print('Ola {}.\nJa passou o tempo de alistamento.\nDeveria se alistar a {} anos atras, o seu ano para alistamento era {}....'.format(nome, (idade - 18), (2026 - (idade - 18))))

elif escolha == 2:
    print('Genero : Feminino...')
    print('Carregando analise, aguarde...')
    sleep(5)
    
    
    if idade < 18:
        print('Ola {}.\nIdade inferior para alistar.\nFalta {} anos, aliste-se no ano de {}...'. format(nome, (18 - idade),(2026 + (18 - idade))))

    elif idade == 18:
        print('Ola {}.\nEsta na hora de se alistar.\nFalta {} anos, aliste-se no ano de {}...'.format(nome, (18 - idade), (2026 + (18 - idade))))
    
    else:
       print('Ola {}.\nJa passou o tempo de alistamento.\nDeveria se alistar a {} anos atras, o seu ano para alistamento era {}....'.format(nome, (idade - 18), (2026 - (idade - 18))))
       
else:
    print('Escolha uma opcao valida!')
    print('Encerrando o programa...')
    sleep(5)
    print('Programa encerrado...')


'''Programa Tabela do Brasileirao'''

colocacao = 1

print('Programa que analisa a tabela do brasileirao serie A, Vamos la ?')
print('~' * 80)

from time import sleep

while True:
    
    tabela_brasileirao = ('Palmeiras','Flamengo','Fluminense','Sao Paulo','Bahia','Atletico PR','Coritiba','Bragantino','Botafogo','Vasco da Gama','Vitoria','Atletico MG','Gremio','Internacional','Santos','Cruzeiro','Corintians','Mirassol','Remo','Chapecoense')
    
    print('''
          
          1. Tabela do Brasileirao...
          2. Colocacao do seu Time...
          3. Zona da Libertadores...
          4. Zona da Sulamericana...
          5. Zona do Rebaixamento...
          6. Tabela do Brasileirao Organizada...
          7. Sair do Programa...
        
        ''')
    print('~' * 80)
    
    opcao = int(input('Informe a opcao desejada: '))
    
    if opcao == 1:
        
        print('~' * 80)
        print('Carregando a Tabela do Brasileirao, Aguarde...')
        sleep(5)
        print(f'Tabela: {tabela_brasileirao}')
    
    elif opcao == 2:
        
        print('~' * 80)
        time = str(input('Informe o nome do seu time: ')).strip()
        
        print('Analisando a colocacao do time...')
        sleep(5)
        
        analise = tabela_brasileirao.index(time)
        posicao_time = analise + 1
        
    
        print(f'O time informado e: {time}, sua posicao e na tabela e: {posicao_time}')
            
    elif opcao == 3:
        
        print('~' * 80)
        print('Carregando a zona da libertadores...')
        sleep(5)
        print(f'Neste momento os times na zona da libertadores sao: {tabela_brasileirao[0:5]}')
        
    elif opcao == 4:
        
        print('~' * 80)
        print('Carregando a zona da Sulamericana...')
        sleep(5)
        print(f'Neste momento os times na zona da Sulamericana sao: {tabela_brasileirao[5:11]}')
        
    elif opcao == 5:
        
        print('~' * 80)
        print('Carregando a zona do Rebaixamento...')
        sleep(5)
        print(f'Neste momento os times que estao na zona de Rebaixamento sao: {tabela_brasileirao[16:21]}')
        
    elif opcao == 6:
        print('~' * 80)
        print('Carregando a tabela do brasileirao alfanumerico...')
        sleep(5)
        print(f'Organizada [A a Z]: {sorted(tabela_brasileirao)}')
        
    else:
        print('~' * 80)
        print('Saindo do programa...')
        sleep(5)
        break
        
print('Programa encerrado com sucesso!')
        
        
         
       
        
        
        
    
    
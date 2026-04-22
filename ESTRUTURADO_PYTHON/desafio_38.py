'''Validação de cadastro'''
from time import sleep

print('Programa de validacao de cadastro, Vamos la ?')
print('~' * 80)

sexo = 'M, F'
r = 'S'
while sexo != 'M' or sexo != 'F' and r == 'S':
        
    sexo = str(input('Informe o sexo [M/F]: ').strip().upper())
    print('Efetuando o cadastro...')
    
    sleep(5)
    print('Cadastro efetuado com sucesso...')
    
    r = str(input('Deseja continuar o cadastro [S/N]: ').strip().upper())
    
    
    if r == 'S':
        
        sexo = str(input('Informe o sexo [M/F]: ').strip().upper())
        print('Efetuando o cadastro...')
        sleep(5)
        print('Cadastro efetuado com sucesso...')
        
    r = str(input('Deseja continuar o cadastro [S/N]: ').strip().upper())
    
    if r == 'N':
        
        print('Encerrando programa....')
        sleep(5)
        
        print('Programa encerrado.')
    
    
            
            
      
    

        
    
     
    
    
'''Validação de Senha'''

print('=========== VALIDACAO DE SENHA =========')
print('----------------------------------------')

print('01. CADASTRE SEU USUARIO')
print('02. TESTE DE VALIDACAO DE LOGIN')
print('03. SAIR DO PROGRAMA')

print('----------------------------------------')
escolha = int(input('Selecione sua escolha: '))
print('----------------------------------------')

if escolha == 1:
    usuario = str(input('Informe o seu usuario: '))
    senha = int(input('Informe sua senha: '))
    print('Cadastro salvo com sucesso!')
    
elif escolha == 2:
    informe_usuario = str(input('Informe o usuario: '))
    informe_senha = int(input('Informe sua senha: '))
    if informe_senha == 123456:
        print('Acesso liberado com sucesso !')
    else:
        print('Acesso ao sistema foi negado !')
    
elif escolha == 3:
    print('Programa finalizado')
    
else:
    print('Selecione a opcao correta !')
    



    
        
    


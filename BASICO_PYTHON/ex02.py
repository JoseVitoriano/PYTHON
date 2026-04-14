print('====== CADASTRO DE FUNCIONARIO =====')

nome = str(input('INFORME O SEU NOME COMPLETO: '))
print('=========================================')

idade = int(input('INFORME A SUA IDADE: '))
print('=========================================')

peso = float(input('INFORME O SEU PESO: '))
print('=========================================')

print('O RESULTADO DO CADASTRO E:\nSEU NOME E:{}\nSUA IDADE E: {}\nSEU PESO E: {:.2f}'.format(nome, idade, peso))
'''Programa que analisa o nome completo de uma pessoa'''

print('Programa que analisa o nome completo de uma pessoa, Vamos la ?')
print('~' * 80)

nome = str(input('Informe o seu nome completo: ').strip())

print('~' * 80)
print('''
      
      1. Nome Maiusculo
      2. Nome Minusculo
      3. Total de letras (Desconsiderando os espaços)
      4. Quantas letras no primeiro nome     
      
    ''')
print('~' * 80)
escolha = int(input('Escolha uma das opcoes [1 a 4]: '))

if escolha == 1:
    maiuscula = nome.upper()
    print('Nome convertido: {}.'.format(maiuscula))
    
elif escolha == 2:
    minuscula = nome.lower()
    print('Nome convertido: {}.'.format(minuscula))
    
elif escolha == 3:
    contagem = nome.split()
    resultado_contagem = ''.join(contagem)
    contagem_final = len(resultado_contagem)
    print('Total de Letras: {}.'.format(contagem_final))

elif escolha == 4:
    primeiro_nome = nome.split()
    lista_um = len(primeiro_nome [0])
    print('Quantidade de Letras no primeiro nome: {}.'.format(lista_um))
    
else:
    print('Programa encerrado, escolha uma opcao valida.')
    
'''programa de analise de votação'''

print('Programa analisa se a pessoa esta valida para votar, Vamos la ?')

from time import sleep

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f'A pessoa com a {idade} anos: voto NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'A pessoa com a {idade} anos: voto OPCIONAL'
    else:
        return f'A pessoa com a {idade} anos: voto OBRIGATORIO'
    
    
    
# Programa principal



nascimento = int(input('Informe o seu ano de nascimento: '))
print('Carregando analise...')
sleep(2)

print(voto(nascimento))
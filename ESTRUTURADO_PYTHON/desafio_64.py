'''Programa que analisa a ficha de um jogador'''

def menu():
    print('''
          
          MENU DO SISTEMA 
          
          1. Cadastrar jogador...
          2. Entendendo o programa...
          3. Sair...          
          
        ''')
    


def ficha(jog='desconhecido', gol=0):
    """ 
    Args:
        jog (str, optional): _description_. Defaults to 'desconhecido'.
        gol (int, optional): _description_. Defaults to 0.
    """
    print(f'O jogador {jog} fez {gol} em todo o campeonato.')
    
    
# Programa principal

n = str(input('informe o nome do jogador: '))
g = str(input('informe a quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g=0
    
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
    
help(ficha)
    

    
    
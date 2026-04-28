'''Usando funções Analise de um Terreno'''

def linha():
    print('~' * 80)
    
    
def analise_terreno(largura, comprimento):
    print(f'A area do terreno {largura} x {comprimento} e de {largura*comprimento} ')
    
    

print('Programa de analise de Terreno, Vamos la ?')
linha()

largura = float(input('Informe a Largura (M): '))
comprimento = float(input('Informe o Comprimento (M): '))

analise_terreno(largura=largura, comprimento=comprimento)



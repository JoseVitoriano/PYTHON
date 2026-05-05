'''Programa de analise de analise de site'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/JoseVitoriano')
except urllib.error.URLError:
    print('O site não esta disponivel...')
    
else:
    print('Consegui acessar o site.')
    print(site.read())
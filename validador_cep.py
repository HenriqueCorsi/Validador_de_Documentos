import re
import requests

def validador_cep(cep):
    cep = str(cep)
    if len(cep) == 8:
        padrao = '([0-9]{5})([0-9]{3})'
        regx = re.search(padrao, cep)
        if regx:
            cep_formatado = f'{regx.group(1)}-{regx.group(2)}'
            print('-------------------------------')
            print(f'CEP -> {cep_formatado} é válido')
            print('-------------------------------')
        else:
            print('CEP inválido')
    else:
        print('CEP inválido!')

def acessando_cep(cep):
    url_api = f'https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url_api)
    infos = r.json()
    print( 'Rua:',infos['logradouro'],'\nBairro:', infos['bairro'],'\nCidade:', infos['localidade'],'\nEstado:', infos['uf'])
    print('-------------------------------')    
    
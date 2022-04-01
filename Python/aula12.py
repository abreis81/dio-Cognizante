## o que são pacotes
## o que é o instalador de pacotes do python (PIP)
## como instalar um pacote no python
## como listar pacotes instalados no python
## como utilizar um pacote
## instalar nosso primeiro pacote (Requests)
## Realizar uma requisição http com requests


import requests

## capturar dados de cep da internet formato json
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    ## print(type(response.text))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

## retorna imagem api do pokemon
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

## raspagem de dados
## retorna o html de uma url
def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('02430001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://digitalinnovation.one/')
    print(response)
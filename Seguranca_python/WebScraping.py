## Ferramenta de coleta de dados web


## Bibliotecas
## BeautifulSoup - é uma biblioteca de extração de dados de arquivos HTML e XML
## requests - permite que você envie solicitações HTTP em Python

from bs4 import BeautifulSoup
import requests 

## pega toda a informação HTML do site
site = requests.get("https://www.climatempo.com.br/").content
# . content é para fazer o get e pegar o conteudo
# objetos site recebendo todo o conteudo da requisição

soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixando do site o html


#print(soup.prettify())
# transforma html em string e o print vai exibir o html


## para fazer analise precisa diseer em clase está
#temperatura = soup.find("span", class_ ="_block _margin-b-5 -gray")

temperatura = soup.find("span", class_="temperature _margin-l-5 -font-13")
#velocidadeVento = soup.find("span", class_="-gray")

print(temperatura.string)
#print(velocidadeVento)

# imprime o bloco p pode ser qualquer um que exista
print(soup.p.string)

## busca no conteudo
print(soup.find('admin'))
### Script para utilizar um web crawler para inddexar paginas da internet
## retorna as palavras cm mais frequencia

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter



def start(url):

    wordList = []
    source_code = requests.get(url).text

    # requisição dos dados do html
    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    # vai procurar no codigo tudo que tem div e classe
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # cada conteudo será uma linha
        words = content.lower().split()


        for each_word in words:
            wordList.append(each_word)
        clean_wordList(wordList)


def clean_wordList(wordList):
    clean_list = []
    for word in wordList:

        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        # se ele achar um dos simbolos ele faz um replace
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

## Mostra as palavras chaves que mais apareceram
    for key, value in sorted(word_count.items() , key = operator.itemgetter(1)):
        print ("% s : % s " % (key, value))
    
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

## função start
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
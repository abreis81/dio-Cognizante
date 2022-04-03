## Wordlists são arquivos contendo uma palavra por linha. São usados para testes de quebras de senha

## biblioteca para iterações
import itertools
from unittest import result


string = input("String a ser permutada: ")

##resultado = itertools.permutations('abcdef', 5)

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
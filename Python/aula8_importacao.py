## como realizar a importação de um módulo
## entender a importância de se trabalhar com vários módulos
## Acessando classes e métodos de um módulo
## Entendendo e trabalhando com funções anônimas (lambda)

## arquivo.py é um módulo, dentro do projeto

from aula7_televisao import Televisao
from aula7_calculadora import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora()
    print(calculadora.soma(5, 10))
    lista = ['cachorro','gato','elefante']
#    print(contador_letras(lista))
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())
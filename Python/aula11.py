## como lançar um exceção genérica
## utiliza exceções específicas
## encadeamento de exceções
## else e finally
## Criação de exceções customizadas


##forçar erro
#divisao = 10 / 0

#tratar erro
#try:
#    divisao = 10 / 0
#except ZeroDivisionError:
#    print('Não é possível realizar divisão por zero')


#tratar erro
lista = [1, 10]
arquivo = open('teste.txt','r')
try:
    divisao = 10 / 0
    numero = lista[1]
    #x = a

    # linhas levas para o finally # teste com erro antes
    #print('fechando arquivo')
    ##arquivo.close()
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
## BaseException é o pai de todas as excessões
#except BaseException as ex:
#    print('Erro desconhecido. Erro: {}'.format(ex))
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
    ## usado para colocar um treço do codigo que só roda se não ocorre erros
finally:
    ## sempre irá executar mesmo que de erro antes
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()

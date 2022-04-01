import shutil

## como gerar e escrever em um arquivo
## como ler informações de um arquivo
## como trabalhar com as informações dos arquivos
## como trabalhar melhor com strings
## como copiar e mover arquivos


###### com o open conseguimos criar ou abrir um aquivo
#### o 'w' ele gera arquivo se não existir ou irá sobreescrever
#### arquivo = open('teste.txt', 'w')
#### o 'a' ele gera o aquivo se não existir e faz apend caso exista
#arquivo = open('teste.txt', 'a')
####arquivo.write('Minha primeira escrita')
### \n quebra a linha
#arquivo.write('\nsegunda linha')
#arquivo.close()


## função para escrever arquivo
def escrever_arquivo(texto):
    ## se não passar  o diretorio ele gera no mesmo lugar de onde está o arquivo python
    diretorio = 'C:\Projetos\DIO\Python\teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

#def atualizar_arquivo(texto):
#    arquivo = open('teste.txt', 'a')
#    arquivo.write(texto)
#    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    # 'r' arquivo sera aberto em modo leitura
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    ## o split quebra pelo passado no ''
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'c:/apaga/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'c:/apaga')

if __name__ == '__main__':
    #print(media_notas('notas.txt'))
    ##print(lista_media)

    # escrever_arquivo('Primeira linha. \n')
    # atualizar_arquivo('Segunda linha. \n')

    # aluno = 'Mauricio, 8, 9, 3, 5\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')

    #copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
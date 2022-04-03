# biblioteca para trabalhar com hash
import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH #### 
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            Digite o número do hash a ser gerado:  '''))


# variavel para armazenar o hash
## o b convert a string em bytes
##resultado = hashlib.md5(b'Python Security')

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O Hash MD5 da string é: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O Hash SHA1 da string é: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O Hash SHA256 da string é: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O Hash SHA512 da string é: ', string, 'é: ', resultado.hexdigest())
else:
    print('Algo de errado não deu certo, tente novamente')
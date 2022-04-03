

# biblioteca para trabalhar com hash
import hashlib


string = input("Digite o texto a ser gerado a hash: ")

# variavel para armazenar o hash
## o b convert a string em bytes
##resultado = hashlib.md5(b'Python Security')

resultado = hashlib.md5(string.encode('utf-8'))

print("O Hash da string é: ", resultado.hexdigest())
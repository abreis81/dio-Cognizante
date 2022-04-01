## projeto de um chat com cliente e servidor

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket Criado com Sucesso!!!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, firmeza?'

## para enviar a mensagem
try:
    print('Cliente:' + mensagem)

#encode é é para empacotar a mensagem com o protocolo udp   , sendto para envio
    s.sendto(mensagem.encode(), (host, 5432))

## 4096 bits, referente ao tamanho máximo que a mensagem pode ter
    dados, servidor = s.recvfrom(4096)
    ## desempacotar a mensagem
    dados = dados.encode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close()
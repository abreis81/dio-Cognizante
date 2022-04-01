import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com sucesso')

host = 'localhost'
port = 5432

# bind é para fazer a ligação cliente / servidor
s.bind((host, port))

mensagem = 'Servidor: Ola Cliente e ai beleza?'

while 1:
    dados, end = s.recvfrom((4096))

if dados:
    print('Servidor enviando mensagem...')
    s.sendto(dados + (mensagem,ecode()), end)
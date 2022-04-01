## biblioteca que fornece acesso de baixo nível à interface de rede
## o S.O. fornece a API socket que relaciona o programa com a rede
## sript tenta fazer conexão e responde se conseguiu ou não

import socket
import sys
## biblioteca sys fornce acesso a alguma variavies e funções do interpretador do python

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou Ip a ser nectado: ")
    PortaAlvo = input("Digite a porta a ser connectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: "+ HostAlvo +" e na Portal: "+ PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host: "+ HostAlvo +" e na Portal: "+ PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()
        # sys.exit é para ele sair da aplicação

if __name__ == "__main__":
    main()
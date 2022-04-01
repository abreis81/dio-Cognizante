import os
# importa o modula ou biblioteca os ( integra os programas e recursos do S.O

print("#" * 80) ## IMPRIMINDO o # 80 vezes
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
print("-" * 80)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 80)
## Laços de repetição
## for com range

#for x in range(101):
#    print(x)

## mostrar se um numero é primo
## for x in range(0, 101):

# a = int(input('Entre como número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(a, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))




## Mostrar primos entre 0 e  100

# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#          resto = num % x
#          if resto == 0:
#              div += 1
#     if div == 2:
#          print(num)


## while
nota = int(input('Entre com a nota'))
while note > 10:
    nota = int(input('Nota inválida. Entre com a nota correta: '))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1
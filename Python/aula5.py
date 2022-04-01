## criação de lista
## pode misturar tipo de dados, mas não é recomendado
lista =  [1, 3, 5, 7, 12, 4, 20]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#print(lista_animal[1])


#for x in lista_animal:
#    print(x)

# soma da lista
#print(sum(lista))

#maior valor
#print(max(lista))

# saber se já existe um valor na lista
# if 'gato' in lista_animal:
#     print('existe o animal na lista')
# else:
#     print('não existe o animal na lista')

# possivel operações com a lista
#nova_lista = lista_animal * 3
#print(nova_lista)



# saber se já existe um valor na lista, se não existir será adicionado
# if 'lobo' in lista_animal:
#     print('existe o animal na lista')
# else:
#     print('não existe o animal na lista. Será incluído')
#     lista_animal.append('lobo')
#     print(lista_animal)

## retirar o ultimo da lista
#lista_animal.pop()
#print(lista_animal)

## retirar uma posição da lista
#lista_animal.pop(1)
#print(lista_animal)

## se já saber o nome pode usar remove
# lista_animal.remove('elefante')
# print(lista_animal)

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)


lista_animal[0] = 'macaco'
print(lista_animal)



####### Tuplas
## não dá para alterar valores
tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))
print(len(lista_animal))

## converter lista para tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

## coverter tupla para lista
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

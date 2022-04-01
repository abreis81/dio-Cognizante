## lista {}
## tupla ()
## conjunto []

## conjunto não tem duplicidade

#conjunto = {1, 2, 2, 3, 4}
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)


conjunto= {1, 2, 3, 4, 5}
conjunto2= {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
# lita o que tem nos dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

#lista a diferença
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))


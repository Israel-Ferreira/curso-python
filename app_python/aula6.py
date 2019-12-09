# conjunto = {1,2,3,4,5,6}
# print(conjunto)

# conjunto.add(7)
# conjunto.discard(2)

# print(conjunto)

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

conjunto_diferenca =  conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)

print(conjunto_diferenca)
print(conjunto_diferenca2)

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("A diferença simetrica entre A e B: {}".format(conjunto_diff_simetrica))

conjunto_a =  {1,2,3}
conjunto_b = {1,2,3,4,5}


conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista =  [1,2,3,4,4,5,5,6,7,8,10,8]
novo_conjunto = set(lista)

new_conjunto =  set(['gato','gato','cachorro','cachorro'])


print(novo_conjunto)
print(new_conjunto)

nova_lista = list(new_conjunto)
print(nova_lista)

tamanho_set = len
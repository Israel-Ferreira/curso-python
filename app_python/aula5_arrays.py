lista = [12,89,1,73,65,120]
lista_animais = ['Gato','Cachorro','Elefante','Rato']

print(type(lista))
print(lista_animais[0])

nova_lista_animal = lista_animais * 3
print(nova_lista_animal)

soma = 0
for num in lista:
    soma += num

soma2 = sum(lista)


def print_result(resultado):
    print("O resultado da soma é {}".format(resultado))


for animal in lista_animais:
    print(animal)


print_result(soma)
print_result(soma2)

print(min(lista))
print(max(lista))

print(min(lista_animais))
print(max(lista_animais))

if 'Lobo' in lista_animais:
    print('Existe o Lobo na lista')
else:
    print('Não Existe o Lobo na lista')
    lista_animais.append('Lobo')


lista.sort()

lista_animais.sort()

print(lista)
print(lista_animais)


print(len(lista_animais))

tupla_animal = tuple(lista_animais)

lista.reverse()
print(lista)
print(tupla_animal)
# print(lista_animais)
# lista_animais.pop()
# lista_animais.pop(1)
# print(lista_animais)

# lista_animais.remove("Elefante")
# print(lista_animais)

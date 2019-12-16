contador_letras =  lambda lista:  [len(x) for x in lista]
lista = contador_letras(["Gato","Cachorro"])
print(lista)

soma = lambda x,y: x + y

print(soma(10,2))
subtracao =  lambda x, y: x - y
print(subtracao(10,2))


calculadora = {
    'soma': lambda x, y: x + y,
    'sub': lambda x,y: x - y,
    'multi': lambda x, y: x * y,
    'divisao': lambda x,y: x / y
}

print(type(calculadora))
soma_raiz = calculadora['soma']
multi = calculadora['multi']

print(soma_raiz(10,2))
print(multi(10,3))

print("A soma é {}".format(soma_raiz(10,3)))
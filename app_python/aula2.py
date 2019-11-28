a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao =  a / b
resto = a % b

resultados = [
    {"operacao": "Soma", "valor": soma},
    {"operacao": "Subtracao","valor": subtracao},
    {"operacao": "Multiplicacao", "valor": multiplicacao},
    {"operacao": "Divisao", "valor": divisao},
    {"operacao": "Divisao Inteira", "valor": resto},
]

for res in resultados:
    print("O resultado da {0} é: {1} \n".format(res["operacao"],res["valor"]))

print(int(divisao))

# x = '1'

# soma2 =  int(x) + 1
# print(soma2)
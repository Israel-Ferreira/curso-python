range_num = int(input('Digite um número: '))

numeros_primos = []

for num in range(1,range_num + 1):
    divisores= []
    for x in range(1, num + 1):
        if num % x == 0:
            divisores.append(x)

    if divisores == [1, num]:
        numeros_primos.append(num)

print(numeros_primos)
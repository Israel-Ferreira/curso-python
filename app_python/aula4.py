num = int(input('Digite um número: '))

divisores = []

for x in range(1,num + 1):
    if num % x == 0:
        divisores.append(x)

if divisores == [1,num]:
    print("{} é primo".format(num))
else:
    print("{} não é primo".format(num))

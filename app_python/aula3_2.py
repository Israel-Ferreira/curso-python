a = int(input("Digite  o primeiro número: "))
b = int(input("Digite  o segundo número: "))

if a % 2 == 0 or (not b % 2 > 0):
    print('Foi digitado um número par')
else:
    print("Nenhum número digitado é par")
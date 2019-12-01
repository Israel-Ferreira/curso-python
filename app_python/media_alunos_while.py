def add_nota(bim):
    nota = float(input('{bim} ° Bimestre:  '.format(bim=bim)))

    if nota < 0  or nota > 10:
        while nota < 0 or nota > 10:
            nota = float(input('Você digitou errado; {bim} ° Bimestre: '.format(bim=bim)))

    return nota


def get_media(notas):
    return sum(notas) / len(notas)

notas = []

for i in range(1,5):
    notas.append(add_nota(i))

media = get_media(notas)

print(media)

if media >= 7:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Exame')
else:
    print('Reprovado')

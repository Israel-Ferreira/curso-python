def note_input(bim):
    nota = float(input('{} ° Bimestre: '.format(bim)))
    if nota > 10 or nota < 0:
        nota =  float(input('Você digitou errado a nota; {} Bimestre: '.format(bim)))
    
    return nota

notas = [note_input(1), note_input(2), note_input(3), note_input(4)]

media = sum(notas) / len(notas)

print("Media: {}".format(media))

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Exame")
else:
    print("Reprovado")


from aluno import Aluno
from file_system import FileSystem


if __name__ == "__main__":
    fs = FileSystem('notas.txt')
    qtde_alunos =  int(input("Digite a quantidade de alunos da sala:  "))

    medias =  []

    if qtde_alunos > 0:
        for i in range(1,(qtde_alunos + 1)):
            nome = input('Digite o nome do aluno: ')
            notas = []

            j = 1

            while j <= 4:
                nota = float(input('Digite a {} ª nota: '.format(j)))
                notas.append(nota)
                j += 1

            
            aluno =  Aluno(nome,notas)
            medias.append(aluno.media())

            fs.append_file(aluno.situacao_aluno())

    else:
        alunos =  fs.read_file().split("\n")
        alunos.pop()
        nome = ""

        for aluno in alunos:
            notas_alunos = aluno.split(",")

            nome = notas_alunos[0]
            notas_alunos.pop(0)

            notas = [float(nota) for nota in notas_alunos]

            aluno = Aluno(nome, notas)
            medias.append({nome : aluno.media()})


        
        
        
    fs2 = FileSystem('medias.txt')
    for media in medias:
        fs2.append_file(("{} \n".format(str(media))))
    
    
    fs2.move_file('/home/israel/curso-python/app_python')



















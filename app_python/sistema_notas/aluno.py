class Aluno:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
    
    def media(self):
        return sum(self.notas) / len(self.notas)
    

    def situacao_aluno(self):
        str_notas =  "{}".format(self.nome)

        for i in range(len(self.notas)):
            bimestre = "{nota}, ".format(bim=(i + 1), nota=self.notas[i])
            str_notas += bimestre


        return "{} \n".format(str_notas).join(",")




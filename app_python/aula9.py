class FileSystem:
    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo



    def escrever_arquivo(self,texto):
        self.mode = "w"
        self.handle_file(texto)

    
    def atualizar_arquivo(self,texto):
        self.mode = "a"
        self.handle_file(texto)


    
    def ler_arquivo(self):
        self.mode = "r"
        conteudo_arquivo = self.handle_file()
        return conteudo_arquivo

        

    def handle_file(self, texto=""):
        file = open(self.nome_do_arquivo,self.mode)

        if (self.mode == "a" or self.mode == "w") and texto != "":
            file.write(texto)
            file.close()
        else:
            conteudo = file.read()
            return conteudo




if __name__ == "__main__":
    fs = FileSystem('teste.txt')
    res = fs.ler_arquivo()
    print(res)


    









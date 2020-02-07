class NotaException(Exception):
    def __init__(self,message=None):
        self.message = message


    def __str__ (self):
        if self.message:
            return "Erro: {}".format(self.message)
        else:
            return "Nota Inválida: Nota menor que 0 ou maior que 10"
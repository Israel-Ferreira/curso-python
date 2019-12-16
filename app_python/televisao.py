class Televisao:
    def __init__(self,marca,tipo):
        self.ligada = False
        self.marca = marca
        self.tipo =  tipo
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def status(self):
        if self.ligada:
            return "A televisão da {marca} {tipo} está ligada".format(marca = self.marca, tipo = self.tipo)
        else:
            return "A televisão da {marca} {tipo} está desligada".format(marca = self.marca, tipo = self.tipo)


    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1


    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1

          
if __name__ == "__main__":
    televisao = Televisao("Samsung","QLED")
    televisao.power()
    print(televisao.status())

    televisao.power()
    print(televisao.status())


    televisao.power()
    televisao.aumentar_canal()
    televisao.aumentar_canal()
    televisao.diminuir_canal()

    print("A televisão está no canal: {}".format(televisao.canal))


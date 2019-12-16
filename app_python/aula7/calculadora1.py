class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def subtracao(self):
        return self.num1 - self.num2

    def soma(self):
        return self.num1 + self.num2

    def mult(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 == 0:
            raise Exception("Erro Divisão Por Zero")
        else:
            return self.num1 / self.num2




if __name__ == "__main__":
    calculadora = Calculadora(10,2)

    print(calculadora.soma())
    print(calculadora.subtracao())

    print(calculadora.mult())
    print(calculadora.divisao())




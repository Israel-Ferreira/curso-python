class Calculadora:
    def subtracao(self,num1,num2):
        return num1 - num2

    def soma(self,num1,num2):
        return num1 + num2

    def mult(self,num1,num2):
        return num1 * num2

    def divisao(self,num1,num2):
        if num2 == 0:
            raise Exception("Erro Divisão Por Zero")
        else:
            return num1 / num2



calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.subtracao(16,14))

print(calculadora.mult(90,2))
print(calculadora.divisao(4,2))
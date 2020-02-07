lista = [1,10]
try:
    arquivo  = open('../medias.txt','r')
    divisao = 10 / 1
    numero =  lista[1]
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except ArithmeticError:
    print("Houve um erro ao fazer uma operaçãp aritmética")
except IndexError:
    print("Erro ao acessar um indice inválido da lista")
except Exception as ex:
    print("Erro Desconhecido: {err}".format(err=ex))
else:
    print(arquivo.readlines())
    print('Executa quando não ocorre exceção')
finally:
    print('Executa Independente se tiver exceção ou não')
    arquivo.close()



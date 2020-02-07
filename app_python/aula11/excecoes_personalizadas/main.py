from nota_exception import NotaException

while True:
    try:
        nota = float(input('Entre com uma nota entre 0 a 10: '))

        if nota > 10:
            raise NotaException("Nota maior que 10")
        elif nota < 0:
            raise NotaException("Nota menor que 0")
        else:
            print("A nota digitada é: {nota}".format(nota=nota))
            break
    except NotaException as nex:
        print(nex)
    except Exception as ex:
        print(ex)



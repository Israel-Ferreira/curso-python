def contador_letras(lista_palavras):
    lista_num_letras =  []

    for palavra in lista_palavras:
        lista_num_letras.append(len(palavra))

    return lista_num_letras 



if __name__ == "__main__":
    arr = contador_letras(["Gato","Cachorro", "Coruja"])
    print(arr)
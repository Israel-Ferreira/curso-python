import requests


def make_get_requests(url):
    return requests.get(url).json()


def retorna_dados_cep(cep):
    new_cep  =  "".join(cep.split("-"))
    url = 'https://viacep.com.br/ws/{cep}/json/'.format(cep=new_cep)
    return make_get_requests(url)



def retorna_dados_pokemon(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    return make_get_requests(url)


def retorna_response(url):
    resultado = requests.get(url)
    return resultado.text


if __name__ == '__main__':
    cep = "01311-000"
    resultado = retorna_dados_cep(cep)
    print(resultado)

    print("\n")

    pokemon = "pikachu"
    rslt = retorna_dados_pokemon(pokemon)
    print(rslt)

    print("\n")

    site = "https://meiobit.com/"
    res_site = retorna_response(site)
    print(res_site)





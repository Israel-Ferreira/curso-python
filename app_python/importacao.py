from televisao import Televisao
from aula7.calculadora1 import Calculadora
from contador_de_letras import contador_letras

if __name__ == "__main__":
    tv = Televisao("Xiaomi", "LED")
    tv.power()
    print(tv.status())


    calc = Calculadora(10,2)
    div = calc.divisao()
    print(div)


    lista = ['Gato','Cachorro', 'Elefante']
    print(contador_letras(lista))
a  = int(input('Digite o primeiro valor: '))
b =  int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))


def print_greather_number(greather_num):
    print('O maior numero é {}'.format(greather_num))

if a > b and a > c:
    print_greather_number(a)
elif c > a and c > b:
    print_greather_number(c)
else:
    print_greather_number(b)
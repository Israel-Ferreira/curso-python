from datetime import date,time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y  %H:%M:%S")
    print(data_atual)
    print(data_formatada)
    print(data_atual.strftime("%c"))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.month)

    data_string = '01/01/2020'
    data_convertida =  datetime.strptime(data_string,'%d/%m/%Y')

    print(data_convertida)
    print(type(data_convertida))
    nova_data = timedelta()
    print(nova_data)





def dia_da_semana():
    data_atual = datetime.now()
    dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta','Sexta','Sabado','Domingo')
    print(dias_da_semana[data_atual.weekday()])





def trabalhando_com_date():
    data_atual = date.today()
    data_br = data_atual.strftime("%A %B %Y")

    

    print(type(data_atual))
    print(type(data_br))
    print(data_br)


def trabalhando_com_time():
    horario = time(hour=15,minute=30,second=8)
    horario_str = horario.strftime('%H:%M:%S')

    print(type(horario))
    print(type(horario_str))


    print(horario)
    print(horario_str)
    # pass


if __name__ == "__main__":
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
    dia_da_semana()
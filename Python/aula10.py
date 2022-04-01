## como recuperar a data atual (date)
## como trabalhar com a data, alterando sua formatação
## como gerar um horário (time)
## Retornar data e hora atual (datetime)
## alterar formatação do datetime
## Realizar soma e subtração de data com timedelta

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    ## formatação olhar documentação
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))
    # convertendo para string
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual)
    print(type(data_atual_str))
    print(data_atual_str)

def trabalhando_com_time():
    # criar um horario
    horario = time(hour=15, minute=18, second=30)
    print(type(horario))
    print(horario)
    ##podendo formatar
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))
    print(horario_str)

def trabalhando_com_datetime():
    datahora_atual = datetime.now()
    print(datahora_atual)
    print(datahora_atual.strftime('%d/%m/%Y'))
    print(datahora_atual.strftime('%H:%M:%S'))
    print(datahora_atual.strftime('%d/%m/%Y %H:%M:%S'))
    # formatacao especial para o datetime
    print(datahora_atual.strftime('%c'))
    # possivel pegar também o dia .day, ano .year etc
    print(datahora_atual.day)
    print(datahora_atual.month)
    print(datahora_atual.year)
    print(datahora_atual.hour)
    print(datahora_atual.weekday())
    ## para converter para o dia da semana em portugues
    ## criar uma tupla, já que a funcao weekday retorna um numero
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[datahora_atual.weekday()])
    ##possivel também criar uma data
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # converte string para data
    data_string = '01/01/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(type(data_string))
    print(type(data_convertida))
    print(data_convertida)

    ## subtrair/somar dias
    nova_data=data_convertida - timedelta(days=365)
    print(nova_data)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)



if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()